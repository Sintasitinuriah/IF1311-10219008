tumpukan = [1,2,3]
print('data sekarang: ',tumpukan)

tumpukan.append(4)# fungsi push
print('data sekarang: ',tumpukan)

tumpukan.append(9) # fungsi push
print('data sekarang: ',tumpukan)

size = len(tumpukan) # cek jumlah item
print('jumlah item dalam stack',size)

out = tumpukan.pop() #fungsi pop
print('item yang dikeluarkan',out)
print('data sekarang : ',tumpukan)

print('cara mengakses top',tumpukan[-1])
