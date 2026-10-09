import tkinter as tk


cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("400x300")
cua_so.resizable(False, False)

nhan_chao = tk.Label(
    cua_so,
    text="Xin chao Tkinter!",
    font=("Arial", 16),
)
nhan_chao.pack(pady=20)

cua_so.mainloop()
