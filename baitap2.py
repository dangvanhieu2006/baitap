import math

xA, yA = map(float, input("A(xA, yA): ").split())
xB, yB = map(float, input("B(xB, yB): ").split())

AB = ((xB - xA)**2 + (yB - yA)**2) ** 0.5

print("|AB| =", round(AB, 4))
