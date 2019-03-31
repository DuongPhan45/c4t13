while True:
    a = input ("Enter your year of birth ")
    if a.isdigit():
        print ("You are ", 2019-int(a)," years old")
        break
    else:
        print ("Please enter a digit")