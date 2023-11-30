# duplikasi list buah
list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(list_buah):
    list_baru = []
    for buah in list_buah:
        list_baru.extend([buah, buah])
    return list_baru

# fungsi
hasil = duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print(hasil)


