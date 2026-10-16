import tkinter as tk


def tao_giao_dien(cua_so):
    cua_so.title("Vi du Scale")
    cua_so.geometry("360x180")
    cua_so.resizable(False, False)

    nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0")
    nhan_gia_tri.pack(pady=(20, 8))

    def cap_nhat_gia_tri(gia_tri):
        nhan_gia_tri.config(text=f"Gia tri hien tai: {int(float(gia_tri))}")

    thanh_truot = tk.Scale(
        cua_so,
        from_=0,
        to=100,
        orient="horizontal",
        command=cap_nhat_gia_tri,
    )
    thanh_truot.pack(padx=20, fill="x")


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()
