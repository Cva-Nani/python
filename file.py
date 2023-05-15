fp=open("info.txt","r")
print(fp.mode)#returns mode of the file
print(fp.name)#returns name of the file
print(fp.closed)#returns False if not closed
fp.close()
print(fp.closed)#return True if file closed
