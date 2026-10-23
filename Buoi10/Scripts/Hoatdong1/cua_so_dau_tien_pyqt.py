import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cua so PyQt dau tien")
        self.resize(300, 200)
        layout = QVBoxLayout()
        nhan = QLabel("Xin chao PyQt!")
        layout.addWidget(nhan)
        self.setLayout(layout)
app = QApplication(sys.argv)
cua_so = CuaSoDauTien()
cua_so.show()
sys.exit(app.exec_())

# =====================================================================
# TRẢ LỜI CÂU HỎI:
# So sánh cấu trúc với Tkinter (cua_so = tk.Tk() + mainloop()):
#
# - app = QApplication(sys.argv)  tương đương  root = tk.Tk() (khởi tạo app)
# - cua_so.show()                 tương đương  việc hiển thị cửa sổ lên màn hình
# - app.exec_()                   tương đương  root.mainloop()
#
# => app.exec_() và mainloop() đều là VÒNG LẶP SỰ KIỆN (Event Loop).
#    Nó giữ cho cửa sổ luôn hiển thị và liên tục lắng nghe các thao tác
#    của người dùng (click chuột, gõ phím, đóng cửa sổ...). Chương trình
#    sẽ dừng tại đây cho đến khi bạn tắt cửa sổ. Nếu thiếu lệnh này,
#    cửa sổ sẽ vụt tắt ngay sau khi hiện ra.
# =====================================================================