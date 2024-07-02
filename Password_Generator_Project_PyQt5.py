import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from random import choice, shuffle

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Şifre Oluşturucu')

        # Dil seçimi
        self.lang_label = QLabel('Klavye dili:')
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(['English', 'Turkish', 'German', 'French', 'Russian', 'Korean', 'Japanese'])

        # Harf sayısı
        self.letters_label = QLabel('Harf sayısı:')
        self.letters_input = QLineEdit()

        # Rakam sayısı
        self.numbers_label = QLabel('Rakam sayısı:')
        self.numbers_input = QLineEdit()

        # Sembol sayısı
        self.symbols_label = QLabel('Sembol sayısı:')
        self.symbols_input = QLineEdit()

        # Sonuç
        self.result_label = QLabel('Oluşturulan şifre:')
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)

        # Butonlar
        self.generate_button = QPushButton('Şifre Oluştur')
        self.generate_button.clicked.connect(self.generate_password)

        self.exit_button = QPushButton('Çıkış')
        self.exit_button.clicked.connect(self.close_application)

        # Layout
        vbox = QVBoxLayout()

        lang_layout = QHBoxLayout()
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)

        letters_layout = QHBoxLayout()
        letters_layout.addWidget(self.letters_label)
        letters_layout.addWidget(self.letters_input)

        numbers_layout = QHBoxLayout()
        numbers_layout.addWidget(self.numbers_label)
        numbers_layout.addWidget(self.numbers_input)

        symbols_layout = QHBoxLayout()
        symbols_layout.addWidget(self.symbols_label)
        symbols_layout.addWidget(self.symbols_input)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_display)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.generate_button)
        buttons_layout.addWidget(self.exit_button)

        vbox.addLayout(lang_layout)
        vbox.addLayout(letters_layout)
        vbox.addLayout(numbers_layout)
        vbox.addLayout(symbols_layout)
        vbox.addLayout(result_layout)
        vbox.addLayout(buttons_layout)

        self.setLayout(vbox)

    def generate_password(self):
        eng_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tr_letters = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
        ger_letters = 'abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜẞ'
        fr_letters = 'abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüÿABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÇÉÈËÎÏÔÙÛÜŸ'
        ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        ko_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ'
        ja_letters = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんガギグゲゴザジズゼゾダヂヅデドバビブベボパ'

        numbers = '0123456789'
        symbols = '!#$%&()*+'

        letters = ''
        lang = self.lang_combo.currentText()
        if lang == 'English':
            letters = eng_letters
        elif lang == 'Turkish':
            letters = tr_letters
        elif lang == 'German':
            letters = ger_letters
        elif lang == 'French':
            letters = fr_letters
        elif lang == 'Russian':
            letters = ru_letters
        elif lang == 'Korean':
            letters = ko_letters
        elif lang == 'Japanese':
            letters = ja_letters

        password_list = []

        try:
            nr_letters = int(self.letters_input.text())
            nr_numbers = int(self.numbers_input.text())
            nr_symbols = int(self.symbols_input.text())

            for _ in range(nr_letters):
                password_list.append(choice(letters))
            for _ in range(nr_numbers):
                password_list.append(choice(numbers))
            for _ in range(nr_symbols):
                password_list.append(choice(symbols))

            shuffle(password_list)

            password = ''.join(password_list)
            self.result_display.setText(password)
        except ValueError:
            QMessageBox.warning(self, 'Hata', 'Lütfen geçerli sayılar girin!')

    def close_application(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())