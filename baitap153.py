import tkinter as tk
from tkinter import messagebox

# Hàm đệ quy phụ: tính tổng và số lượng phần tử âm
def helper(arr, n):
    if n == 0:
        return (0, 0)  # (sum, count)

    s, c = helper(arr, n - 1)

    if arr[n - 1] < 0:
        return (s + arr[n - 1], c + 1)
    else:
        return (s, c)

# Hàm chính
def NegAverage(arr):
    s, c = helper(arr, len(arr))
    if c == 0:
        return 0
    return s / c

# Xử lý khi bấm nút
def xu_ly():
    try:
        arr = list(map(int, entry_arr.get().split()))
    except:
        messagebox.showerror("Lỗi", "Nhập mảng số nguyên cách nhau bằng khoảng trắng!")
        return

    kq = NegAverage(arr)

    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Trung bình các số âm: {kq}")

# GUI
root = tk.Tk()
root.title("Trung bình số âm (đệ quy)")
root.geometry("500x300")

tk.Label(root, text="Nhập mảng (cách nhau bằng khoảng trắng):").pack()
entry_arr = tk.Entry(root, width=50)
entry_arr.pack()

tk.Button(root, text="Tính trung bình", command=xu_ly).pack(pady=10)

text = tk.Text(root, height=5, width=50)
text.pack()

root.mainloop()
