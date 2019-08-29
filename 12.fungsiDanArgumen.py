def siswa(name):
    print('siswa ini bernama', name)

siswa('mario')

def teman(name,makanan,hobby):
    print('teman saya bernama',name,', dia suka makan',makanan,'dan hobby nya', hobby)

teman('riko','bakso','main catur')

def guru(name,pelajaran='matematika',shift='jam ke-1'):
    print('guru saya bernama',name)
    print('dia mengajar palajaran', pelajaran)
    print('dia mengajar pada',shift)
guru('udin')
guru('samsul','ipa')
guru(pelajaran='ips',name='eni',shift='jam ke-2')