import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path_repository', type=str)

args = parser.parse_args()

path = args.path_repository

# linux
# def run_scripts(path):
#     proc = subprocess.Popen(path, stdout=subprocess.PIPE)
#     output = proc.stdout.readline()
#     print(output)

# Windows
def run_scripts(path):
    os.popen(f"sh {path}")


run_scripts(path)