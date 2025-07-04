import sqlite3

# Kết nối (nếu chưa có file sẽ tự tạo)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Xoá bảng nếu đã tồn tại để tránh lỗi khi chạy lại nhiều lần (có thể bỏ nếu muốn giữ dữ liệu cũ)
cursor.execute("DROP TABLE IF EXISTS devices")

# Tạo bảng devices
cursor.execute('''
    CREATE TABLE devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        system TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

# Thêm dữ liệu mẫu
sample_data = [
    ('Thiết bị A', 'Windows', 'Online'),
    ('Thiết bị B', 'Linux', 'Offline'),
    ('Thiết bị C', 'macOS', 'Online')
]

cursor.executemany('''
    INSERT INTO devices (name, system, status)
    VALUES (?, ?, ?)
''', sample_data)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("✅ Database initialized and sample data inserted.")
