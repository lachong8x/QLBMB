
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
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

@app.route('/add', methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        name = request.form['name']
        system = request.form['system']
        status = request.form['status']
        error_date = request.form.get('error_date')
        progress = request.form.get('progress')

        conn = get_db_connection()
        conn.execute('INSERT INTO devices (name, system, status, error_date, progress) VALUES (?, ?, ?, ?, ?)', 
                     (name, system, status, error_date, progress))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_device.html')
