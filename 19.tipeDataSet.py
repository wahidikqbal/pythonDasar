#TIPE DATA SET / HIMPUNAN

mobil = {
    'avanza',
    'xenia',
    'jazz',
    'pajero',
    'fortuner'
}

print(mobil)

mobil.add('lamborgini')
print(mobil)
print(sorted(mobil)) #-----> sorted(arg), mengurutkan data

ganjil = {1,3,5,7,9}
genap  = {2,4,6,8,10}
prima  = {2,3,5,7,11}

a = ganjil.union(prima)
b = genap.intersection(prima)

print(a)
print(b)