# latihan konversi satuan temperature

# program konversi celcius ke satuan lain 

print("\n PROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah ",celcius ,"Celius")

# reamur
reamur = (4/5)* celcius
print("suhu dalam reamur adalah ",reamur,"Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit,"Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin,"Kelvin")
