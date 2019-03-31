# Delete an item
# no1: index_base: item.pop(index)
# no2: value_base: item.remove('value')
danhsach = input("Enter your list ").split(",")
print(*danhsach, sep= ',')
while True:
    a = input("Do you wanna delete an item (Yes/No): ").upper()
    if a == "YES":
        while True:
            classify= input("Choose way to delete: (a)Index base  (b)Value base   (type a/b): ").upper()
            if classify =="A":
                index = int(input("Enter item number: "))
                danhsach.pop(index-1)
                break
            elif classify =="B":
                value = input("Enter item value: ")
                if value in danhsach:
                    danhsach.remove(value)
                    break
                else:
                    print("Inserted item is not in the list")
                    break
            else:
                print ("Retype a/b")

    elif a== "NO":
        print(*danhsach, sep = ',')
        break
    else:
        print ("Retype Yes/No")

# Cho nguoi dung nhap vao mot list roi xoa thanh phan tu chon theo value hoac index