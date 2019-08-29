#mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')

#memanggil fungsi
fungsi()

print(10*'=-')

def salam():
    print('haloo, mau beli apa?')

def kata1():
    salam()
    print('harga daging per 1 kg adalah Rp. 20.000')

def listHarga(kg):
    kata1()
    hargaDaging = 20000
    hargaBeli  = hargaDaging*kg
    print('harga',kg,'daging, adalah',hargaBeli)

listHarga(2)
listHarga(0.5)