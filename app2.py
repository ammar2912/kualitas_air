from flask import Flask, request
from fuzzy_do import hitung_sugeno
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
    do = float(request.form['do'])
    id_alat = int(request.form['id_alat'])

    
    # Menghitung kualitas air
    label, hasil = hitung_sugeno(suhu, do, ph, tds)

    # return str(label), str(hasil)
    
    # # Membuka koneksi ke database
    # db = connect_db()
    # cursor = db.cursor()
    
    # # Memasukkan data ke tabel kualitas_air
    # sql = "INSERT INTO kualitas (ph, suhu, tds, do, id_alat, hasil, label) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # cursor.execute(sql, (float(ph), float(suhu), float(tds), float(do), id_alat, float(hasil), label))
    
    # # Commit perubahan
    # db.commit()

    # # Menutup koneksi database
    # cursor.close()
    # db.close()

    # return 'Data berhasil disimpan', 200

if __name__ == '__main__':
    app.run(debug=True)
