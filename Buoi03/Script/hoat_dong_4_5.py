import math

#hd 4.1
toa_do = (3, 5)
print(toa_do, type(toa_do))
# Thu gan lai: toa_do[0] = 10 -> quan sat loi TypeError (tuple bat bien)

#hd 4.2
x, y = toa_do
print("x =", x, "- y =", y)
# Doi gia tri 2 bien bang unpacking (khong can bien tam)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

#hd 4.3
c, d = 17, 5
thuong_du = divmod(c, d) # divmod tra ve mot tuple (thuong, du)
thuong, du = thuong_du # unpacking ket qua
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

#hd 5
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

#Yêu cầu: tạo thêm danh sách cac_diem = [(0,0), (3,4), (6,8)] (list chứa các tuple tọa độ), dùng for để in ra khoảng cách của từng điểm so với gốc tọa độ (0, 0).
cac_diem = [(0,0), (3,4), (6,8)]
for x, y in cac_diem:
    khoang_cach = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu {(x, y)} den (0,0) la: {round(khoang_cach, 2)}")