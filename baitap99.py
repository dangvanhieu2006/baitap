import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Xử lý ma trận")
root.geometry("600x500")

A = []
B = []
n = 0

# Tạo 2 ma trận
def tao_ma_tran():
    global A, B, n
    try:
        n = int(entry_n.get())
        A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        B = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

        text.delete(1.0, tk.END)

        text.insert(tk.END, "Ma trận A:\n")
        for row in A:
            text.insert(tk.END, " ".join(map(str, row)) + "\n")

        text.insert(tk.END, "\nMa trận B:\n")
        for row in B:
            text.insert(tk.END, " ".join(map(str, row)) + "\n")

    except:
        messagebox.showerror("Lỗi", "Nhập n hợp lệ!")

# Tính tổng ma trận
def tinh_tong():
    if not A or not B:
        messagebox.showwarning("Cảnh báo", "Chưa tạo ma trận!")
        return

    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

    text.insert(tk.END, "\nMa trận tổng A + B:\n")
    for row in C:
        text.insert(tk.END, " ".join(map(str, row)) + "\n")

# Tính tích ma trận
def tinh_tich():
    if not A or not B:
        messagebox.showwarning("Cảnh báo", "Chưa tạo ma trận!")
        return

    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    text.insert(tk.END, "\nMa trận tích A * B:\n")
    for row in C:
        text.insert(tk.END, " ".join(map(str, row)) + "\n")

# Giao diện
tk.Label(root, text="Nhập bậc n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo 2 ma trận", command=tao_ma_tran).pack(pady=5)
tk.Button(root, text="Tính tổng", command=tinh_tong).pack(pady=5)
tk.Button(root, text="Tính tích", command=tinh_tich).pack(pady=5)

text = tk.Text(root, width=70, height=20)
text.pack(pady=10)

root.mainloop()
