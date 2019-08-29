text  = 'jalan - jalan di hari minggu'
text2 = 'jalan - jalan di hari jum\'at'
text3 = 'saya berkata: "sudah makan belum?"'
text4 = 'eko menjawab: \"belum broo\"'
text5 = 'maimunah: "kemaren kemana bro?" \neko: "kmaren ke salon"'

#All string
text6 = '''
eko: "hari ini masuk jam berapa coy?"
aji: "hari ini masuk jam 3 coy"
eko: "berangkat kuy!!"
aji: "kuy kuy"
'''

#raw string
text7 = r'C:\nyoto'

#pengkalian string
print(5*"wk")

#penggabungan 2 kalimat
print(text + text2)


#|s|e|p|a|n|j|a|n|g| |j |a |l |a |n |
#| | | | | | | | | | |  |  |  |  |  |
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#print huruf ke - ... | dimulai dari 0
kata = "sepanjang jalan"
a    = kata[3]
print(a)

#print huruf ke-... , sampai huruf ke-...
kata2 = "hallo dunia"
b     = kata2[2:8]
print(b)
