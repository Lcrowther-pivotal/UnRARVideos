import os
from subprocess import check_call
from os.path import join

rx = '(.*rar$)|(.*r00$)'
path = "/Users/XXX/rartest/"
extensions = "[.mkv,.avi]"

def runUnRar(path,cmd_part):
    for root, dirs, files in os.walk(path):
        if not any(f.endswith(extensions) for f in files):
            found_r = False
            for file in files:
                pth = join(root, file)

                try:
                     if not found_r and file.endswith((".rar",".r00")):
                         command = cmd_part
                         command.append(pth)
                         command.append(root)
                         check_call(command)
                         #cmd = ["unrar", "e", "-o-", pth, root]
                         # #check_call(cmd)
                         found_r = True
                         break
                except Exception:
                    print ("OOps! That did not work")


runUnRar(path,["unrar", "e", "-o-"])
