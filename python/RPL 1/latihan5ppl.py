#buat 3 objek orang, pelajar, pekerja
#orang = kelas induk
#orang dan pekerja = kelas turunan

from multiprocessing import set_forkserver_preload
from sys import orig_argv


class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("Hallo Nama Saya", self.nama, "Dari", self.asal)

class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
        orang.__init__(self, nama, asal)
        self.sekolah = sekolah
        

class pekerja(orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor


andi = orang('Hisyam','Jakarta\n')
andi.perkenalan()

tito = pelajar('tito','subang', 'smk jp1 ')
tito.perkenalan()
print(f'Saya Sekolah di{tito.sekolah}\n')

anto = pekerja('anto','bandung','Smk JP1')
anto.perkenalan()
print(f'Saja Kerja Di{anto.kantor}')
