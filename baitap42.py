# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo danh sách số nguyên tố < 1000
primes = [i for i in range(2, 1000) if is_prime(i)]

# Kiểm chứng giả thuyết
def check_goldbach_odd(limit=1000):
    for n in range(7, limit, 2):  # chỉ xét số lẻ > 5
        found = False
        
        for p1 in primes:
            if p1 > n:
                break
            for p2 in primes:
                if p1 + p2 > n:
                    break
                p3 = n - p1 - p2
                if p3 in primes:
                    print(f"{n} = {p1} + {p2} + {p3}")
                    found = True
                    break
            if found:
                break
        
        if not found:
            print(f"❌ Không biểu diễn được: {n}")
            return
    
    print("✅ Tất cả số lẻ < 1000 đều thỏa mãn!")

# Chạy
check_goldbach_odd()
