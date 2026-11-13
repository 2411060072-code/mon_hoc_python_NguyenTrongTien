import csv
import matplotlib.pyplot as plt

def doc_file_csv(ten_file):
    danh_sach = []
    try:
        with open(ten_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sp = {
                    "MaSP": row["MaSP"],
                    "TenSP": row["TenSP"],
                    "Gia": float(row["Gia"]),
                    "SoLuong": int(row["SoLuong"])
                }
                danh_sach.append(sp)
    except FileNotFoundError:
        print(f"Không tìm thấy file {ten_file}")
    return danh_sach

def thong_ke(danh_sach):
    if not danh_sach:
        print("Danh sách trống.")
        return
        
    tong_sp = len(danh_sach)
    tong_gia = sum(sp["Gia"] for sp in danh_sach)
    gia_tb = tong_gia / tong_sp
    
    sp_cao_nhat = max(danh_sach, key=lambda x: x["Gia"])
    
    print(f"Tổng số sản phẩm: {tong_sp}")
    print(f"Giá trung bình: {gia_tb:,.2f}")
    print(f"Sản phẩm giá cao nhất: {sp_cao_nhat['TenSP']} (Giá: {sp_cao_nhat['Gia']})")

def ve_bieu_do(danh_sach):
    if not danh_sach:
        return
    ten_sp = [sp["TenSP"] for sp in danh_sach]
    so_luong = [sp["SoLuong"] for sp in danh_sach]
    
    plt.figure(figsize=(8, 5))
    plt.bar(ten_sp, so_luong, color="skyblue")
    plt.title("Số lượng tồn kho theo từng sản phẩm")
    plt.xlabel("Tên sản phẩm")
    plt.ylabel("Số lượng")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("bieu_do_ton_kho.png")
    plt.show()

def xuat_file_canh_bao(danh_sach):
    sap_het = [sp for sp in danh_sach if sp["SoLuong"] < 10]
    
    if not sap_het:
        print("Không có sản phẩm nào sắp hết hàng.")
        return
        
    with open("canh_bao_hang.csv", mode='w', encoding='utf-8', newline='') as f:
        fieldnames = ["MaSP", "TenSP", "Gia", "SoLuong"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sap_het)
    print("Đã xuất file canh_bao_hang.csv")

if __name__ == "__main__":
    ds = doc_file_csv("sanpham.csv")
    print("--- THỐNG KÊ ---")
    thong_ke(ds)
    print("\n--- XUẤT FILE CẢNH BÁO ---")
    xuat_file_canh_bao(ds)
    print("\n--- VẼ BIỂU ĐỒ ---")
    ve_bieu_do(ds)