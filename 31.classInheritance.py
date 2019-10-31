class siswa():

    def __init__(self, nama, absen, nilai):
        self.nama  = nama
        self.absen = absen
        self.nilai = nilai
    
    def cekStatus(self):
        print('SISWA no absen',self.absen,'.', self.nama, 'nilainya adalah', self.nilai)

#turunan dari class siswa
class siswi(siswa):
    def cekStatus(self):
        print('SISWI no absen',self.absen,'.', self.nama, 'nilainya adalah', self.nilai)


murid1 = siswa('dito', 3, 75)
murid2 = siswi('andini', 1, 90)


murid1.cekStatus()
murid2.cekStatus()
