import ast
import operator
import tkinter as tk
from tkinter import messagebox


_PHEP_TOAN = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def tinh_bieu_thuc(bieu_thuc):
    """Tinh bieu thuc so hoc chi voi +, -, *, / va khong dung eval()."""
    cay = ast.parse(bieu_thuc, mode="eval")

    def tinh_nut(nut):
        if isinstance(nut, ast.Expression):
            return tinh_nut(nut.body)
        if isinstance(nut, ast.Constant) and type(nut.value) in (int, float):
            return nut.value
        if isinstance(nut, ast.UnaryOp) and isinstance(
            nut.op, (ast.UAdd, ast.USub)
        ):
            gia_tri = tinh_nut(nut.operand)
            return gia_tri if isinstance(nut.op, ast.UAdd) else -gia_tri
        if isinstance(nut, ast.BinOp) and type(nut.op) in _PHEP_TOAN:
            return _PHEP_TOAN[type(nut.op)](
                tinh_nut(nut.left), tinh_nut(nut.right)
            )
        raise ValueError("Bieu thuc chi ho tro so va cac phep +, -, *, /.")

    return tinh_nut(cay)


def tao_giao_dien(cua_so):
    cua_so.title("May tinh bo tui")
    cua_so.geometry("300x390")
    cua_so.resizable(False, False)

    bien_hien_thi = tk.StringVar()
    o_hien_thi = tk.Entry(
        cua_so,
        textvariable=bien_hien_thi,
        justify="right",
        font=("Arial", 20),
        state="readonly",
        readonlybackground="white",
    )
    o_hien_thi.grid(
        row=0, column=0, columnspan=4, padx=10, pady=12, sticky="nsew"
    )

    def them_vao_bieu_thuc(ky_tu):
        bien_hien_thi.set(bien_hien_thi.get() + ky_tu)

    def xoa():
        bien_hien_thi.set("")

    def xoa_ky_tu_cuoi():
        bien_hien_thi.set(bien_hien_thi.get()[:-1])

    def tinh():
        bieu_thuc = bien_hien_thi.get().strip()
        if not bieu_thuc:
            return
        try:
            ket_qua = tinh_bieu_thuc(bieu_thuc)
        except (SyntaxError, ValueError, ZeroDivisionError):
            messagebox.showerror("Loi", "Bieu thuc khong hop le.")
            return
        bien_hien_thi.set(str(ket_qua))

    cac_nut = (
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    )
    for ky_tu, hang, cot in cac_nut:
        lenh = tinh if ky_tu == "=" else lambda k=ky_tu: them_vao_bieu_thuc(k)
        tk.Button(
            cua_so,
            text=ky_tu,
            font=("Arial", 14),
            command=lenh,
        ).grid(row=hang, column=cot, padx=4, pady=4, sticky="nsew")

    tk.Button(cua_so, text="C", command=xoa).grid(
        row=5, column=0, columnspan=2, padx=4, pady=4, sticky="nsew"
    )
    tk.Button(cua_so, text="Xoa ky tu", command=xoa_ky_tu_cuoi).grid(
        row=5, column=2, columnspan=2, padx=4, pady=4, sticky="nsew"
    )

    for cot in range(4):
        cua_so.grid_columnconfigure(cot, weight=1)
    for hang in range(1, 6):
        cua_so.grid_rowconfigure(hang, weight=1)


if __name__ == "__main__":
    cua_so = tk.Tk()
    tao_giao_dien(cua_so)
    cua_so.mainloop()
