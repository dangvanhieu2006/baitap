import math

n = int(input("Nhap n: "))

count = 0
num = 2

while count < n:
    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print(num, end=" ")
        count += 1
    
    num += 1
