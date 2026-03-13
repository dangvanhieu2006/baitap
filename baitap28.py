import math
x = float(input("Nhập số thực x: "))
n = int(input("Độ chính xác: "))

if n >= 0:
    kq = round(x, n)
else:
    p = 10 ** (-n)
    kq = round(x / p) * p

print(kq)
