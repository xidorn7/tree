#!/usr/bin/env python3
import subprocess
import sys


# YOUR CODE GOES here

import os
import re


def sortkeys(s):
    return re.sub("[^A-Za-z0-9]+", "", s).lower()


def draw_tree(path, listCount, space):
    fList = os.listdir(path)
    fList = [item for item in fList if item[0] != '.']
    fList = sorted(fList, key=sortkeys)
    for fPos, fileName in enumerate(fList):
        nextPath = os.path.join(path, fileName)
        if fPos == len(fList) - 1:
            print(space + "└── " + fileName)
        else:
            print(space + "├── " + fileName)
        if os.path.isdir(nextPath):
            # update number of folders
            listCount[0] += 1
            if fPos == len(fList) - 1:
                draw_tree(nextPath, listCount, space + "    ")
            else:
                draw_tree(nextPath, listCount, space + '│   ')
        else:
            # update number of files
            listCount[1] += 1
if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    if(len(sys.argv)) > 1:
        path = sys.argv[1]
    else:
        path = "."
    print(path)
    listCount = [0, 0]
    draw_tree(path, listCount, space="")
    print()
    print(str(listCount[0]) + " directories, " + str(listCount[1]) + " files")
