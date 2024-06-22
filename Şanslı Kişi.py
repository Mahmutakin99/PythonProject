'''
from random import randint
while True:
    person_list=[]
    i=0
    choice = int(input("1 to start/continue processing Press 0 to stop/finish.\nProcess selection: "))
    if(choice == 0):
        choice2 = input("You have chosen to stop the transaction, should the transaction be executed? 'yes' or 'no' ")
        if(choice2 == 'yes'):
            break
        else:
            continue
    while True:
        person_number = int(input("\nEnter the number of people: "))
        if person_number <= 1:
            if person_number == 1:
                person = input(f"{i+1}. Enter the person: ")
                print("\nLucky person is: ", person)
                print("\n*******************************")
                break
            else:
                print("Please enter valid number of individuals.")
                print("\n*******************************")
                continue
        while(i< person_number):
            random_number = randint(1, person_number)
            person = input(f"{i+1}. Enter the person: ")
            person_list.append(person)
            i+=1
        print("\nLucky person is: ", person_list[random_number - 1])
        print("\n*******************************")
        break
'''
from random import randint
while True:
    kişi_liste=[]
    i=0
    secim=int(input("işleme başlamak/devam etmek için 1 durmak/bitirmek için 0 a basınız.\nİşlem seçimi: "))
    if(secim==0):
        secim2=input("işlem durdurmayı seçtiniz işlem yapılsın mı? 'evet' yada 'hayır' ")
        if(secim2=='evet'):
            break
        else:
            continue
    while True:
        s=int(input("\nkişi sayısını giriniz: "))
        if s<=1:
            if s==1:
                kişi=input(f"{i+1}. kişiyi giriniz: ")
                print("\nşanslı kişi: ",kişi)
                print("\n*******************************")
                break
            else:
                print("Lütfen geçerli sayıda birey giriniz.")
                print("\n*******************************")
                continue
        while(i<s):
            rastgele_sayı=randint(1,s)
            kişi=input(f"{i+1}. kişiyi giriniz: ")
            kişi_liste.append(kişi)
            i+=1
        print("\nşanslı kişi: ",kişi_liste[rastgele_sayı - 1])
        print("\n*******************************")
        break