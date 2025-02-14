import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Host MySQL
        port=8111,         # Port MySQL (ubah sesuai dengan konfigurasi server Anda)
        user="root",       # Username MySQL
        password="",  # Password MySQL
        database="db_sanke"  # Nama database yang digunakan
    )