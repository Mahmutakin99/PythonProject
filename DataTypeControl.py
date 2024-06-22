def DataTypeControl(x = ""):
    # veri türünü kontrol et
    # check data type
    
    try:
        return int(x)
    except ValueError:
        pass
    
    try:
        return float(x)
    except ValueError:
        pass
    
    return x


int_list = []
str_list = []
float_list = []

a = int(input("How many data will you enter: "))
# her hangi veri giriniz
# any number of data input
for i in range(a):
    # veri girişi
    # data input
    x = input(f"{i+1}. Enter data: ")
    # veriyi fonksiyona gönder
    # send data to the function
    x = DataTypeControl(x)
    # veriyi türüne göre ayır
    # sorting data by type
    if type(x) == int:
        int_list.append(x)
    elif type(x) == float:
        float_list.append(x)
    elif type(x) == str:
        str_list.append(x)
    # olası hatalar için
    # For possible errors    
    else: 
        print("Escape block for possible errors")
        
# türüne göre verileri ekrana yazdır
# print data to the screen by type
if len(int_list) > 0:
    print("int: ",int_list)
if len(float_list) > 0:
    print("float: ",float_list)
if len(str_list) > 0:
    print("str: ",str_list)