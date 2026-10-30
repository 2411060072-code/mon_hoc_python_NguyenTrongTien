import numpy as np
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5] # list Python thuan
diem_array = np.array(diem_list) # chuyen sang mang NumPy (ndarray)
print(type(diem_list), type(diem_array))
# Phep toan vector hoa: cong truc tiep 0.5 vao TOAN BO mang, khong can vong lap
diem_cong_them = diem_array + 0.5
print(diem_cong_them)
# So sanh voi cach lam bang list thuan (Buoi 3) - can dung list comprehension/vong lap
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)
print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)

# --- GIẢI THÍCH ---
# diem_array + 0.5 chạy được: Vì đây là mảng NumPy, nó hỗ trợ tính năng Vector hóa (Broadcasting).
# NumPy tự hiểu phép + là cộng 0.5 vào TỪNG phần tử trong mảng mà không cần vòng lặp.
#
# diem_list + 0.5 báo lỗi: Vì đây là List thông thường của Python. Với List, dấu + là phép NỐI (Concatenation).
# Python không hiểu việc nối một list với một số thực (float) nên báo lỗi TypeError.
# Muốn cộng từng phần tử cho List, bắt buộc phải dùng vòng lặp hoặc List Comprehension.