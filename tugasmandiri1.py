#berat telur = brt
#harga telur = hrg
#transpot = ongkos
#uang ibu = uang
#sisa uang = sisa

brt=5
hrg=26000
ongkos=2*3500
harga_telur=brt*hrg
uang=200000
sisa=(uang-(harga_telur + ongkos))
print("sisa uang Rp : ", str(sisa))