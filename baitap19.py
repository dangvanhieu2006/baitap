import math
h1, m1, s1 = map(int, input("Nhap gio, phut, giay [1]: ").split())
h2, m2, s2 = map(int, input("Nhap gio, phut, giay [2]: ").split())

# đổi sang giây
t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

# hiệu thời gian
t = abs(t2 - t1)

gio = t // 3600
t = t % 3600

phut = t // 60
giay = t % 60

print("Hieu thoi gian:", gio, "gio", phut, "phut,", giay, "giay")
