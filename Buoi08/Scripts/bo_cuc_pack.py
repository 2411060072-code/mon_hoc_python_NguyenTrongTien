import tkinter as tk


cua_so = tk.Tk()
cua_so.title("Bo cuc bang pack()")
cua_so.geometry("300x250")

tk.Label(cua_so, text="Ho ten:").pack(pady=5)
tk.Label(cua_so, text="Tuoi:").pack(pady=5)
tk.Label(cua_so, text="Email:").pack(pady=5)
tk.Button(cua_so, text="Dong y").pack(side="left", padx=20, pady=15)
tk.Button(cua_so, text="Huy").pack(side="right", padx=20, pady=15)

cua_so.mainloop()

# Tra loi: pack() xep widget theo thu tu duoc goi; mac dinh tu tren xuong.
# Tham so side doi huong xep (TOP, BOTTOM, LEFT, RIGHT).
# padx va pady tao khoang cach theo chieu ngang va doc quanh widget.
#
# Frame la khung chua de gom cac widget lien quan. Gom widget vao Frame giup
# chia giao dien thanh cac khu vuc, sap xep va dieu chinh tung nhom de hon,
# thay vi dat tat ca truc tiep len cua so chinh.
