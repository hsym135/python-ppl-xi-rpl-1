def garis():
    print("===========================================")

garis()
print("Selamat datang di alfamart")
garis()

print()
kasir = input("Nama Kasir = ")
total_item = int(input("masukan total harga ="))
tunai = int(input("masukan uang tunai = "))
kembalian = tunai - total_item
print()

garis()
print ("kasir yang bertugas = ",kasir)
print ("total item = ",total_item)
print ("tunai=",tunai)
print ("kembalian=",kembalian)
garis()

print()
print("Terima kasih telah berbelanja di alfamart")
