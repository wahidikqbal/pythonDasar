siswa = [
    'kacong',
    'ipul',
    'gundala',
    'ponari',
    'mirjan',
    'sayuti' 
]

nilai = [
    100,
    76,
    80,
    90,
    65,
    55
]

print(10*'--','UNTUK LIST DAN TUPLE',10*'--')
#enumerate -----> untuk mengambil urutan dari list
for i,nomerAbsen in enumerate(siswa):
    print(i, ' => ', nomerAbsen)

#zip ------> menggabungkan 2 list
for rapot, nama in zip(nilai,siswa):
    print(nama,'mendapatkan nilai :',rapot)



print(10*'--','UNTUK TIPE DATA SET',10*'--')
#TIPE DATA SET
indonesia = {
    'jawa',
    'bali',
    'kalimantan',
    'sumatera',
    'sulawesi',
    'papua',
    'lombok' 
}

for pulau in sorted(indonesia): #sorted() --> untuk mengurutkan tipedata SET
    print(pulau)

print(10*'--','UNTUK TIPE DATA DICTIONARY',10*'--')
#TIPE DATA DICTIONARY
hobby = {
    'eko'       : 'makan',
    'pandji'    : 'futsal',
    'dika'      : 'jalan-jalan',
    'ratu'      : 'shopping',
    'kobal'     : 'ngoding',
}
#items() ---> mengambil semua data dictionary
for orang,suka in hobby.items():
    print(orang,'hobbynya',suka)
#keys() ---> mengambil data kunci/depan saja
for orang in hobby.keys():
    print('nama teman saya:', orang)
#valuse() ---> mengambil data nilai/belakang saja
for suka in hobby.values():
    print('hobby teman saya', suka)