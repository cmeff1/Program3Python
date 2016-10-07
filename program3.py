#!/usr/local/bin/python3


import sys
import os
import os.path
import stat




#print(len(sys.argv))
if len(sys.argv) == 4 :
    if os.path.isdir(sys.argv[1]) != True:
        print("Incorrect paths try again")
        #break
    elif os.path.isdir(sys.argv[2]) != True:
        print("Incorrect 2nd paths try again")
    elif os.path.isdir(sys.argv[3]) == True:
        print("Dir already exsist please select different name")

    else:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
        newdir = sys.argv[3]
        print(dir1, dir2, newdir)
        
        print("yey!")
elif len(sys.argv) <= 1 :
    print("Missing dirs please re-enter")


os.mkdir( newdir, 493 )
print("new dir created", newdir)

