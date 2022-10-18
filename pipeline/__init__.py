from gaiasdk import sdk
import logging
import time
import subprocess
import os
import git

path_parent = os.getcwd()

source_path = path_parent+"/Vulnerable-Flask-App"
safety_path = path_parent+"/Vulnerable-Flask-App/app/requirements.txt"
pyraider_path = path_parent+"/Vulnerable-Flask-App/app/requirements.txt"
bandit_path = path_parent+"/Vulnerable-Flask-App/app/app.py"

def Clone(args):
    logging.info("Cloning Latest Source started!")
    time.sleep(5)
    
    cmd = "rm -rf {0} | true".format(source_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    stdout, stderr = process.communicate()
    logging.info(stdout)
    logging.info(stderr)
    logging.info("Cleared previous source code")
    
    git.Repo.clone_from('https://github.com/we45/Vulnerable-Flask-App.git', 'Vulnerable-Flask-App')
    logging.info("Cloning Latest Source finished!")
    
def RunBandit(args):
    logging.info("Bandit has been started!")
    cmd = "bandit -r -f json {0}".format(bandit_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    stdout, stderr = process.communicate()
    logging.info(stdout)
    logging.info(stderr)
    logging.info("Bandit has been finished!")
    logging.info("==================================================")

def RunSafety(args):
    logging.info("Safety has been started!")
    cmd = "safety check -r {0} --output json".format(safety_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    stdout, stderr = process.communicate()
    logging.info(stdout)
    logging.info(stderr)
    logging.info("Safety has been finished!")
    logging.info("==================================================")

def RunPyraider(args):
    logging.info("Pyraider has been started!")
    cmd = "pyraider check -f {0}".format(pyraider_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    stdout, stderr = process.communicate()
    logging.info(stdout)
    logging.info(stderr)
    logging.info("Pyraider has been finished!")
    logging.info("==================================================")

def main():
    logging.basicConfig(level=logging.INFO)
    clone = sdk.Job("Clone Source", "Cloning Latest Source", Clone)
    runbandit = sdk.Job("Run Bandit Scan", "Running Bandit Scan", RunBandit,["Clone Source"])
    runsafety = sdk.Job("Run Safety Scan", "Running Safety Scan", RunSafety, ["Run Bandit Scan"])
    runpyraider = sdk.Job("Run Pyraider Scan", "Running Pyraider Scan", RunPyraider, ["Run Safety Scan"])
    sdk.serve([clone, runbandit, runsafety, runpyraider])
