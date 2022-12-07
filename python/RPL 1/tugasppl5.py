
class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def output(self):
        print(self.nama, "Beragama", self.agama)

class islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat
        

class kristen(Agama):
    def __init__(self, nama, agama, khotbah):
        super().__init__(nama, agama)
        self.khotbah = khotbah


hisyam = islam('Hisyam','Islam', 'sholat')
hisyam.output()
print(f'{hisyam.nama} Beribadah Dengan Melakukan {hisyam.sholat}\n')

bram = kristen('Abraham','kristen','khotbah')
bram.output()
print(f'{bram.nama} Beribadah Dengan Melakukan {bram.khotbah}')
