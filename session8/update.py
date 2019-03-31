danhsach = input("Enter your list ").split(",")
print(danhsach)
while True:
    a= input("Do you want to change item name?(Yes/No): ").upper()
    if a == "NO" :
        print(danhsach)
        break
    elif a == "YES":
        num = int(input("Change item no: "))
        danhsach[num-1] = input("Change item name into: ")
        print(*danhsach, sep =',')
    else:
        print("Retype Yes/no ")       
    

# Cho nguoi su dung nhap vao 1 list roi thay doi cac thanh phan cua list
