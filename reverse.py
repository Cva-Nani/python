num=int(input("Enter a number: "))
n=num
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("The reverse of:",num," is:",rev)
