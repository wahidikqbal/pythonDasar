class siswa():
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim  = input_nim
        print('inisialiisasi siswa')

    def makan(self, argumen):
        print(self.nama, 'sedang makan', argumen)
    def belajar(self, argumen):
        print(self.nama, 'sedang belajar', argumen)
    def nomer(self):
    	print(self.nama, 'nimnya adalah', self.nim)

#mengisi data argument
siswa = siswa("TEJO SUBIANTO", 123)

siswa.belajar('matematika')
siswa.makan('duren')
siswa.nomer()


#print(siswa.nama)
#print(siswa.nim)
