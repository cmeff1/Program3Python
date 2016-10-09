#!/usr/local/bin/python3


import sys
import os
import os.path
import stat
import shutil



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
        direct1 = sys.argv[1]
        source = os.path.join('.',direct1)
        direct2 = sys.argv[2]
        
        newdir = sys.argv[3]
        dest = os.path.join('.',newdir)

        print(direct1, direct2, newdir,source,dest)
        print("yey!")
elif len(sys.argv) <= 1 :
    print("Missing dirs please re-enter")

#dircont1 = os.listdir(direct1)
#print(dircont1)
os.mkdir( newdir, 493 )
print("new dir created", newdir)

#lettera = []
#for letter in direct1:
#    print(letter)




lista = []
def copyfiles_1 (DirI):
    #print("going through dir")
    dircont1 = os.listdir(DirI)
    #listb = []
    #print(dircont1)
    
    for item1 in dircont1:
        lista.append(os.path.join(DirI, item1))
        if os.path.isdir(os.path.join(DirI,item1)):
            copyfiles_1(os.path.join(DirI, item1))
    seta = set(lista)
    return lista

listb = []
def copyfiles_2 (DirII):
    #print("going through dir")
    dircont2 = os.listdir(DirII)
    #listb = []
    #print(dircont1)
    for item2 in dircont2:
        listb.append(os.path.join(DirII, item2))
        if os.path.isdir(os.path.join(DirII,item2)):
            copyfiles_2(os.path.join(DirII, item2))
    setb = set(listb)
    return setb


for item in copyfiles_1(source):
    if os.path.isdir(item):
        newdir = item.replace(source, dest)
        if not os.path.exists(newdir):
            os.mkdir(newdir)
    elif os.path.isfile(item):
        newfile = item.replace(source,dest)
        
        src_file = os.path.join(source, item)
        dst_file = os.path.join(dest, newfile)
        #print("Source", src_file)
        #print("dest", dst_file)
        shutil.copy2(src_file, dst_file)
dirlista = []

