#!/usr/bin/python3
import subprocess
import argparse

command = "msg * you have been hacked"
subprocess.Popen(command,shell = True)