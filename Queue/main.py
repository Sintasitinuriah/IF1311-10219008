from collections import deque

antrian = deque([1,2,3,4,5])

print('data sekarang: ',antrian)

# menambahkan data
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

# mengurangi data
out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

# menambah data
antrian.append(8)
print('data masuk: ',8)
print('data sekarang: ',antrian)

# cek ukuran antrian
print(len(antrian))

# implementasi queue tanpa deque
antrian2 =[1,2,3]
print('data sekarang: ',antrian2)

# tambah / add/ enqueue
antrian2.append(4)
print('data antrian sekarang', antrian2)

# kurang / delete / dequeque
out = antrian2.pop(0)
print('data keluar : ',out)
print('data sekarang : ',antrian2)
