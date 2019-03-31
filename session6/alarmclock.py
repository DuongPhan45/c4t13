import datetime
import pyglet   



a = int(input("Nhap gio bao thuc: "))
b = int(input("Nhap phut bao thuc: "))

while True:
    time = datetime.datetime.now().time()
    print(time.hour, time.minute, time.second)
    if time.hour == a and time.minute == b :
        music = pyglet.resource.media('StarSky.mp3')
        music.play()
        pyglet.app.run()
        break

# Thực hiện một đồng hồ báo thức đơn giản bằng cách tạo ra 1 vòng lặp chạy liên tục cho đến khi giờ của máy tính bằng số giờ báo thức (ví dụ 20 giờ tối) thì chơi một file wav để đánh thức người dùng


