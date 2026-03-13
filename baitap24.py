import math
n = int(input("Nhập n: "))
so_chu_so = len(str(n))
chu_so_cuoi = n % 10
chu_so_dau = int(str(n)[0])
tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10
dao = int(str(n)[::-1])

print(n, "có", so_chu_so, "chữ số")
print("Chữ số cuối cùng là:", chu_so_cuoi)
print("Chữ số đầu tiên là:", chu_so_dau)
print("Tổng các chữ số là:", tong)
print("Số đảo ngược là:", dao)
