# Input
try :
    suhu = float(input("Input Besaran Suhu :"))
except ValueError as e :
    print("error :", e)
    exit()

format_suhu = input("Format Suhu (c/f/k) :")
konversi_suhu = input("Konversi Suhu (c/f/k) :")
hasil = ""

# Proses
# x adalah suhu
# y adalah format suhu
# z adalah konversi suhu
def konversiSuhu(x, y, z) :
    global hasil
    #cek kondisi untuk celcius ke fahrenheit
    if y == 'c' and z == 'f' :
        f = (9/5) * x + 32
        hasil = f'{f}{z.upper()}'
    # cek kondisi untuk celcius ke kelvin
    elif y == 'c' and z == 'k' :
        k = x + 273.15
        hasil = f'{k}{z.upper()}'
    # cek kondisi untuk fahrenheit ke celcius
    elif y == 'f' and z == 'c' :
        c = x - 32* (5/9)
        hasil = f'{c}{z.upper()}'
    #cek kondisi untuk fahrenheit ke kelvin
    elif y == 'f' and z == 'k' :
        k = (5/9) * x + 459.67
        hasil = f'{k}{z.upper()}'
    #cek kondisi untuk kelvin ke celcius
    elif y == 'k' and z == 'c' :
        c = x - 273.15
        hasil = f'{c}{z.upper()}'
    #cek kondisi untuk kelvin ke fahrenheit
    elif y == 'k' and z == 'f' :
        f = (x - 273.15) * (9/5) + 32
        hasil = f'{f}{z.upper()}'
    else :
        hasil = "Konversi nilai tidak valid"

if(format_suhu == konversi_suhu):
    hasil = f'{suhu} {format_suhu.upper()}'
else :
    konversiSuhu(suhu, format_suhu, konversi_suhu)

# Output
print(hasil)