import itertools

ops = ['+', '-', '*', '/']

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return None
        return a / b

for comb in itertools.product(ops, repeat=5):
    try:
        res = calculate(1, 2, comb[0])
        res = calculate(res, 3, comb[1])
        res = calculate(res, 4, comb[2])
        res = calculate(res, 5, comb[3])
        res = calculate(res, 6, comb[4])
        
        if res is not None and abs(res - 36) < 1e-6:
            print("Tìm được:")
            print(f"((((1 {comb[0]} 2) {comb[1]} 3) {comb[2]} 4) {comb[3]} 5) {comb[4]} 6 = 36")
    except:
        continue
