import tkinter as tk
from tkinter import ttk


def tao_giao_dien(cua_so):
    cua_so.title("Listbox va Combobox")
    cua_so.geometry("360x380")
    cua_so.resizable(False, False)

    tk.Label(cua_so, text="Bai tap 3.1 - Chon mon hoc").pack(pady=(12, 4))
    listbox_mon_hoc = tk.Listbox(cua_so, height=5, exportselection=False)
    for mon_hoc in ("Toan", "Ly", "Hoa", "Van", "Anh"):
        listbox_mon_hoc.insert(tk.END, mon_hoc)
    listbox_mon_hoc.pack(pady=4)

    ket_qua_mon_hoc = tk.Label(cua_so, text="")
    ket_qua_mon_hoc.pack(pady=4)

    def xem_mon_da_chon():
        lua_chon = listbox_mon_hoc.curselection()
        if not lua_chon:
            ket_qua_mon_hoc.config(text="Vui long chon mot mon hoc.")
            return
        ket_qua_mon_hoc.config(
            text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}"
        )

    tk.Button(
        cua_so, text="Xem mon da chon", command=xem_mon_da_chon
    ).pack(pady=4)

    ttk.Separator(cua_so, orient="horizontal").pack(fill="x", padx=15, pady=10)

    tk.Label(cua_so, text="Bai tap 3.2 - Chon thanh pho").pack(pady=4)
    thanh_pho = ttk.Combobox(
        cua_so,
        values=("Ha Noi", "Da Nang", "TP.HCM", "Hue"),
        state="readonly",
    )
    thanh_pho.current(0)
    thanh_pho.pack(pady=4)

    ket_qua_thanh_pho = tk.Label(cua_so, text="")

    def xem_thanh_pho():
        ket_qua_thanh_pho.config(text=f"Ban chon: {thanh_pho.get()}")

    tk.Button(
        cua_so, text="Xac nhan", command=xem_thanh_pho
    ).pack(pady=4)
    ket_qua_thanh_pho.pack(pady=4)


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()
