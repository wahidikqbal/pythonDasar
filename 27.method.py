class siswa():
    #pass ---> kalau class kosong pakai pass
    nama = 'masih kosong'
    def makan(self, argumen):
        print(self.nama, 'sedang makan', argumen)   #---> 1.self.nama memanggil nama
                                                    #---> 2.argumen memanggil argumen

arifin = siswa()
ucup   = siswa()

arifin.nama = 'arifin ilham'

arifin.makan('sayur bayem')  