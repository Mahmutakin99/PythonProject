from modül1 import bin, dec
'''
def bin(sayi):
    liste = []
    while sayi:
        liste.append(int(sayi % 2))
        sayi >>= 1
    liste.reverse()
    return liste

def dec(liste):
    liste.reverse()
    deger = 0
    j = 0
    for i in liste:
        if i == 1:
            deger += i * (2**j)
        j+=1
    return deger
'''
print("***********************************\n\nProgramdan çıkmak için herhangi bir seçim noktasında q ya basınız\n\n***********************************")
while True:
    secim = input("binary e çevir için (bin) veya decimal e çevir için (dec) yazınız: ")
    if secim == 'q':
        break
    
    if secim == 'bin':
        x = input("decimal int değer giriniz: ")
        if x == 'q':
            break
        x = int(x)
        liste = bin(x)
        for i in liste:
            print(i , end= '')
        print()
            

    if secim == 'dec':
        liste = input("binary değer giriniz: ")
        if secim == 'q':
            break
        liste = [int(i) for i in liste]
        print(dec(liste))