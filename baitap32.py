n = int(input("Nhap n: "))

print("Chuoi hailstones:")

while n != 1:
    print(n, end=" ")
    
    if n % 2 == 0:      # n chẵn
        n = n // 2
    else:               # n lẻ
        n = 3*n + 1

print(1)
