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



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from random import randint

class RandomPickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Random Person Picker')
        self.setGeometry(100, 100, 400, 300)  # Pencere boyutlarını ayarla

        main_layout = QVBoxLayout()

        self.person_count_label = QLabel('Enter the number of people:')
        self.person_count_input = QLineEdit()
        self.person_count_input.returnPressed.connect(self.create_person_inputs)

        self.person_list_label = QLabel('Enter person names:')
        self.person_list_inputs = []
        self.person_inputs_layout = QVBoxLayout()

        self.result_label = QLabel('Lucky person:')
        self.result_display = QLabel()

        self.pick_button = QPushButton('Run')
        self.pick_button.clicked.connect(self.pick_random_person)

        main_layout.addWidget(self.person_count_label)
        main_layout.addWidget(self.person_count_input)
        main_layout.addWidget(self.person_list_label)
        main_layout.addLayout(self.person_inputs_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_display)
        main_layout.addWidget(self.pick_button)

        self.setLayout(main_layout)

    def create_person_inputs(self):
        person_number = int(self.person_count_input.text())

        # Temizleme işlemi
        for i in reversed(range(self.person_inputs_layout.count())):
            widget = self.person_inputs_layout.itemAt(i).widget()
            widget.setParent(None)

        self.person_list_inputs = []

        for i in range(person_number):
            person_input = QLineEdit()
            self.person_inputs_layout.addWidget(person_input)
            self.person_list_inputs.append(person_input)

    def pick_random_person(self):
        person_list = [input_field.text() for input_field in self.person_list_inputs if input_field.text()]
        
        if len(person_list) < 1:
            QMessageBox.warning(self, 'Warning', 'Please enter at least one person.')
            return

        random_number = randint(0, len(person_list) - 1)
        lucky_person = person_list[random_number]
        self.result_display.setText(lucky_person)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPickerApp()
    ex.show()
    sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from random import randint

class RandomPickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Random Person Picker')
        self.setGeometry(100, 100, 400, 300)  # Pencere boyutlarını ayarla

        main_layout = QVBoxLayout()

        # Kişi sayısı girişi için etiket ve giriş kutusu
        self.person_count_label = QLabel('Enter the number of people:')
        self.person_count_input = QLineEdit()
        self.person_count_input.returnPressed.connect(self.create_person_inputs)  # Enter'a basınca kişi girişlerini oluştur

        # Kişi isimlerini girmek için etiket ve düzenleme kutuları düzeni
        self.person_list_label = QLabel('Enter person names:')
        self.person_list_inputs = []  # Kişi isimleri için giriş kutuları listesi
        self.person_inputs_layout = QVBoxLayout()

        # Sonuç gösterimi için etiket
        self.result_label = QLabel('Lucky person:')
        self.result_display = QLabel()

        # Rastgele kişi seçmek için düğme
        self.pick_button = QPushButton('Run')
        self.pick_button.clicked.connect(self.pick_random_person)  # Run düğmesine tıklandığında rastgele kişiyi seç

        # Ana düzeni oluştur
        main_layout.addWidget(self.person_count_label)
        main_layout.addWidget(self.person_count_input)
        main_layout.addWidget(self.person_list_label)
        main_layout.addLayout(self.person_inputs_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_display)
        main_layout.addWidget(self.pick_button)

        self.setLayout(main_layout)

    def create_person_inputs(self):
        person_number = int(self.person_count_input.text())  # Kullanıcı tarafından girilen kişi sayısını al

        # Önceki kişi giriş kutularını temizle
        for i in reversed(range(self.person_inputs_layout.count())):
            widget = self.person_inputs_layout.itemAt(i).widget()
            widget.setParent(None)

        self.person_list_inputs = []  # Yeni kişi giriş kutuları için liste

        # Kişi sayısı kadar düzenleme kutusu oluştur
        for i in range(person_number):
            person_input = QLineEdit()
            self.person_inputs_layout.addWidget(person_input)  # Giriş kutusunu düzenlemeye ekle
            self.person_list_inputs.append(person_input)  # Giriş kutusunu listeye ekle

            # Enter tuşu için sinyal bağlantısı ekle
            person_input.returnPressed.connect(self.pick_random_person)

    def pick_random_person(self):
        person_list = [input_field.text() for input_field in self.person_list_inputs if input_field.text()]  # Boş olmayan kişi isimlerini al
        
        if len(person_list) < 1:
            QMessageBox.warning(self, 'Warning', 'Please enter at least one person.')
            return

        random_number = randint(0, len(person_list) - 1)
        lucky_person = person_list[random_number]
        self.result_display.setText(lucky_person)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPickerApp()
    ex.show()
    sys.exit(app.exec_())

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from random import randint

class RandomPickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Random Person Picker')
        self.setGeometry(100, 100, 400, 300)  # Pencere boyutlarını ayarla

        main_layout = QVBoxLayout()

        self.person_count_label = QLabel('Enter the number of people:')
        self.person_count_input = QLineEdit()
        self.person_count_input.returnPressed.connect(self.create_person_inputs)

        self.person_list_label = QLabel('Enter person names:')
        self.person_list_inputs = []
        self.person_inputs_layout = QVBoxLayout()

        self.result_label = QLabel('Lucky person:')
        self.result_display = QLabel()

        self.pick_button = QPushButton('Run')
        self.pick_button.clicked.connect(self.pick_random_person)

        main_layout.addWidget(self.person_count_label)
        main_layout.addWidget(self.person_count_input)
        main_layout.addWidget(self.person_list_label)
        main_layout.addLayout(self.person_inputs_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_display)
        main_layout.addWidget(self.pick_button)

        self.setLayout(main_layout)

    def create_person_inputs(self):
        person_number = int(self.person_count_input.text())

        # Temizleme işlemi
        for i in reversed(range(self.person_inputs_layout.count())):
            widget = self.person_inputs_layout.itemAt(i).widget()
            widget.setParent(None)

        self.person_list_inputs = []

        for i in range(person_number):
            person_input = QLineEdit()
            self.person_inputs_layout.addWidget(person_input)
            self.person_list_inputs.append(person_input)

    def pick_random_person(self):
        person_list = [input_field.text() for input_field in self.person_list_inputs if input_field.text()]
        
        if len(person_list) < 1:
            QMessageBox.warning(self, 'Warning', 'Please enter at least one person.')
            return

        random_number = randint(0, len(person_list) - 1)
        lucky_person = person_list[random_number]
        self.result_display.setText(lucky_person)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPickerApp()
    ex.show()
    sys.exit(app.exec_())