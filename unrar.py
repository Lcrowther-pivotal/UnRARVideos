import os
from subprocess import check_call
from os.path import join
import os

path = "/Users/lcrowther/rartest/movies/"
movie_extensions = [".mkv", ".avi"]
extensions_to_delete = [".rar"]
#build up full list of ".rxx" files to delete
for x in xrange(0, 10):
    for y in xrange(0, 10):
        extensions_to_delete.append(".r"+str(x)+str(y))


def doUnRAR(path, cmd_part):
    for root, dirs, files in os.walk(path):
        found_r = False
        for file in files:
            pth = join(root, file)

            try:
                 if not found_r and file.endswith((".rar",".r00")):
                     command = cmd_part[:]
                     command.append(pth)
                     command.append(root)
                     check_call(command)
                     found_r = True
                     break
            except Exception as e:
                print ("OOps! That did not work: ")

def doDelete(path, cmd_part):
    for root,dirs, files in os.walk(path):
        for file in files:
            pth = join(root, file)
            try:
                if not os.path.isdir(pth) and file.endswith(tuple(extensions_to_delete)):
                    command = cmd_part[:]
                    command.append(pth)
                    check_call(command)
            except Exception as e:
                print ("OOps! That did not work: " +str(e))


#first execute the unrar process
doUnRAR(path, ["unrar", "e", "-o-"])

#next execute the delete process
doDelete(path, ["rm"])

