colorList = ['black','white','blue']
while True:
    no = input("Enter position: ")
    if int(no) > len(colorList):
        print("Retype")
    elif no.isdigit():
        print(colorList[int(no)])
        break