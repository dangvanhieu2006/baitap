import math
year = int(input("Nhap nam: "))

# kiểm tra năm nhuận
def leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

# số ngày từng tháng
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if leap(year):
    days[1] = 29

# tính thứ ngày 1/1 bằng công thức Zeller
d = 1
m = 13
y = year - 1

start = (d + y + y//4 - y//100 + y//400 + (31*m)//12) % 7

weekday = start

for month in range(1,13):

    print("\nThang", month)
    print("S  M  T  W  T  F  S")

    # khoảng trắng đầu tháng
    for i in range(weekday):
        print("   ", end="")

    for day in range(1, days[month-1] + 1):
        print(f"{day:2}", end=" ")

        weekday += 1
        if weekday == 7:
            weekday = 0
            print()

    if weekday != 0:
        print()
