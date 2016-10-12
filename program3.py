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
        source1 = os.path.join('.',direct1)
        direct2 = sys.argv[2]
        source2 = os.path.join('.',direct2)
        newdir = sys.argv[3]
        dest = os.path.join('.',newdir)

        #print(direct1, direct2, newdir,source,dest)
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
    #seta = set(lista)
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
    #setb = set(listb)
    return listb


for item in copyfiles_1(source1):
    if os.path.isdir(item):
        newdir = item.replace(source1, dest)
        if not os.path.exists(newdir):
            os.mkdir(newdir)
    elif os.path.isfile(item):
        newfile = item.replace(source1,dest)
        
        src_file = os.path.join(source1, item)
        dst_file = os.path.join(dest, newfile)
        #print("Source", src_file)
        #print("dest", dst_file)
        shutil.copy2(src_file, dst_file)


for itemb in copyfiles_2:
    #print(itemb)
    if os.path.isdir(itemb):
        newdirb = itemb.replace(source2, dest)
        #print(newdirb)
        if os.path.exists(newdirb):
            time_1 = os.path.getmtime(newdirb)
            time_2 = os.path.getmtime(itemb)
            if time_1 < time_2:
                #call copyfiles2(newdirb)
        else:
            os.mkdir(newdirb)
    elif os.path.isfile(itemb):
        newfileb = itemb.replace(source2,dest)
        if os.path.exists(newfileb):
            timef_1 = os.path.getmtime(newfileb)
            timef_2 = os.path.getmtime(itemb)
            if timef_1 < timef_2:
                srcb_file = os.path.join(source2, itemb)
                dstb_file = os.path.join(dest, newfileb)
                shutil.copy2(srcb_file,dstb_file)
        else:
            srcb_file = os.path.join(source2, itemb)
            dstb_file = os.path.join(dest, newfileb)
            shutil.copy2(srcb_file,dstb_file)
                
        #need a if path exsist in here 
        src_fileb = os.path.join(source2,itemb)
        dst_fileb = os.path.join(dest, newfile)
        shutil.copy2(src_fileb, dst_fileb)
'''
