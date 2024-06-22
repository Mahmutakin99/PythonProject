import random
import time
print("**************************\nSayı Tahmin Oyunu\n**************************")
rastgele_sayı=random.randint(1,100)
tahmin_hakkı=10
while True:
    tahmin=int(input("tahmininiz: "))
    if(tahmin<rastgele_sayı):
        time.sleep(0.3)
        print("biraz büyük bir sayı söyleyin...")
        tahmin_hakkı-=1
    elif(tahmin>rastgele_sayı):
        time.sleep(0.3)
        print("biraz küçük bir sayı söyleyin...")
        tahmin_hakkı-=1
    else:
        time.sleep(0.3)
        print("tebikler bildiniz sayımız: ",rastgele_sayı)
        break
    if(tahmin_hakkı==0):
        time.sleep(0.3)
        print("tahmin hakkınız bitmiştir yeni oyuna geçiniz:")
        break
