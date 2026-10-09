import tkinter as tk


def khi_go_phim(event):
    ky_tu = event.char if event.char.isprintable() else event.keysym
    nhan_thong_bao.config(text=f"Ban vua nhan phim: {ky_tu}")


def khi_click_chuot(event):
    nhan_thong_bao.config(
        text=f"Ban vua click tai toa do: ({event.x}, {event.y})"
    )


cua_so = tk.Tk()
cua_so.title("Vi du bind()")
cua_so.geometry("400x250")

nhan_thong_bao = tk.Label(
    cua_so,
    text="Hay go phim hoac click chuot",
    font=("Arial", 12),
)
nhan_thong_bao.pack(pady=30)

cua_so.bind("<Key>", khi_go_phim)
cua_so.bind("<Button-1>", khi_click_chuot)
cua_so.focus_set()

cua_so.mainloop()

# Tra loi: command gan mot ham callback cho widget (thuong la Button) va
# goi ham do khi kich hoat widget; command khong nhan doi tuong Event.
# bind() gan ham xu ly vao mot loai su kien, co the ap dung cho nhieu widget
# hoac cua so chinh; ham xu ly nhan Event de doc phim, toa do chuot, ...
