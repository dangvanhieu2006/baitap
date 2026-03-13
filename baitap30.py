import math
r, p, n = map(float, input("Nhập lãi suất, tiền vốn, thời hạn: ").split())
n = int(n)

print("Lãi suất:", r * 100, "%")
print("Vốn ban đầu:", p)
print("Thời hạn:", n, "năm")

print("Năm   Vốn")

for i in range(1, n + 1):
    p = p * (1 + r)
    print(i, round(p, 2))
