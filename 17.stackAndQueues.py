print(20*'=','STACKING / TUMPUKAN',20*'=')
#---------- STACKING / TUMPUKAN ------------------
tumpukan = [1,2,3,4,5,6]
print('data sekarang = ',tumpukan)

tumpukan.append(7)
print('tambah data ->', 7)
print('data sekarang = ',tumpukan)
tumpukan.append(8)
print('tambah data ->', 8)
print('data sekarang = ',tumpukan)

dataKeluar = tumpukan.pop() #-----> remove and return item at index
print(dataKeluar)
print('data sekarang = ',tumpukan)

dataKeluar = tumpukan.pop()
print(dataKeluar)
print('data sekarang = ',tumpukan)

print(20*'=','QUEUES / ANTRIAN',20*'=')
#-------------- QUEUES / ANTRIAN ----------------
from collections import deque #----------> MODUL

antrian = deque([11,12,13,14,15]) #------> menambahkan deque didepan list
print('data antrian = ', antrian)

antrian.append(16)
print('tambah antrian ->', 16)
print('antrian sekarang =', antrian)

antrian.append(17)
print('tambah antrian ->', 17)
print('antrian sekarang =', antrian)

out = antrian.popleft() #----------------> popleft() untuk mengurangi antrian/list dibagian depan
print('data keluar = ', out)
print('antrian sekarang =', antrian)
