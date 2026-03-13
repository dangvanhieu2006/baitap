n = int(input("Nhap n: "))

s = 0
m = 0

while s + (m + 1) < n:
    m += 1
    s += m

print("m lon nhat la:", m)
