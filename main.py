from pathlib import Path
import os


def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))

    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def creatfile():

    try:
        readfileandfolder()
        name=input("please tell you file name:- ")
        p=Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data=input("what you want to write in this file:-")
                fs.write(data)

            print("file created successfully....")
        else:
            print("file already exist...")

    except Exception as err:
        print(f"error accured as {err}")



def readfile():
    try:

        readfileandfolder()
        name=input("please tell which file you want to read:- ")
        p=Path(name)

        if p.exists() and p.is_file:
            with open(p,'r') as fs:
                data=fs.read()
                print(data)

            print("reading file successfully...")
        else:
            print("this file does not exit")

    except Exception as err:
        print(f"error occured as {err}")


def updatefile():
    try:
        
        readfileandfolder()
        name=input("please tell which file you want to update:- ")
        p=Path(name)
        if p.exists() and p.is_file:
            print("press 1 for changing the name")
            print("press 2 for overwriting the you file ")
            print("press 1 for appending some content in your file")

            res=int(input("please tell your resonse:-"))

            if res==1:
                name2=input("tell you new file name:-")
                p2=Path(name2)
                p.rename(p2)

            if res==2:
                with open(p,'w') as fs:
                    data=input("tell what you want to write in overwriting data")
                    fs.write(data)
            if res==3:
                with open(p,'w') as fs:
                    data=input("tell what you want to  append ")
                    fs.write("  "+data)

    except Exception as err:
        print(f"error occured as {err}")


def deletfile():
    readfileandfolder()
    name=input("which file you want to remove:-")
    p=Path(name)

    if p.exists() and p.is_file:
        os.remove(p)



    


print ("press 1 for file creating")
print ("press 2 for file reading")
print ("press 3 for file updating ")
print ("press 4 for file deleting")

check=int(input("please tell you respose:- "))

if check==1:
    creatfile()
    


elif check==2:
    readfile()





elif check==3:
    updatefile()



elif check==4:
    deletfile()




else:
    print("please chose correct choice:")
    