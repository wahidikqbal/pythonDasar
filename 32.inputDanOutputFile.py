file = open("32.Data.txt", 'w')
file.write('ini adalah baris pertama write')
file.write('\nini adalah baris kedua write')
file.close()

file = open("32.Data.txt", 'a')
file.write('\nini baris ke tiga, dibuat menggunakan append')
file.close()

file3 = open("32.Data.txt", 'r')
print(file3.readline())
file3.close()

file4 = open("32.DataBaru.txt", 'w')
file4.write('ini adalah data baru , dibuat menggunakan write')
file4.close()


# w = write
# a = append
# r = read only
# r+ = write and read mode