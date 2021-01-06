 Latihan logika dan kompparasi 

# membuat gabungan area rentang dari angka 

# ++++++3------10++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nLebih dari 10\n"))

# ++++++3-----------------
# memeriksa angka kurang dari 3
isKurangDari =(inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

# -----10+++++++++++++++
# memeriksa angka lebiih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =",isLebihDari)

# ++++++3------10++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan",isCorrect)


# ++++++3------10++++++

inputUser = float(input("masukan angka yang bernilai\nLebih dari 3\natau\nKurang dari 10\n"))

# -------3++++++++++++
# memeriksa angka Lebih dari 3
isLebihDari =(inputUser > 3)
print("Lebih dari 3 =",isLebihDari)

# ++++++10--------
# memeriksa angka Kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =",isKurangDari)

# -------3++++++10------
isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan",isCorrect)
