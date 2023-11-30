# konsonan
def cuma_konsonan(kalimat):
    konsonan = ""
    for huruf in kalimat:
        if huruf.isalpha() and huruf.lower() not in 'aiueo':
            konsonan += huruf
    return konsonan

# fungsi
hasil = cuma_konsonan("Nurul Fikri")
print(hasil)
