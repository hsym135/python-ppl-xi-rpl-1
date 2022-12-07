#belajar objek dan class

class kucing:
    warna = None
    usia = None

class icikiwir:
    merk = None
    kecepatan = None

#membuat instance atau variabel sebagai "objek nyata"
kucing1 = kucing()
kucing1.warna = "black"
kucing1.usia = "4 bulan"

kucing2 = kucing()
kucing2.warna = "putih"
kucing2.usia = "5 bulan"

pembalap_handal = kucing()
pembalap_handal = icikiwir()
pembalap_handal.warna = "hitam"
pembalap_handal.merk = "honda karbu"
pembalap_handal.kecepatan = "100km"

print("kucing",pembalap_handal.warna, "menaiki icikiwir", pembalap_handal.merk, "dengan kecepatan", pembalap_handal.kecepatan)