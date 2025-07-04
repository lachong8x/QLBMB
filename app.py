from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    devices = conn.execute('SELECT * FROM devices').fetchall()
    conn.close()
    return render_template('dashboard.html', devices=devices)

@app.route('/add', methods=('GET', 'POST'))
def add_device():
    if request.method == 'POST':
        name = request.form['name']
        don_vi_quan_ly = request.form['don_vi_quan_ly']
        vi_tri = request.form['vi_tri']
        trang_thai = request.form['trang_thai']
        ngay_phat_hien_su_co = request.form.get('ngay_phat_hien_su_co') or None
        tien_do_khac_phuc = request.form.get('tien_do_khac_phuc') or None
        ghi_chu = request.form.get('ghi_chu') or None
        ngay_ket_thuc_su_co = None

        if trang_thai == 'Hoạt động tốt':
            tien_do_khac_phuc = None
            ngay_phat_hien_su_co = None

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO devices (name, don_vi_quan_ly, vi_tri, trang_thai, ngay_phat_hien_su_co, tien_do_khac_phuc, ghi_chu, ngay_ket_thuc_su_co)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, don_vi_quan_ly, vi_tri, trang_thai, ngay_phat_hien_su_co, tien_do_khac_phuc, ghi_chu, ngay_ket_thuc_su_co))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_device.html')
