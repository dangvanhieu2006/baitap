print("Bo ba Pythagorean < 100:")

for a in range(1, 100):
    
    # 3 số liên tiếp
    b = a + 1
    c = a + 2
    
    if c < 100 and a*a + b*b == c*c:
        print(a, b, c)
    
    # 3 số chẵn liên tiếp
    b = a + 2
    c = a + 4
    
    if c < 100 and a*a + b*b == c*c:
        print(a, b, c)
