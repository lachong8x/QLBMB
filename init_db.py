import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    don_vi_quan_ly TEXT,
    vi_tri TEXT,
    trang_thai TEXT CHECK(trang_thai IN ('Hoạt động tốt', 'Sự cố')),
    ngay_phat_hien_su_co TEXT,
    tien_do_khac_phuc TEXT,
    ghi_chu TEXT,
    ngay_ket_thuc_su_co TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER,
    trang_thai TEXT,
    thoi_gian TEXT,
    FOREIGN KEY(device_id) REFERENCES devices(id)
)
''')

cursor.execute("DELETE FROM devices")

cursor.execute("INSERT INTO devices (name, don_vi_quan_ly, vi_tri, trang_thai) VALUES ('Thiết bị A', 'Phòng CNTT', 'Tầng 1', 'Hoạt động tốt')")
cursor.execute("INSERT INTO devices (name, don_vi_quan_ly, vi_tri, trang_thai, ngay_phat_hien_su_co, tien_do_khac_phuc, ghi_chu) VALUES ('Thiết bị B', 'Phòng KT', 'Tầng 2', 'Sự cố', '2025-07-01', 'Đã lập biên bản', 'Mất nguồn')")
conn.commit()
conn.close()
print("Initialized database with sample data.")
