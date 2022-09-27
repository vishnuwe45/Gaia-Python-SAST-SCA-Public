from gaiasdk import sdk
import logging
import time
import subprocess
import os
import git

path_parent = os.getcwd()
#os.chdir(path_parent)

#safety_path = str(os. getcwd())+"/requirements.txt"
#pyraider_path = str(os. getcwd())+"/requirements.txt"
#bandit_path = str(os. getcwd())+"/app.py"

def Clone(args):
    logging.info("Cloning Latest Source started!")
    time.sleep(5)
    git.Repo.clone_from('https://github.com/we45/Vulnerable-Flask-App.git', 'Vulnerable-Flask-App')
    logging.info("Cloning Latest Source finished!")
    
def RunBandit(args):
    logging.info("Bandit has been started!")
    time.sleep(5)
    logging.info("Bandit has been finished!")

def RunSafety(args):
    logging.info("Safety has been started!")
    #logging.info(safety_path)
    #cmd = "safety check -r {0} --output json".format(safety_path)
    cmd = "ls"
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    stdout, stderr = process.communicate()
    logging.info(stdout)
    logging.info(stderr)
    logging.info("Safety has been finished!")

def RunPyraider(args):
    logging.info("Pyraider has been started!")
    time.sleep(5)
    logging.info("Pyraider has been finished!")

def main():
    logging.basicConfig(level=logging.INFO)
    clone = sdk.Job("Clone Source", "Cloning Latest Source", Clone)
    runbandit = sdk.Job("Run Bandit Scan", "Running Bandit Scan", RunBandit,["Clone Source"])
    runsafety = sdk.Job("Run Safety Scan", "Running Safety Scan", RunSafety, ["Run Bandit Scan"])
    runpyraider = sdk.Job("Run Pyraider Scan", "Running Pyraider Scan", RunPyraider, ["Run Safety Scan"])
    sdk.serve([clone, runbandit, runsafety, runpyraider])
