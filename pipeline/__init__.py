from gaiasdk import sdk
import logging
import time
import subprocess

from pathlib import Path


def RunBandit(args):
    logging.info("Bandit has been started!")
    time.sleep(5)
    print(Path.cwd())
    logging.info("Bandit has been finished!")

def RunSafety(args):
    logging.info("Safety has been started!")
    time.sleep(5)
    logging.info("Safety has been finished!")

def RunPyraider(args):
    logging.info("Pyraider has been started!")
    time.sleep(5)
    logging.info("Pyraider has been finished!")

def main():
    logging.basicConfig(level=logging.INFO)
    runbandit = sdk.Job("Run Bandit Scan", "Running Bandit Scan", RunBandit)
    runsafety = sdk.Job("Run Safety Scan", "Running Safety Scan", RunSafety, ["Run Bandit Scan"])
    runpyraider = sdk.Job("Run Pyraider Scan", "Running Pyraider Scan", RunPyraider, ["Run Safety Scan"])
    sdk.serve([runbandit, runsafety, runpyraider])
