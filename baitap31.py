print("Bang cuu chuong")

for i in range(1, 11):        # 1 → 10
    for j in range(2, 10):    # 2 → 9
        print(f"│{j}x{i:2}={j*i:2}", end="")
    print("│")
