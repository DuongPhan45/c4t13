# Print items in a list
# items =[....]
# no1: for i in range(len(iemts)):
#      print(items[i])
# no2: for item in items:
#      print(item)
# no3: for i, item in enumerate(items)
#      print (i,item)
danhsach = input("Input a list: ").upper()
for i,item in enumerate(danhsach.split(",")):
    print(i+1,".",item)