# Chuong trinh game T/F
# Pham vi phep tinh 2 so nho hon 11 khi diem nho hon 20
# Pham vi phep tinh 2 so nho hon 21 khi diem lon hon 20
from random import randint

score = 0

while True:
    if score < 20 :
        a = randint (0, 10)
        b = randint (0, 10)
    else :
        a = randint (0, 20)
        b = randint (0, 20)
    

    x = randint(-1,1)
    y = randint (-1,1)
    if y==0:
        c = a + b + x  
        print (a,"+", b, "=", c)
    else:
        c= a - b + x
        print ( a,"-", b,"=", c)
    

    while True:
        inp = input("Insert T/F: ").upper()
        if inp in ['T','F']:
            break

    if x == 0 and inp == "T":
        print("Correct")
        score +=1
        print ("Your score: ",score)
    elif x != 0 and inp == "F":
        print("Correct")
        score +=1
        print ("Your score: ",score)
    else: 
        print("Incorrect")
        print ("Your score: ",score)
        break

