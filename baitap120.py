import tkinter as tk
from tkinter import messagebox

# Hàm chèn chuỗi
def chen_chuoi():
    s1 = entry_s1.get()
    s2 = entry_s2.get()

    # kiểm tra độ dài
    if len(s1) > 80 or len(s2) > 80:
        messagebox.showerror("Lỗi", "Chuỗi tối đa 80 ký tự!")
        return

    try:
        k = int(entry_k.get())
    except:
        messagebox.showerror("Lỗi", "k phải là số nguyên!")
        return

    if k < 0 or k > len(s1):
        messagebox.showerror("Lỗi", "0 ≤ k ≤ độ dài chuỗi 1!")
        return

    # chèn chuỗi
    result = s1[:k] + s2 + s1[k:]

    text.delete(1.0, tk.END)
    text.insert(tk.END, "Kết quả:\n" + result)

# Tạo giao diện
root = tk.Tk()
root.title("Chèn chuỗi")
root.geometry("500x350")

tk.Label(root, text="Chuỗi 1:").pack()
entry_s1 = tk.Entry(root, width=50)
entry_s1.pack()

tk.Label(root, text="Chuỗi 2:").pack()
entry_s2 = tk.Entry(root, width=50)
entry_s2.pack()

tk.Label(root, text="Vị trí k:").pack()
entry_k = tk.Entry(root)
entry_k.pack()

tk.Button(root, text="Chèn chuỗi", command=chen_chuoi).pack(pady=10)

text = tk.Text(root, height=8, width=60)
text.pack()

root.mainloop()
