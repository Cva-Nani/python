fp=open("data.txt","r")
li=fp.readlines()
#print(li)
lcnt=0
wcnt=0
ccnt=0
for line in li:
    lcnt+=1
    lwords=line.split()
    for word in lwords:
        wcnt+=1
        ccnt+=len(word)
print("Number of lines=",lcnt)
print("Number of words=",wcnt)
print("Number of characters=",ccnt)
