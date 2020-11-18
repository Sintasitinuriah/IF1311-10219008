#Casting type data
#merubah dari satu type ke type lain

#Integer
data_int = 9;
print("data =", data_int,",type=", type(data_int))

data_float= float(data_int)
data_str= str(data_int)
data_bool= bool(data_int)#akan false jika nilai int = 0

print("data =", data_float,",type=", type(data_float))
print("data =", data_str,",type=", type(data_str))
print("data =", data_bool,",type=", type(data_bool))

#float 
print("====FLOAT====")
data_float = 0.999999;
print("data =", data_float,",type=", type(data_float))

data_int= int(data_float)
data_str= str(data_float)
data_bool= bool(data_float)

print("data =", data_int,",type=", type(data_int))
print("data =", data_str,",type=", type(data_str))
print("data =", data_bool,",type=", type(data_bool))

print("====BOOLEAN====")
data_bool = False;
print("data =", data_bool,",type=", type(data_bool))

data_float= float(data_bool)
data_str= str(data_bool)
data_int= int(data_bool)

print("data =", data_int,",type=", type(data_int))
print("data =", data_str,",type=", type(data_str))
print("data =", data_float,",type=", type(data_float))

print("====String====")
data_str = "10";
print("data =", data_str,",type=", type(data_str))

data_float= float(data_str)
data_bool= bool(data_str)
data_int= int(data_str)

print("data =", data_int,",type=", type(data_int))
print("data =", data_bool,",type=", type(data_bool))
print("data =", data_float,",type=", type(data_float))