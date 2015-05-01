__author__ = 'nick'

import sys
import subprocess
import os

if (2 <= len(sys.argv)):
    filewriter = open(os.path.dirname(sys.argv[0]) + "/args.txt", "w")
    for argument in sys.argv:
        if __file__ != str(argument):
            filewriter.writelines(str(argument) + "\n")
    filewriter.close()

print os.path.dirname(sys.argv[0]) + "/args.txt"
args = ["gedit", os.path.dirname(sys.argv[0]) + "/args.txt"]
subprocess.Popen(args)