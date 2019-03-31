n= int(input("Enter the first number of the odd positive sequence: "))
r1= range(n-1,0,-2)
r2 = range (n,0,-2)
if n % 2 == 0 :
    print (*r1)
else:
    print (*r2)

    #Viết chương trình in ra một dãy số lẻ từ n đến 0, n > 0 do người dùng nhập vào