from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

# MINGGU 2: Data Exclesia dan Lovely
info_toko ={
    "nama_toko": "Baked Dough",
        "slogan": "Warm Bakes for Sweet Days",
        "lokasi": "Planet Lampung",
        "no_wa": "6285768085517"
}

# ==== MINGGU 3: Daftar Produk (list of Dictionnaries) ====
daftar_produk = [
    {
    "nama": "Pastry",
    "harga": 20000,
    "gambar": "pastry.jpg" 
    },
    {
    "nama": "Cookies",
    "harga": 35000,
    "gambar": "cookies.jpg"
    },
    {
    "nama": "Bagel",
    "harga": 10000,
    "gambar": "bagel.jpg"
    },
    {
    "nama": "Slice Cake",
    "harga": "65000",
    "gambar": "slice_cake.jpg"
    }
]

@app.route('/')
def halaman_depan ():
    return render_template(
        'index.html',
        data=info_toko,
        produk=daftar_produk
        )

    #halaman detail dan checkout
@app.route('/detail?<int:id_barang>')
def halaman_detail(id_barang):
    
    barang_ketemu = None

# Mencari produk berdasarkan id
    for p in daftar_produk:
        if p ['id'] == id_barang:
            barang_ketemu = p
            break

        #jika ditemukan
        if barang_ketemu:
            #membuat pesan otomatis
            pesan = (
                f"Hai min BAked Dough! Mau order roti/pastry-nya dong!"
                f"{barang_ketemu['nama']}"
                f"seharga Rp {barang_ketemu['harga']}."
                f"Mohon info total harga, makasih!"
            )

            #mengubah pesan agar aman dimasukkan ke URL
            pesan_encoded = quote(pesan)

            #membuat link whatsapp otomatis
            link_wa = (
                f"https://wa.me/{info_toko['no_wa']}"
                f"?text={pesan_encoded}"
            )

            return render_template(
                'detail:html',
                barang=barang_ketemu,
                data_toko=info_toko,
                link_wa=link_wa
            )
        # jika produk tidak ditemukan
        else:
            return "Produk tidak ditemukan", 404

    if __name__ == '__main__':
        app.run(debug=True)