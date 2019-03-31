while True:
    name = input ("Please enter your name without any special characters ")
    if name.isalpha():
        print ("Your name is ", name)
        break
    else :
        print ("Error. Your name must not contain a special character")
        
# Viết một chương trình yêu cầu người dùng nhập tên, nếu trong tên có chữ số, yêu cầu họ nhập lại