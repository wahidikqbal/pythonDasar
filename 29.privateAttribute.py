class mahasiswa():
    #menambahkan doble underscore / __ untuk menjadikan private
    __nilai = 0

    def __init__(self, input_nama, input_nim):
        self.nama  = input_nama
        self.nim = input_nim
        print('nama siswa', self.nama, 'nim', self.nim)

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai
        
    def status(self):
        if self.__nilai <= 50:
            print(self.nama,'nilai jelek')
                #-------> ada self.nama di print

        elif self.__nilai <= 75:
            print(self.nama,"nilai cukup")
                #-------> ada self.nama di print

        else:
            print("nilai bagus")




otong = mahasiswa("otong markotong", 123)

#print(otong.nama)
#print(otong.nim)
otong.uts(30)
otong.uas(30)
otong.status()