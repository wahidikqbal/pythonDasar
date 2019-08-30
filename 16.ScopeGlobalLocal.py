mobil = 'avanza'
print('saya punya mobil',mobil)

def gantiMobil(mobilBaru):
    global mobil #-------------> global, membuat data menjadi global
    #delete global untuk mengetehui perbedaan
    mobil = mobilBaru
    print('saya beli mobil baru', mobilBaru)
gantiMobil('terios')

print('mobil saya sekarang',mobil)