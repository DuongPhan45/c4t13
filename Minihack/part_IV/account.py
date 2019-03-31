a = input("Insert user name: ")
while True:
    c = input("Insert email: ")
    if "@" in c and "." in c:
        break
    else:
        print("RETYPE")

while True:
    b = input ("Insert password: ")
    d = input("Retype password: ")
    if b == d and len(b)>8 and b.isdigit()==False and b.isalpha()==False :
        break
    else:
        print ("RETYPE")

print ("Username: ",a)
print ("Password: ",b)
print ("Email: ",c)