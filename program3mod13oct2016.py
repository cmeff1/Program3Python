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
    dircont1 = os.listdir(DirI)
    for item1 in dircont1:
        lista.append(os.path.join(DirI, item1))
        if os.path.isdir(os.path.join(DirI,item1)):
            copyfiles_1(os.path.join(DirI, item1))
    return lista

listb = []
def copyfiles_2 (DirII):
    dircont2 = os.listdir(DirII)
    for item2 in dircont2:
        listb.append(os.path.join(DirII, item2))
        if os.path.isdir(os.path.join(DirII,item2)):
            copyfiles_2(os.path.join(DirII, item2))
    return listb

def copy1 (lista):
	for item in lista:
    		if os.path.isdir(item):
        		newdir = item.replace(source1, dest)
        		if not os.path.exists(newdir):
            			os.mkdir(newdir)
    		elif os.path.isfile(item):
        		newfile = item.replace(source1,dest)
        		src_file = os.path.join(source1, item)
        		dst_file = os.path.join(dest, newfile)
        		shutil.copy2(src_file, dst_file)



def copy2 (listb):
	for item in listb:
		if os.path.isdir(item):
			newdirb = item.replace(source2, dest)
			if os.path.exists(newdirb):
				copyfiles_2(newdirb)
			else:
				os.mkdir(newdirb)
		elif os.path.isfile(item):
			newfileb = item.replace(source2,dest)
			if os.path.exists(newfileb):
				timef_1 = os.path.getmtime(newfileb)
				timef_2 = os.path.getmtime(item)
				#print(timef_1, newfileb, "newfileb")
				#print(timef_2, item, "item")
				
				srcb_file = os.path.join(source2, item)
				dstb_file = os.path.join(dest, newfileb)
				if timef_1 < timef_2:
					#srcb_file = os.path.join(source2, item)
					#dstb_file = os.path.join(dest, newfileb)
					print("File exsists")
					print(srcb_file)
					print(dstb_file)
					shutil.copy2(srcb_file,dstb_file)
			else:

				#srcb_file = os.path.join(source2, item)
				#dstb_file = os.path.join(dest, newfileb)
				print("file is new")
				print(srcb_file)
				print(dstb_file)
				shutil.copy2(srcb_file,dstb_file)

copyfiles_1(source1)
copyfiles_2(source2)
copy1(lista)
copy2(listb)
