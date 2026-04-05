import mysql.connector

# Konfigurasi koneksi (Sesuaikan dengan settingan XAMPP kamu)
db = mysql.connector.connect(
  host="localhost",
  user="root",        # Default XAMPP adalah root
  password="Fathao;ifh02",        # Default XAMPP adalah kosong
  database="startup_logistik" # Nama database yang kamu buat tadi
)

cursor = db.cursor()

# Coba ambil data (untuk ngetes aja)
cursor.execute("SELECT DATABASE();")
data = cursor.fetchone()

print(f"✅ Kamu terhubung ke database! : {data[0]}")

# Tutup koneksi
db.close()