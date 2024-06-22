from modül1 import dec,bin
def DataTypeControl(x):
    if len(x) > 0:
        # Geçerli bir binary string olup olmadığını kontrol et
        
        # all(char in '01' for char in x): Bu ifade, x stringindeki her karakterin '0' veya '1' olup olmadığını kontrol eder.
        
        # all(): Bu fonksiyon, içindeki tüm ifadeler True ise True döner. Eğer x stringindeki tüm karakterler 
        # '0' veya '1' ise, all(char in '01' for char in x) ifadesi True döner.
        
        if all(char in '01' for char in x):
            return x
        else:
            return "I think something's wrong"
    
    else:
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
    
def binÇarpma(liste1,liste2):
    i, j = dec(liste1), dec(liste2)
    return bin(i * j)

def binBölme(liste1,liste2):
    i, j = dec(liste1), dec(liste2)
    return bin(i / j)
    

'''
def binToplama(liste1=[0], liste2=[0]):
    liste1, liste2 = liste1[::-1], liste2[::-1]
    elde = 0
    liste = []
    for i in range(max(len(liste1), len(liste2))):
        bit1 = liste1[i] if i < len(liste1) else 0
        bit2 = liste2[i] if i < len(liste2) else 0
        toplam = bit1 + bit2 + elde
        liste.append(toplam % 2)
        elde = 1 if toplam >= 2 else 0
    if elde:
        liste.append(1)

    return liste[::-1]
'''
'''
def binToplama(liste1, liste2):
    liste = []
    liste1.reverse()
    liste2.reverse()
    elde = 0
    for i in range(l1):
        if i < l1:
            bit1 = liste1[i]
        else:
            bit1 = 0
        if i < l2:
            bit2 = liste2[i]
        else:
            bit2 = 0
        toplam = bit1 + bit2 + elde
        if toplam == 3:
            liste.append(1)
            elde = 1
        elif toplam == 2:
            liste.append(0)
            elde = 1
        elif toplam == 1:
            liste.append(1)
            elde = 0
        else:
            liste.append(0)
    if elde == 1:
        liste.append(1)
    return liste[::-1]
'''

def binToplama(liste1,liste2):
    liste1.reverse()
    liste2.reverse()
    elde = 0
    sonuc = []
    for i in range(0,len(liste1)):
        if liste1[i] + liste2[i] + elde == 0:
            sonuc.append(0)
        elif liste1[i] + liste2[i] + elde == 1:
            sonuc.append(1)
        elif liste1[i] + liste2[i] + elde == 2:
            sonuc.append(0)
            elde = 1
        else:
            sonuc.append(1)
            elde = 1
    if elde == 1:
        sonuc.append(1)
    sonuc.reverse()
    return sonuc



def binÇıkarma(liste1=[0],liste2=[0]):
    a=[1]
    for i in range(0,len(liste1)-1):
        a.insert(i,0)
    liste3 = liste2[::-1]
    liste4 = binToplama(liste3,a)
    liste5 = binToplama(liste1,liste4)
    if len(liste5) == len(liste1):
        return liste5
    else:
        while True:
            if len(liste5) == len(liste1):
                break
            else:
                liste5.pop(0)
        return liste5

def BinaryListeyeÇevir(liste):
    return [int(i) for i in liste]


'''
def binÇarpma(liste1, liste2):
    liste1.reverse()
    liste2.reverse()
    sonuc = []
    gecici_sonuc = []
    for i in range(len(liste2)):
        gecici_sonuc = binToplama(liste1, [0] * i + [liste2[i]])
        for j in range(min(len(sonuc), len(gecici_sonuc))):
            gecici_sonuc[j] += sonuc[j]
            elde = gecici_sonuc[j] // 2
            gecici_sonuc[j] %= 2
            if elde:
                if j == len(gecici_sonuc) - 1:
                    gecici_sonuc.append(elde)
                else:
                    gecici_sonuc[j + 1] += elde
        sonuc = gecici_sonuc[:]  # Her iterasyonda sonucu güncelle
    return sonuc[::-1]


def binÇarpma(liste1, liste2):
    liste1.reverse()
    liste2.reverse()
    sonuc = []
    liste = []
    for i in range(len(liste2)):
        sonuc.append(0)
    for i in range(len(liste2)):
        if i > 0: # kaydırma işlemi
            for x in range(i):
                liste1.insert(0,0)
        if liste2[i] == 0:
            temp = [0] * len(liste1)
            binToplama(liste1,temp)
        elif liste2[i] == 1:
            binToplama(liste1,sonuc)
        
    sonuc.reverse()
    return sonuc
'''

print("programdan çıkmak için herhangi bir seçim noktasında q ya basınız.")
while True:
    liste1 = input("binary bir değer giriniz:\n--> ")
    if liste1.lower() == 'q':
        break
    
    liste2 = input("binary ikinci değeri giriniz:\n--> ")
    if liste2.lower() == 'q':
        break
    
    liste1 = DataTypeControl(liste1)
    liste2 = DataTypeControl(liste2)

    işlem = input("yapmak istediğiniz işlemi giriniz(Toplama: 1 Çıkarma: 2 Çarpma: 3 Bölme: 4):\n--> ")
    if işlem.lower() == 'q':
        break
    
    liste1 = BinaryListeyeÇevir(liste1)
    liste2 = BinaryListeyeÇevir(liste2)
    
    l1, l2 = len(liste1), len(liste2)
    if l1 != l2:
        if l1 < l2:
            for i in range(l2-l1):
                liste1.insert(0,0)
        else:
            for i in range(l1-l2):
                liste2.insert(0,0)

    if işlem == '1':
        print(binToplama(liste1,liste2))
    elif işlem == '2':
        print(binÇıkarma(liste1,liste2))
    elif işlem == '3':
        print(binÇarpma(liste1,liste2))
    elif işlem == '4':
        print(binBölme(liste1,liste2))
    else:
        print("Hatalı işlem")