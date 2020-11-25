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


