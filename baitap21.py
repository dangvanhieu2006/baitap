import math
diem_chuan = float(input("Nhap diem chuan: "))
a, b, c = map(float, input("Nhap diem 3 mon thi: ").split())
khu_vuc = input("Nhap khu vuc (A, B, C, X): ")
doi_tuong = int(input("Nhap doi tuong (1, 2, 3, 0): "))
if khu_vuc == "A":
    kv = 2
elif khu_vuc == "B":
    kv = 1
elif khu_vuc == "C":
    kv = 0.5
else:
    kv = 0
if doi_tuong == 1:
    dt = 2.5
elif doi_tuong == 2:
    dt = 1.5
elif doi_tuong == 3:
    dt = 1
else:
    dt = 0
tong = a + b + c + kv + dt
if a == 0 or b == 0 or c == 0:
    print("Rot [", tong, "]")
elif tong >= diem_chuan:
    print("Dau [", tong, "]")
else:
    print("Rot [", tong, "]")
