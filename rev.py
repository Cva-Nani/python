st=input("Emter a string: ")
le=len(st)
s=""
for ind in range(le-1,-1,-1):
    s+=st[ind];
print("The reverse of:",st," is:",s)
