import tkinter as tk
from tkinter import ttk


def tao_giao_dien(cua_so):
    cua_so.title("Checkbutton va Radiobutton")
    cua_so.geometry("360x300")
    cua_so.resizable(False, False)

    cac_tab = ttk.Notebook(cua_so)
    tab_so_thich = ttk.Frame(cac_tab, padding=12)
    tab_tai_khoan = ttk.Frame(cac_tab, padding=12)
    cac_tab.add(tab_so_thich, text="So thich")
    cac_tab.add(tab_tai_khoan, text="Loai tai khoan")
    cac_tab.pack(fill="both", expand=True)

    doc_sach = tk.BooleanVar(value=False)
    the_thao = tk.BooleanVar(value=False)
    am_nhac = tk.BooleanVar(value=False)
    tk.Label(tab_so_thich, text="Chon so thich cua ban:").pack(
        anchor="w", pady=(0, 8)
    )
    for ten, bien in (
        ("Doc sach", doc_sach),
        ("The thao", the_thao),
        ("Am nhac", am_nhac),
    ):
        tk.Checkbutton(tab_so_thich, text=ten, variable=bien).pack(anchor="w")

    ket_qua_so_thich = tk.Label(tab_so_thich, text="", wraplength=310)
    ket_qua_so_thich.pack(anchor="w", pady=8)

    def xem_so_thich():
        da_chon = [
            ten
            for ten, bien in (
                ("Doc sach", doc_sach),
                ("The thao", the_thao),
                ("Am nhac", am_nhac),
            )
            if bien.get()
        ]
        ket_qua_so_thich.config(
            text="Ban da chon: " + (", ".join(da_chon) if da_chon else "Chua chon")
        )

    tk.Button(
        tab_so_thich, text="Xem lua chon", command=xem_so_thich
    ).pack(anchor="w", pady=4)

    loai_tai_khoan = tk.StringVar(value="Ca nhan")
    tk.Label(tab_tai_khoan, text="Chon loai tai khoan:").pack(
        anchor="w", pady=(0, 8)
    )
    for ten in ("Ca nhan", "Doanh nghiep"):
        tk.Radiobutton(
            tab_tai_khoan,
            text=ten,
            value=ten,
            variable=loai_tai_khoan,
        ).pack(anchor="w")

    ket_qua_tai_khoan = tk.Label(tab_tai_khoan, text="")

    def xem_tai_khoan():
        ket_qua_tai_khoan.config(text=f"Ban da chon: {loai_tai_khoan.get()}")

    tk.Button(
        tab_tai_khoan, text="Xac nhan", command=xem_tai_khoan
    ).pack(anchor="w", pady=8)
    ket_qua_tai_khoan.pack(anchor="w")


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()
