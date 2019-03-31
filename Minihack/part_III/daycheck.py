a = int(input("Insert month: "))
b = int(input ("Insert year: "))
if a in [1,3,5,7,8,10,12]:
    print ("This month has 31 days")
if a in [4,6,9,11]:
    print ("This month has 30 days")
if a == 2:
    if b % 4 == 0:
        print ("This month has 29 days")
    else:
        print ("This month has 28 days")