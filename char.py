for row in range(1,6):
    for col in range(1,20):
        if row%2==1 and col<6 or col==1 and row<3 or col==5 and row>3:
            print("Shiva",end="")
        else:
            print(" ",end="")
    print()
