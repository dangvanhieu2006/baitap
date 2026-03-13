import math
kw = int(input("Nhap so kW tieu thu: "))

tien = 0

if kw <= 100:
    tien = kw * 500

elif kw <= 250:
    tien = 100 * 500 + (kw - 100) * 800

elif kw <= 350:
    tien = 100 * 500 + 150 * 800 + (kw - 250) * 1000

else:
    tien = 100 * 500 + 150 * 800 + 100 * 1000 + (kw - 350) * 1500

print("Chi phi:", tien)
