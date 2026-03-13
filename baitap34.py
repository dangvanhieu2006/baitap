import math

# Hàm cần tích phân
def f(x):
    return (math.sin(x)**2) * math.cos(x)

a = 0
b = math.pi/2
eps = 1e-6
n = 1

# Hàm tính tích phân hình thang
def trapezoid(n):
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

I1 = trapezoid(n)

while True:
    n *= 2
    I2 = trapezoid(n)
    if abs(I2 - I1) < eps:
        break
    I1 = I2

print("Gia tri gan dung:", I2)
print("So doan chia:", n)

# Kiểm chứng kết quả chính xác
print("Gia tri dung:", 1/3)
