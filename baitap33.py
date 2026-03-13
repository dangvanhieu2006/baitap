print("So Armstrong co 3 chu so:")
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    
    if a**3 + b**3 + c**3 == i:
        print(i)

print("So Armstrong co 4 chu so:")
for i in range(1000, 10000):
    a = i // 1000
    b = (i // 100) % 10
    c = (i // 10) % 10
    d = i % 10
    
    if a**4 + b**4 + c**4 + d**4 == i:
        print(i)
