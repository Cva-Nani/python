units=int(input("Emter number of units: "))
amt=200
if units<=100:
    print("Amount=",amt," Rs")
elif units>100 and units<=200:
    amt=amt+(units-100)*3
    print("Amount=",amt," Rs")
elif units>200 and units<=300:
    amt=amt+(units-100)*4
    print("Amount=",amt," Rs")
elif units>300 and units<=400:
    amt=amt+(units-100)*5
    print("Amount=",amt," Rs")
else:
    amt=amt+(units-100)*6
    print("Amount=",amt," Rs")
