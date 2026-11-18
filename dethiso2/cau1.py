def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": gia,
        "SoLuong": soluong
    }
    danh_sach.append(sach)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    tu_khoa_lower = tu_khoa.lower()
    for sach in danh_sach:
        if tu_khoa_lower in sach["TenSach"].lower():
            ket_qua.append(sach)
    return ket_qua

def tong_gia_tri_kho_sach(danh_sach):
    tong = 0
    for sach in danh_sach:
        tong += sach["Gia"] * sach["SoLuong"]
    return tong

def hien_thi_danh_sach(danh_sach):
    if not danh_sach:
        print("Empty list.")
        return
    for s in danh_sach:
        print(f"{s['MaSach']} - {s['TenSach']} - Gia: {s['Gia']} - SL: {s['SoLuong']}")

def main():
    danh_sach_sach = [
        {"MaSach": "S001", "TenSach": "Lap trinh Python co ban", "Gia": 95000, "SoLuong": 40},
        {"MaSach": "S002", "TenSach": "Cau truc du lieu va giai thuat", "Gia": 120000, "SoLuong": 6},
        {"MaSach": "S003", "TenSach": "Nhap mon tri tue nhan tao", "Gia": 150000, "SoLuong": 25},
        {"MaSach": "QB 36-36", "TenSach": "BienDo", "Gia": 1000000, "SoLuong": 1}
    ]

    while True:
        print("\n--- QUAN LY SACH THU VIEN ---")
        print("1. Them sach")
        print("2. Tim kiem theo ten")
        print("3. Xem tong gia tri kho sach")
        print("4. Thoat chuong trinh")
        
        chon = input("Chon chuc nang (1-4): ")
        
        if chon == "1":
            ma = input("Nhap ma sach: ")
            ten = input("Nhap ten sach: ")
            gia = float(input("Nhap gia sach: "))
            soluong = int(input("Nhap so luong: "))
            them_sach(danh_sach_sach, ma, ten, gia, soluong)
            print("Da them sach thanh cong!")
            
        elif chon == "2":
            tu_khoa = input("Nhap tu khoa ten sach can tim: ")
            kq = tim_kiem_theo_ten(danh_sach_sach, tu_khoa)
            print("Ket qua tim kiem:")
            hien_thi_danh_sach(kq)
            
        elif chon == "3":
            tong = tong_gia_tri_kho_sach(danh_sach_sach)
            print(f"Tong gia tri kho sach: {tong:,.0f}")
            
        elif chon == "4":
            print("Da thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai!")

if __name__ == "__main__":
    main()