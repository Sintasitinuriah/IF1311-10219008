# Latihan Komparasi dan Logika 
# 1. -------0++++++5-------8++++++11------

inputUser = float(input("masukan angka yang bernilai : "))

# -----0+++++
# memeriksa angka Lebih dari 0
isLebihDari0 = inputUser > 0
print("Lebih dari 0 =",isLebihDari0)

# +++++5-----
# memeriksa angka Kurang dari 5
iskurangDari5 = inputUser < 5
print("Kurang dari 5 =",iskurangDari5)

# -----8+++++
# memeriksa angka Lebih dari 8
isLebihDari8 = inputUser > 8
print("Lebih dari 8 =",isLebihDari8)

# +++++11-----
# memeriksa angka Kurang dari 11
isKurangDari11 = inputUser < 11
print("kurang dari 11 =",isKurangDari11)

isCorrect1 = (isLebihDari0 and iskurangDari5) or (isLebihDari8 and isKurangDari11)
print("angka yang anda masukan",isCorrect1)

# 2. +++++0-----5++++++8-------11+++++
inputUser = float(input("masukan angka yang bernilai\nLebih dari 0\natau\nKurang dari 5\ndan\nLebih dari 8\natau\nKurang dari 11\n"))

# ++++++0-----------------
# memeriksa angka kurang dari 0
isKurangDari0 =inputUser < 0
print("Kurang dari 0 =",isKurangDari0)

# -----5+++++++++++++++
# memeriksa angka lebiih dari 5
isLebihDari5 = inputUser > 5
print("Lebih dari 5 =",isLebihDari5)

# ++++++8-----------------
# memeriksa angka kurang dari 8
isKurangDari8 = inputUser < 8
print("Kurang dari 8 =",isKurangDari8)

# -----11+++++++++++++++
# memeriksa angka lebiih dari 11
isLebihDari11 = inputUser > 11
print("Lebih dari 11 =",isLebihDari11)

# ++++++0------5++++++8------11++++++
isCorrect2 = (isKurangDari0 or isLebihDari5) and (isKurangDari8 or isLebihDari11)
print("angka yang anda masukan",isCorrect2)
