import qrcode

def generate_smart_point(lat, lon, label):
    # Format link Google Maps untuk navigasi presisi
    # Link ini otomatis akan membuka aplikasi Maps di HP kurir
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    
    # Buat QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(maps_url)
    qr.make(fit=True)

    # Simpan jadi gambar
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"SmartPoint_{label}.png"
    img.save(filename)
    
    print(f"✅ QR Code untuk '{label}' berhasil dibuat!")
    print(f"📍 Koordinat: {lat}, {lon}")
    print(f"📂 File disimpan sebagai: {filename}")

# CONTOH: Titik di sekitar Telkom University (Gedung Kuliah Umum / GKU)
# Kamu bisa ganti koordinat ini dengan titik depan kosanmu
latitude = -6.974028 
longitude = 107.630367
nama_lokasi = "GKU_Telkom_University"

generate_smart_point(latitude, longitude, nama_lokasi)