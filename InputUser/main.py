# input user

# data yang dimasukan pasti string
data = input("masukkan data : ")

print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka float : "))
print("data float =",angka,",type = ",type(angka))

angka = int(input("masukan angka int: "))

print("data int =",angka,",type = ",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukkan nilai bool =")))

print("data = ",biner,",type =",type(biner))
