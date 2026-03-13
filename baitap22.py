import math
n = int(input("Nhập n: "))

dem = 0
tong = 0

print("Các ước số:", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        dem += 1
        tong += i

print("\nCó", dem, "ước số, tổng là:", tong)
