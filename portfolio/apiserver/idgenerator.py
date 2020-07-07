import os.path

def getID():
    counter_file = 'static/.count.txt'
    if os.path.isfile(counter_file):
        fileobj=open(counter_file,'r')
        idi=fileobj.read()
        fileobj.close()
        idi=int(idi)
        idi=idi+1
        idi=str(idi)
        fileobj=open(counter_file,'w')
        fileobj.write(idi)
        fileobj.close()
    else:
        fileobj=open(counter_file,'w')
        idi=1
        idi=str(idi)
        fileobj.write(idi)
        
        fileobj.close()
        
    return 'image-' + idi
