import math

n = int(input("Nhap n: "))

# Hàm kiểm tra số nguyên tố
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if isPrime(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")
    
    for i in range(n-1, 1, -1):
        if isPrime(i):
            print("So nguyen to gan n nhat va be hon n la:", i)
            break
