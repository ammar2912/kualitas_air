from flask import Flask, request
from fuzzy_without_do import hitung_sugeno
import mysql.connector
from config import connect_db
from datetime import datetime

app = Flask(__name__)

@app.route('/kualitas-air', methods=['GET', 'POST'])
def kualitas_air():
    # Menggunakan request.form, bukan request.from
    suhu = float(request.form['suhu'])
    ph = float(request.form['ph'])
    tds = float(request.form['tds'])
    id_alat = int(request.form['id_alat'])

    
    # Menghitung kualitas air
    kualitas = hitung_sugeno(suhu, tds, ph)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Membuka koneksi ke database
    db = connect_db()
    cursor = db.cursor()
    
    # Memasukkan data ke tabel kualitas_air
    sql = "INSERT INTO kualitas_air (ph, suhu, tds, id_alat, label, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (ph, suhu, tds, id_alat, kualitas, timestamp))
    
    # Commit perubahan
    db.commit()

    # Menutup koneksi database
    cursor.close()
    db.close()

    return 'Data berhasil disimpan', 200

if __name__ == '__main__':
    app.run(debug=True)
