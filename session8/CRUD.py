danhsach = input("Insert a list: ").split(",")
while True:
    while True:
        
        choose = input("Choose: Creat / Read / Update / Delete/ None ").upper()
        if choose in ["C","R","U","D","N"]:
            break
    if choose == "C":
        creat = input("Add an item: ")
        danhsach.append(creat)
        print(*danhsach)
    elif choose == "R":
        if len(danhsach) == 0:
            print ("Empty list")
        else:
            for item in danhsach:
                print(item)
    elif choose == "U":
        num = int(input("Change item no"))
        danhsach[num-1] = input("Change item into: ")
        print("Updated list: ",*danhsach)
    elif choose == "D":
        classify = input("Delete by: Index(a)  Value(b)").upper()
        if classify == "A":        
            index = int(input("Delete intem no: "))
            danhsach.pop(index)
            print(*danhsach)
        if classify == "B":
            value = input("Delete item: ")
            danhsach.remove(value)
            print(*danhsach)
    elif choose == "N":
        break
    