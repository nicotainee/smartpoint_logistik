import mysql.connector
import qrcode

# 1. Koneksi ke Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fathao;ifh02", # Sesuaikan lagi kalau tadi kamu pakai "root"
    database="startup_logistik"
)
cursor = db.cursor()

# 2. Input Data dari Kamu (User)
print("--- INPUT ALAMAT BARU ---")
kode = input("Masukkan Kode Unik (misal BDG001): ")
nama = input("Nama Penerima: ")
lat = input("Latitude (dari Google Maps): ")
lon = input("Longitude (dari Google Maps): ")
patokan = input("Patokan Visual (Warna pagar/ciri rumah): ")

# 3. Simpan ke SQL
sql = "INSERT INTO smart_points (kode_unik, nama_penerima, latitude, longitude, patokan_visual) VALUES (%s, %s, %s, %s, %s)"
val = (kode, nama, lat, lon, patokan)

try:
    cursor.execute(sql, val)
    db.commit()
    print(f"✅ Data {nama} berhasil disimpan ke SQL!")

    # 4. Langsung Bikin QR Code-nya Otomatis
    maps_url = f"https://www.google.com/maps?q={lat},{lon}"
    img = qrcode.make(maps_url)
    img.save(f"QR_{kode}.png")
    print(f"✅ QR Code untuk {kode} sudah siap di folder!")

except Exception as e:
    print(f"❌ Waduh, ada error: {e}")

db.close()