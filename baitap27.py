import math
n = int(input("Nhập n: "))

i = 2
while i <= n:
    while n % i == 0:
        print(i, end=" ")
        n //= i
        if n > 1:
            print("*", end=" ")
    i += 1
