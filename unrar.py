import os
from subprocess import check_call
from os.path import join

rx = '(.*rar$)|(.*r00$)'
path = "/Users/xxxxxx/rartest/Sample"


def runUnRar(path):
    for root, dirs, files in os.walk(path):
        if not any(f.endswith(".avi") for f in files):
            found_r = False
            for file in files:
                pth = join(root, file)
                try:
                     if not found_r and file.endswith((".rar",".r00")):
                         check_call(["unrar","x", pth, root])
                         found_r = True
                         break
                except ValueError:
                    print ("OOps! That did not work")


runUnRar(path)