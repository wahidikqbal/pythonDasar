class siswa():
    
    jurusan = "ekonomi"
    siswa = 0
    def __init__(self, inputName, inputNim):
        self.name = inputName
        self.nim  = inputNim

otong = siswa('otong surotong', 123)
ucup  = siswa('ucup markcup', 124)


otong.jurusan = "Teknik Informasi"

print(otong.name)

print(siswa.jurusan)
print(otong.jurusan)