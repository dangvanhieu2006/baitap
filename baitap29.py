import math
print("Celsius   Fahrenheit")
for c in range(0, 11):
    f = c * 9/5 + 32
    print(f"{c:<8} {f:.2f}")

print()

print("Fahrenheit   Celsius")
for f in range(32, 43):
    c = 5 * (f - 32) / 9
    print(f"{f:<11} {c:.2f}")
