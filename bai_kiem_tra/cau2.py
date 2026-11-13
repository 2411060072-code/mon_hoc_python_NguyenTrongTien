# File: cau2.py
import tkinter as tk
from tkinter import messagebox
import cau1

class QuanLySanPham(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý sản phẩm")
        self.geometry("600x500")
        
        self.danh_sach = []
        
        frame_nhap = tk.Frame(self)
        frame_nhap.pack(pady=10)
        
        tk.Label(frame_nhap, text="Mã SP:").grid(row=0, column=0, sticky="w")
        self.entry_ma = tk.Entry(frame_nhap, width=30)
        self.entry_ma.grid(row=0, column=1, pady=5)
        
        tk.Label(frame_nhap, text="Tên SP:").grid(row=1, column=0, sticky="w")
        self.entry_ten = tk.Entry(frame_nhap, width=30)
        self.entry_ten.grid(row=1, column=1, pady=5)
        
        tk.Label(frame_nhap, text="Giá:").grid(row=2, column=0, sticky="w")
        self.entry_gia = tk.Entry(frame_nhap, width=30)
        self.entry_gia.grid(row=2, column=1, pady=5)
        
        tk.Label(frame_nhap, text="Số lượng:").grid(row=3, column=0, sticky="w")
        self.entry_sl = tk.Entry(frame_nhap, width=30)
        self.entry_sl.grid(row=3, column=1, pady=5)
        
        frame_nut = tk.Frame(self)
        frame_nut.pack(pady=10)
        
        tk.Button(frame_nut, text="Thêm sản phẩm", command=self.them_san_pham).grid(row=0, column=0, padx=5)
        tk.Button(frame_nut, text="Tìm kiếm", command=self.tim_kiem).grid(row=0, column=1, padx=5)
        
        self.listbox = tk.Listbox(self, width=80, height=15)
        self.listbox.pack(pady=10, padx=10, fill="both", expand=True)

    def hien_thi_danh_sach(self, danh_sach_hien_thi):
        self.listbox.delete(0, tk.END)
        for sp in danh_sach_hien_thi:
            chuoi = f"{sp['MaSP']} - {sp['TenSP']} - {sp['Gia']} - SL: {sp['SoLuong']}"
            self.listbox.insert(tk.END, chuoi)

    def them_san_pham(self):
        ma = self.entry_ma.get().strip()
        ten = self.entry_ten.get().strip()
        gia = self.entry_gia.get().strip()
        sl = self.entry_sl.get().strip()
        
        if not self.kiem_tra_du_lieu(show_error=True):
            return
            
        cau1.them_san_pham(self.danh_sach, ma, ten, float(gia), int(sl))
        
        self.hien_thi_danh_sach(self.danh_sach)
        
        self.entry_ma.delete(0, tk.END)
        self.entry_ten.delete(0, tk.END)
        self.entry_gia.delete(0, tk.END)
        self.entry_sl.delete(0, tk.END)

    def tim_kiem(self):
        tu_khoa = self.entry_ten.get().strip()
        if not tu_khoa:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập từ khóa vào ô Tên SP để tìm!")
            return
            
        kq = cau1.tim_kiem(self.danh_sach, tu_khoa)
        if not kq:
            messagebox.showinfo("Kết quả", "Không tìm thấy sản phẩm nào phù hợp.")
            self.listbox.delete(0, tk.END)
        else:
            self.hien_thi_danh_sach(kq)

    def kiem_tra_du_lieu(self, show_error=False):
        ma = self.entry_ma.get().strip()
        ten = self.entry_ten.get().strip()
        gia = self.entry_gia.get().strip()
        sl = self.entry_sl.get().strip()
        
        if not ma or not ten:
            if show_error: messagebox.showerror("Lỗi", "Mã SP và Tên SP không được để trống!")
            return False
            
        try:
            sl_int = int(sl)
            if sl_int < 0:
                if show_error: messagebox.showerror("Lỗi", "Số lượng không được là số âm!")
                return False
        except ValueError:
            if show_error: messagebox.showerror("Lỗi", "Số lượng phải là số nguyên!")
            return False
            
        try:
            float(gia)
        except ValueError:
            if show_error: messagebox.showerror("Lỗi", "Giá phải là số!")
            return False
            
        if show_error:
            messagebox.showinfo("Thành công", "Dữ liệu hợp lệ!")
        return True

if __name__ == "__main__":
    app = QuanLySanPham()
    app.mainloop()