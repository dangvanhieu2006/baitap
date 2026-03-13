n = int(input("Nhap so tien (nghin dong): "))

min_notes = 10**9
best_a = best_b = best_c = 0

for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            
            if a + 2*b + 5*c == n:
                total = a + b + c
                
                if b > total/2 and total < min_notes:
                    min_notes = total
                    best_a = a
                    best_b = b
                    best_c = c

print("Phuong an doi tien:")
print("1000:", best_a)
print("2000:", best_b)
print("5000:", best_c)
print("Tong so to:", min_notes)
