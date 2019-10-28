class siswa():
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim  = input_nim

    def makan(self, argumen):
        print(self.nama, 'sedang makan', argumen)
    def belajar(self, argumen):
        print(self.nama, 'sedang belajar', argumen)

#mengisi data argument
siswa = siswa("TEJO SUBIANTO", 123)

print(siswa.nama)
print(siswa.nim)

print(siswa.belajar)