luas = lambda jarijari : 3.14159 * jarijari ** 2

try :
    jari = float(input("Isikan Nilai Jari-Jari :"))
    result = luas(jari)
    print(f'Luas dari lingkaran dengan jari jari {jari} adalah {result}')
except ValueError :
    print("Nilai Jari-Jari Harus Angka")