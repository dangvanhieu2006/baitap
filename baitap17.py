import math
year = int(input("Nhap nam: "))
start = int(input("Nhap thu cho ngay dau tien cua nam: "))
month = int(input("Nhap thang: "))

# kiểm tra năm nhuận
def leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

days = [31,28,31,30,31,30,31,31,30,31,30,31]
if leap(year):
    days[1] = 29

# tính thứ của ngày đầu tháng
weekday = start
for i in range(month-1):
    weekday = (weekday + days[i]) % 7

names = ["A","B","C","D","E"]
idx = 0

print("\n Sun Mon Tue Wed Thu Fri Sat")

for i in range(weekday):
    print("    ", end="")

for d in range(1, days[month-1] + 1):

    if weekday == 0:
        print(f"{d:2} [ ]", end=" ")
    else:
        print(f"{d:2} [{names[idx]}]", end=" ")
        idx = (idx + 1) % 5

    weekday += 1
    if weekday == 7:
        weekday = 0
        print()
