import tkinter as tk
from tkinter import messagebox


def tao_giao_dien(cua_so):
    danh_sach_cong_viec = []

    cua_so.title("Ung dung Ghi chu cong viec")
    cua_so.geometry("440x410")
    cua_so.resizable(False, False)

    tk.Label(
        cua_so, text="TO-DO LIST", font=("Arial", 16, "bold")
    ).grid(row=0, column=0, columnspan=3, pady=10)

    bien_cong_viec_moi = tk.StringVar()
    entry_cong_viec = tk.Entry(
        cua_so, textvariable=bien_cong_viec_moi, width=36
    )
    entry_cong_viec.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    listbox_cong_viec = tk.Listbox(
        cua_so, width=52, height=13, exportselection=False
    )
    listbox_cong_viec.grid(
        row=2, column=0, columnspan=3, padx=10, pady=10
    )

    def lam_moi_listbox():
        listbox_cong_viec.delete(0, tk.END)
        for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
            tien_to = "[Da xong] " if da_hoan_thanh else "[Chua xong] "
            listbox_cong_viec.insert(tk.END, tien_to + noi_dung)

    def them_cong_viec():
        noi_dung = bien_cong_viec_moi.get().strip()
        if not noi_dung:
            messagebox.showerror(
                "Loi", "Vui long nhap noi dung cong viec truoc khi them."
            )
            entry_cong_viec.focus_set()
            return

        danh_sach_cong_viec.append((noi_dung, False))
        bien_cong_viec_moi.set("")
        lam_moi_listbox()
        entry_cong_viec.focus_set()

    def lay_vi_tri_da_chon(thong_bao):
        lua_chon = listbox_cong_viec.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", thong_bao)
            return None
        return lua_chon[0]

    def xoa_cong_viec():
        vi_tri = lay_vi_tri_da_chon(
            "Vui long chon mot cong viec trong danh sach de xoa."
        )
        if vi_tri is None:
            return
        danh_sach_cong_viec.pop(vi_tri)
        lam_moi_listbox()

    def danh_dau_hoan_thanh():
        vi_tri = lay_vi_tri_da_chon(
            "Vui long chon mot cong viec de danh dau hoan thanh."
        )
        if vi_tri is None:
            return
        noi_dung, _ = danh_sach_cong_viec[vi_tri]
        danh_sach_cong_viec[vi_tri] = (noi_dung, True)
        lam_moi_listbox()
        listbox_cong_viec.selection_set(vi_tri)

    tk.Button(
        cua_so, text="Them", command=them_cong_viec
    ).grid(row=1, column=2, padx=10, pady=5)
    tk.Button(
        cua_so, text="Danh dau hoan thanh", command=danh_dau_hoan_thanh
    ).grid(row=3, column=0, padx=8, pady=5)
    tk.Button(
        cua_so, text="Xoa cong viec", command=xoa_cong_viec
    ).grid(row=3, column=1, padx=8, pady=5)

    def them_khi_nhan_enter(event):
        if event.keysym == "Return":
            them_cong_viec()

    entry_cong_viec.bind("<Return>", them_khi_nhan_enter)


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()
