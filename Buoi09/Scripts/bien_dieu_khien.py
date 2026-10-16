import tkinter as tk


def tao_giao_dien(cua_so):
    cua_so.title("Vi du bien dieu khien")
    cua_so.geometry("380x230")
    cua_so.resizable(False, False)

    bien_ho_ten = tk.StringVar(value="Nguyen Van A")
    bien_tuoi = tk.IntVar(value=18)
    bien_dong_y = tk.BooleanVar(value=False)

    tk.Label(cua_so, text="Ho ten:").grid(
        row=0, column=0, padx=10, pady=10, sticky="w"
    )
    tk.Entry(cua_so, textvariable=bien_ho_ten, width=25).grid(
        row=0, column=1, padx=10, pady=10
    )

    tk.Label(cua_so, text="Tuoi:").grid(
        row=1, column=0, padx=10, pady=10, sticky="w"
    )
    tk.Entry(cua_so, textvariable=bien_tuoi, width=25).grid(
        row=1, column=1, padx=10, pady=10
    )

    tk.Checkbutton(
        cua_so,
        text="Dong y dieu khoan",
        variable=bien_dong_y,
    ).grid(row=2, column=0, columnspan=2, pady=5)

    ket_qua = tk.Label(cua_so, text="", justify="left")
    ket_qua.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def xem_gia_tri():
        ket_qua.config(
            text=(
                f"Ho ten: {bien_ho_ten.get()}\n"
                f"Tuoi: {bien_tuoi.get()}\n"
                f"Dong y dieu khoan: {bien_dong_y.get()}"
            )
        )
        bien_tuoi.set(bien_tuoi.get() + 1)

    tk.Button(
        cua_so, text="Xem gia tri (va +1 tuoi)", command=xem_gia_tri
    ).grid(row=3, column=0, columnspan=2, pady=5)


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()

# textvariable tao lien ket hai chieu giua Entry va bien Tkinter: .get() doc
# gia tri moi nhat, con .set() co the cap nhat Entry. Entry.get() chi doc truc
# tiep mot widget, khong tien neu can chia se hoac cap nhat gia tri qua bien.
