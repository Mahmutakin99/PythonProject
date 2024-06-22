from math import *
print("************************************\n\tHesap makinesi programı\n************************************\n      çıkmak için 'q'ya basınız...")
while True:
    secim=input('''************************************
1)toplama 
2)cıkarma
3)carpma 
4)bölme
5)yuzde alma 
6)üs alma
7)karekok alma 
8)on tabanlı logaritma
9)Ebob/Ekok
yapmak istediğiniz işlemi seciniz:
************************************\n''')
    print("seçilen işlem kodu: ",secim)
    if(secim=='q'):
        print("programdan çıkılıyor...")
        break
    elif(secim=='1'):
        print("Yapacağınız işlem (toplama)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a+b}")
    elif(secim=='2'):
        print("Yapacağınız işlem (çıkarma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a-b}")
    elif(secim=='3'):
        print("Yapacağınız işlem (çarpma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a*b}")
    elif(secim=='4'):
        print("Yapacağınız (işlem bölme)dir:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a/b}")
    elif(secim=='5'):
        print("Yapacağınız işlem (yüzde alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("Yüzde kaç almak istersiniz:"))
        print(f"************************************\nsonuç: {(a*b)/100}")
    elif(secim=='6'):
        print("Yapacağınız işlem (üs alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=int(input("Üs giriniz:"))
        print(f"************************************\nsonuç: {a**b}")
    elif(secim=='7'):
        print("Yapacağınız işlem (karekök alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        print(f"************************************\nsonuç: {a**(0.5)}")
    elif(secim=='8'):
        print("Yapacağınız işlem (on tabanlı logaritma alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        print(f"************************************\nsonuç: {log10(a)}")
    elif(secim=='9'):
        print("Yapacağınız işlem (Ebob/Ekok Alma)dır:")
        a=float(input("işlem yapmak istediğiniz sayıyı giriniz:"))
        b=float(input("işlem yapacağınız diğer sayıyı giriniz:"))
        ebob= ebob(a,b)
        ekok= ekok(a,b)
        print(f"************************************\nEbob: {ebob}\tEkok: {ekok}")
    else:
        print("seçilen işlem kodu hatalıdır:")  