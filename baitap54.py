import tkinter as tk

# Tạo cửa sổ
root = tk.Tk()
root.title("Bảng Cửu Chương")

# Tạo khung chứa nội dung
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Hàm tạo bảng cửu chương
def tao_bang():
    text.delete("1.0", tk.END)  # Xóa nội dung cũ
    
    for i in range(2, 10):
        text.insert(tk.END, f"Bảng {i}:\n")
        for j in range(1, 11):
            text.insert(tk.END, f"{i} x {j} = {i*j}\n")
        text.insert(tk.END, "\n")

# Ô hiển thị
text = tk.Text(frame, width=30, height=25, font=("Arial", 12))
text.pack()

# Nút bấm
btn = tk.Button(frame, text="Hiển thị bảng cửu chương", command=tao_bang)
btn.pack(pady=10)

# Chạy chương trình
root.mainloop()
