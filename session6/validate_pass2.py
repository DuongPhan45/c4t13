while True:
    a = input ("Enter your password ")
    if a.isalpha():
        print ("Your password must contain at least a number")
    elif len(a)<9:
        print ("Your password must contain more than 8 characters")
    else:
        print ("Your password is valid ", a)
        break
# Viết một chương trình yêu cầu người dùng nhập mật khẩu, nếu mật không không chứa số  hoặc không có trên 8 ký tự, yêu cầu người dùng nhập lại

# while True:
#     a = input ("Enter your password:  ")
#     if a.isalpha() == False and len(a) > 8:
#         print (a)
#         break
#     else:
#         print ("try again")