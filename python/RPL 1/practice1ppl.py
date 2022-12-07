# Jenis enkapsulasi : public, protected, privete

# membuat public class

class siswa:
    def __init__(self, siswa):
        self.siswa = siswa

#instasiasi 
nama_siswa = siswa('hisyam')

# print
print(f'1. siswa kami bernama {nama_siswa.siswa} ganteng')


# membuat protected class
class gurujp1: #class induk
    def __init__(self,guru):
        self._guru = guru #protected classs declaration


class guru(gurujp1): #class turunan
    def __init__(self, guru):
        super().__init__(guru) #panggil merk dibagian sini

    def nama_guru(self):
        # hak akses _merk  dari subclass
        print (f'2. Guru Kami Bernama {self._guru} Yang Cantik')

# instamsiasi
output = guru('bu anita')
output.nama_guru()

# Membuat privete class
class kepsek:
    def __init__(self, nama):
        self._nama = nama #privete class declaration

    def tampilkan_nama(self):
        print(f'3. kepsek kami biasa disebut {self._nama}') 

#instansiasi
siapa = kepsek('pak lilik')
siapa.tampilkan_nama()
