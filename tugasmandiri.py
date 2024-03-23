
print("****************")
brt=int(input("Masukan berat telur :"))
hrg=int(input("harga telur :"))
ongkos=int(input("tarif angkot pp :"))
uang=int(input("uang yang dibawa ibu :"))
sisa=(uang-brt*hrg-ongkos*2)
print("=============================")

print("berat telur :",str(brt) + 'kg')
print("harga telur Rp :", hrg)
print("ongkos pp :", ongkos*2)
print("uang yang dibawa Rp :", uang)
print("sisa Rp :", sisa)