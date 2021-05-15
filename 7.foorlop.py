#list dalam itereable
gorengan = ['tahu', 'tempe', 'weci', 'menjes', 'brontak']

for g in gorengan:
    print(g) 


print(100*'=')

#string sebagai itereable

ayamgoreng = 'ayamgoreng'
for huruf in ayamgoreng:
    print(huruf)

print(100 * '=')

#for dalam for
buah  = ['semangka', 'apel', 'nanas', 'melon', 'pisang']
sayur = ['kangkung', 'wortel', 'tomat', 'buncis', 'kentang']

Beli  = [gorengan,buah,sayur]
for daftarBeli in Beli:
    print(daftarBeli)
    for komponen in daftarBeli:
        print(komponen)