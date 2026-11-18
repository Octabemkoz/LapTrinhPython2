import pandas as pd
import matplotlib.pyplot as plt

noi_dung_csv = """MaSach,TenSach,Gia,SoLuong
S001,Lap trinh Python co ban,95000,40
S002,Cau truc du lieu va giai thuat,120000,6
S003,Nhap mon tri tue nhan tao,150000,25
S004,Co so du lieu nang cao,135000,4
S005,Tieng Anh chuyen nganh CNTT,70000,80"""

with open("sach.csv", "w", encoding="utf-8") as f:
    f.write(noi_dung_csv)

# a) Read CSV file
df = pd.read_csv("sach.csv")
print("--- Data ---")
print(df)

# b) Calculate statistics
tong_dau_sach = len(df)
gia_trung_binh = df["Gia"].mean()
sach_gia_cao_nhat = df.loc[df["Gia"].idxmax(), "TenSach"]

print("\n--- Statistics ---")
print(f"Total book titles: {tong_dau_sach}")
print(f"Average price: {gia_trung_binh:,.0f}")
print(f"Highest priced book: {sach_gia_cao_nhat}")

# c) Plot bar chart and save as bieudo.png
plt.figure(figsize=(10, 6))
plt.bar(df["TenSach"], df["SoLuong"], color="skyblue", edgecolor="black")
plt.title("Stock Quantity by Book")
plt.xlabel("TenSach")
plt.ylabel("SoLuong")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig("bieudo.png")
plt.close()
print("\nSaved chart to bieudo.png")

# d) Filter books with SoLuong < 10 and export to canh_bao_sach.csv
sach_sap_het = df[df["SoLuong"] < 10]
sach_sap_het.to_csv("canh_bao_sach.csv", index=False, encoding="utf-8")
print("Exported low stock books to canh_bao_sach.csv")