#contoh penggunaan
hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
    ]


def lulus_saja(hasil_akhir):
    lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] >65]
    return lulus

print(lulus_saja(hasil_akhir))