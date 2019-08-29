#print list
barang = ['sapu','kunci','motor']
print(barang)

#manambahkan data-list
barang.append('sepeda')
print(barang)

#menambahakan data-list tiap huruf
barang.extend('abc')
print(barang)

#menambahkan data-list berdasarkan urutan
barang.insert(3,'sapu')
print(barang)

#menghitung data-list
jumlahBarang = barang.count('sapu')
print('jumlah sapu adalah', jumlahBarang)

#menghapus data-list (yg pertama kali ditemui)
barang.remove('sapu')
print(barang)

#membalikkan urutan data-list
barang.reverse()
print(barang)

print('-----------DANGERRR!!!--------------')
biring = barang.copy()
biring.append('mejaBiring')
print('ini adalah list biring = ',biring)

print('ini adalah list barang = ',barang) #data dari biring tercopy ke data Barang, padahal yg ditambahkan mejaBiring hanya data Biring

#ANTISIPASI
#dengan menambahkan .copy() pada data barang