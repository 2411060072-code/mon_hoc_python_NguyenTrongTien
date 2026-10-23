import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du Signal - Slot")
        self.resize(300, 180)

        self.o_nhap = QLineEdit()
        nut_hien_thi = QPushButton("Hien thi noi dung")
        self.nhan_ket_qua = QLabel("Chua co noi dung")

        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        # 1 signal nối nhiều slot
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)
        nut_hien_thi.clicked.connect(self.in_ra_man_hinh) # Dòng thêm cho bài 3.2

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Ban vua nhap: {noi_dung}")

    def in_ra_man_hinh(self): # Hàm thêm cho bài 3.2
        print("Nut vua duoc bam!")

app = QApplication(sys.argv)
cua_so = ViDuSignalSlot()
cua_so.show()
sys.exit(app.exec_())


# =====================================================================
# TRẢ LỜI CÂU HỎI (Phần in vàng):
#
# - Signal: Là tín hiệu được phát ra khi có một sự kiện xảy ra (ví dụ: 
#   nút bị click). Trong code là "clicked".
# - Slot: Là hàm nhận tín hiệu đó để xử lý (ví dụ: hàm hiển thị nội dung).
# - Hàm connect(): Dùng để "nối" Signal với Slot lại với nhau.
#
# * So sánh với Tkinter (command=ten_ham):
#   - Trong Tkinter: Dùng tham số command=ten_ham để gắn trực tiếp một hàm 
#     vào nút. Cách này đơn giản hơn nhưng ít linh hoạt.
#   - Trong PyQt5: Dùng nut.clicked.connect(ham). Linh hoạt hơn rất nhiều vì 
#     một tín hiệu (signal) có thể nối tới nhiều hàm (slot), và ngược lại.
#
# =====================================================================