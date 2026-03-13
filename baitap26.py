import math
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

a = abs(tu)
b = abs(mau)


while b != 0:
    a, b = b, a % b

uscln = a

tu //= uscln
mau //= uscln


if mau < 0:
    tu = -tu
    mau = -mau

# Xuất kết quả
if mau == 1:
    print("Rút gọn:", tu)
else:
    print("Rút gọn:", tu, "/", mau)
