# a=10, a adalah variabel dengan nilai 10

#tipe data : angka satuan (integer)
data_integer = 1
print("data :", data_integer)
print("- bertype :", type(data_integer))

#tipe data : angka dengan koma (float)
data_float = 1.5
print("data :", data_float)
print("- bertype :", type(data_float))

#tipe data : kumpulan karakter (string)
data_string = "Ucup"
print("data :", data_string)
print("- bertype :", type(data_string))

#tipe data : type data biner true/false (bool)
data_bool = False
print("data :", data_bool)
print("- bertype :", type(data_bool))

#tipe data : bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertype", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertype", type(data_c_double))
