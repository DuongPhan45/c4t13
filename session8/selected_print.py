danhsach = input("Insert a list: ").upper()
for item in danhsach.split(","):
    if "E" in item:
        print(item)
# In ra list của bài tập trước mỗi phần tử này một dòng, chỉ in ra các phần tử có chứa chữ 'e' hoặc 'E' :