class siswa():
    #pass ---> kalau class kosong pakai pass

    nama = 'masih kosong'

    def makan(self, argumen):
        print(self.nama, 'sedang makan', argumen)   #---> 1.self.nama memanggil nama
                                                    #---> 2.argumen memanggil argumen

    def belajar(self, argumen):
        print(self.nama, 'sedang belajar', argumen)

    def kelas(self, arg):
    	print(self.obj, 'adalah', arg)

arifin 		= siswa()
ucup   		= siswa()
keterangan 	= siswa()


arifin.nama = 'arifin ilham'
ucup.nama   = 'ucup markucup'

arifin.makan('sayur bayem') 
ucup.belajar('python')


keterangan.obj	= 'kelas satu'
keterangan.kelas('kelas pertama')