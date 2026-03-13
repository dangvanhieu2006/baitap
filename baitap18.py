import math
gio = int(input("Nhap so gio: "))

tuan = gio // 168
gio_du = gio % 168

ngay = gio_du // 24
gio_con = gio_du % 24

print(tuan, "tuan,", ngay, "ngay,", gio_con, "gio")
