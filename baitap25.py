import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Tìm USCLN
x = a
y = b

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

uscln = x

# Tìm BSCNN
bscnn = (a * b) // uscln

print("USCLN (a, b):", uscln)
print("BSCNN (a, b):", bscnn)
