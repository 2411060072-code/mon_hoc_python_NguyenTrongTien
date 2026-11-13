def them_san_pham(danh_sach, ma, ten, gia, so_luong):
    san_pham = {
        "MaSP": ma,
        "TenSP": ten,
        "Gia": float(gia),
        "SoLuong": int(so_luong)
    }
    danh_sach.append(san_pham)
    return danh_sach

def tim_kiem(danh_sach, tu_khoa):
    tu_khoa_lower = tu_khoa.lower()
    ket_qua = []
    for sp in danh_sach:
        if tu_khoa_lower in sp["TenSP"].lower():
            ket_qua.append(sp)
    return ket_qua

def tong_gia_tri_kho(danh_sach):
    tong = 0
    for sp in danh_sach:
        tong += sp["Gia"] * sp["SoLuong"]
    return tong

def menu_chinh(danh_sach):
    while True:
        print("\n--- QUẢN LÝ SẢN PHẨM ---")
        print("1. Thêm sản phẩm")
        print("2. Tìm kiếm sản phẩm")
        print("3. Xem tổng giá trị kho")
        print("4. Thoát")
        lua_chon = input("Nhập lựa chọn: ")
        
        if lua_chon == "1":
            ma = input("Nhập Mã SP: ")
            ten = input("Nhập Tên SP: ")
            gia = float(input("Nhập Giá: "))
            sl = int(input("Nhập Số lượng: "))
            them_san_pham(danh_sach, ma, ten, gia, sl)
            print("Đã thêm!")
            
        elif lua_chon == "2":
            tk = input("Nhập từ khóa tìm kiếm: ")
            kq = tim_kiem(danh_sach, tk)
            if not kq:
                print("Không tìm thấy sản phẩm nào.")
            else:
                print("Kết quả tìm kiếm:")
                for sp in kq:
                    print(f"  {sp['MaSP']} - {sp['TenSP']} - {sp['Gia']} - SL: {sp['SoLuong']}")
                    
        elif lua_chon == "3":
            tong = tong_gia_tri_kho(danh_sach)
            print(f"Tổng giá trị kho: {tong:,.0f} VNĐ")
            
        elif lua_chon == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    kho = []
    menu_chinh(kho)