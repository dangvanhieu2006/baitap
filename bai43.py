def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Nhập n
n = int(input("Nhập n (n < 40): "))

if n >= 40:
    print("Vui lòng nhập n < 40")
else:
    print(f"Fibonacci thứ {n} là: {fibonacci(n)}")
