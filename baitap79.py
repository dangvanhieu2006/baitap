import tkinter as tk
from tkinter import messagebox
import random

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Xử lý mảng")
root.geometry("500x400")

arr = []

# Hàm tạo mảng
def tao_mang():
    global arr
    try:
        n = int(entry_n.get())
        arr = [random.randint(-100, 100) for _ in range(n)]
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Mảng:\n" + " ".join(map(str, arr)))
    except:
        messagebox.showerror("Lỗi", "Nhập n hợp lệ!")

# Hàm tìm phần tử gần x nhất
def tim_gan_nhat():
    try:
        x = int(entry_x.get())
        if not arr:
            messagebox.showwarning("Cảnh báo", "Chưa có mảng!")
            return
        
        closest = arr[0]
        min_diff = abs(arr[0] - x)

        for num in arr:
            if abs(num - x) < min_diff:
                min_diff = abs(num - x)
                closest = num

        text.insert(tk.END, f"\nGần {x} nhất: {closest}")
    except:
        messagebox.showerror("Lỗi", "Nhập x hợp lệ!")

# Hàm chèn số 1 sau số âm
def chen_so_1():
    global arr
    if not arr:
        messagebox.showwarning("Cảnh báo", "Chưa có mảng!")
        return

    new_arr = []
    for num in arr:
        new_arr.append(num)
        if num < 0:
            new_arr.append(1)

    text.insert(tk.END, "\nMảng sau khi chèn:\n" + " ".join(map(str, new_arr)))

# Giao diện
tk.Label(root, text="Nhập n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo mảng", command=tao_mang).pack(pady=5)

tk.Label(root, text="Nhập x:").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Button(root, text="Tìm gần nhất", command=tim_gan_nhat).pack(pady=5)
tk.Button(root, text="Chèn số 1 sau số âm", command=chen_so_1).pack(pady=5)

text = tk.Text(root, height=10, width=50)
text.pack(pady=10)

root.mainloop()
