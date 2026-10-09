import tkinter as tk


cua_so = tk.Tk()
cua_so.title("Bo cuc bang place()")
cua_so.geometry("300x250")

tk.Label(cua_so, text="Ho ten:").place(x=20, y=20)
tk.Label(cua_so, text="Tuoi:").place(x=20, y=60)
tk.Label(cua_so, text="Email:").place(x=20, y=100)
tk.Button(cua_so, text="Dong y").place(x=40, y=160)
tk.Button(cua_so, text="Huy").place(x=150, y=160)

cua_so.mainloop()

# Tra loi: place() cho phep dat widget chinh xac theo toa do hoac ti le.
# Uu diem la kiem soat vi tri tu do; nhuoc diem la phai tu tinh toa do va
# can chinh lai khi kich thuoc cua so thay doi. pack()/grid() thuong thich
# ung voi thay doi kich thuoc tot hon; place() phu hop voi bo cuc co dinh.
