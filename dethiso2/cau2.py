import tkinter as tk
from tkinter import messagebox

danh_sach_sach = []

def cap_nhat_listbox(ds_hien_thi):
    listbox_sach.delete(0, tk.END)
    for s in ds_hien_thi:
        dong = f"{s['MaSach']} - {s['TenSach']} - {int(s['Gia'])}d - SL: {s['SoLuong']}"
        listbox_sach.insert(tk.END, dong)

def xu_ly_them_sach():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia_str = entry_gia.get().strip()
    sl_str = entry_sl.get().strip()

    if not ma or not ten or not gia_str or not sl_str:
        messagebox.showerror("Input Error", "Please enter all book information!")
        return

    try:
        gia = float(gia_str)
        soluong = int(sl_str)
        if gia < 0 or soluong < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Price and Quantity must be valid numbers (>= 0)!")
        return

    sach_moi = {"MaSach": ma, "TenSach": ten, "Gia": gia, "SoLuong": soluong}
    danh_sach_sach.append(sach_moi)
    cap_nhat_listbox(danh_sach_sach)

    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_sl.delete(0, tk.END)

def xu_ly_tim_kiem():
    tu_khoa = entry_tim.get().strip().lower()
    if not tu_khoa:
        cap_nhat_listbox(danh_sach_sach)
        return
    
    ket_qua = [s for s in danh_sach_sach if tu_khoa in s["TenSach"].lower()]
    cap_nhat_listbox(ket_qua)

root = tk.Tk()
root.title("Quan ly sach thu vien")
root.geometry("500x450")

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Ma sach:").grid(row=0, column=0, sticky="w", pady=3)
entry_ma = tk.Entry(frame_form, width=35)
entry_ma.grid(row=0, column=1, pady=3)

tk.Label(frame_form, text="Ten sach:").grid(row=1, column=0, sticky="w", pady=3)
entry_ten = tk.Entry(frame_form, width=35)
entry_ten.grid(row=1, column=1, pady=3)

tk.Label(frame_form, text="Gia:").grid(row=2, column=0, sticky="w", pady=3)
entry_gia = tk.Entry(frame_form, width=35)
entry_gia.grid(row=2, column=1, pady=3)

tk.Label(frame_form, text="So luong:").grid(row=3, column=0, sticky="w", pady=3)
entry_sl = tk.Entry(frame_form, width=35)
entry_sl.grid(row=3, column=1, pady=3)

btn_them = tk.Button(frame_form, text="Them sach", command=xu_ly_them_sach, bg="#4CAF50", fg="white")
btn_them.grid(row=4, column=1, sticky="w", pady=8)

frame_tim = tk.Frame(root, padx=10, pady=5)
frame_tim.pack(fill="x")

tk.Label(frame_tim, text="Tim ten sach:").pack(side="left")
entry_tim = tk.Entry(frame_tim, width=25)
entry_tim.pack(side="left", padx=5)
btn_tim = tk.Button(frame_tim, text="Tim kiem", command=xu_ly_tim_kiem)
btn_tim.pack(side="left")

frame_ds = tk.Frame(root, padx=10, pady=10)
frame_ds.pack(fill="both", expand=True)

tk.Label(frame_ds, text="Danh sach sach:").pack(anchor="w")
listbox_sach = tk.Listbox(frame_ds, width=60, height=12)
listbox_sach.pack(fill="both", expand=True)

root.mainloop()