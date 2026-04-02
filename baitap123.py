import tkinter as tk
from tkinter import messagebox

# Hàm cộng nhị phân bằng chuỗi
def cong_nhi_phan(s1, s2):
    i = len(s1) - 1
    j = len(s2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry:
        bit1 = int(s1[i]) if i >= 0 else 0
        bit2 = int(s2[j]) if j >= 0 else 0

        tong = bit1 + bit2 + carry
        result = str(tong % 2) + result
        carry = tong // 2

        i -= 1
        j -= 1

    return result

# Xử lý khi bấm nút
def xu_ly():
    s1 = entry_s1.get().strip()
    s2 = entry_s2.get().strip()

    # kiểm tra hợp lệ
    if not all(c in '01' for c in s1) or not all(c in '01' for c in s2):
        messagebox.showerror("Lỗi", "Chỉ nhập số nhị phân (0,1)!")
        return

    kq = cong_nhi_phan(s1, s2)

    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Kết quả: {kq}")

# GUI
root = tk.Tk()
root.title("Cộng số nhị phân (chuỗi)")
root.geometry("500x300")

tk.Label(root, text="Số nhị phân 1:").pack()
entry_s1 = tk.Entry(root, width=40)
entry_s1.pack()

tk.Label(root, text="Số nhị phân 2:").pack()
entry_s2 = tk.Entry(root, width=40)
entry_s2.pack()

tk.Button(root, text="Cộng", command=xu_ly).pack(pady=10)

text = tk.Text(root, height=5, width=50)
text.pack()

root.mainloop()
