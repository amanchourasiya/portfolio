import os.path

def getID():
    if os.path.isfile('./apiserver/count.txt'):
        fileobj=open("./apiserver/count.txt","r")
        idi=fileobj.read()
        fileobj.close()
        idi=int(idi)
        idi=idi+1
        idi=str(idi)
        fileobj=open("./apiserver/count.txt","w")
        fileobj.write(idi)
        fileobj.close()
    else:
        fileobj=open("./apiserver/count.txt","w")
        idi=1
        idi=str(idi)
        fileobj.write(idi)
        
        fileobj.close()
        
    return idi
