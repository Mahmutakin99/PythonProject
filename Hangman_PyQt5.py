import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from random import choice

class WordGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Adam Asmaca')
        self.setGeometry(100, 100, 800, 400)

        # Oyun kelimeleri ve zorluk seviyeleri
        self.kelimeler = {
    'Kolay': [
        'Elma', 'Kedi', 'Göl', 'Çiçek', 'Kalem', 'Deniz', 'Ağaç', 'Yıldız', 'Müzik', 'Saat',
        'Kahve', 'Masa', 'Sandalye', 'Telefon', 'Şapka', 'Cam', 'Tabak', 'Çanta', 'Ayakkabı', 'Bebek',
        'Kuş', 'Balık', 'Göl', 'Nehir', 'Çocuk', 'Kar', 'Güneş', 'Kavun', 'Kiraz', 'Çilek',
        'Muz', 'Üzüm', 'Armut', 'Ev', 'Park', 'Bahçe', 'Elma', 'Kum', 'Bulut', 'Boya',
        'Ekmek', 'Peynir', 'Zeytin', 'Domates', 'Salatalık', 'Biber', 'Patates', 'Havuç', 'Soğan', 'Nane'
    ],
    'Orta': [
        'Bilgisayar', 'Çanta', 'Pantolon', 'Ceket', 'Gözlük', 'Lamba', 'Harita', 'Bina', 'Köprü', 'Tren',
        'Araba', 'Bisiklet', 'Uçak', 'Balon', 'Cadde', 'Yatak', 'Oda', 'Salon', 'Koridor', 'Çerçeve',
        'Anahtar', 'Meyve', 'Sebze', 'Çikolata', 'Dondurma', 'Pasta', 'Ekmek', 'Peynir', 'Zeytin', 'Mandalina',
        'Karpuz', 'Kavun', 'Salatalık', 'Biber', 'Patates', 'Havuç', 'Soğan', 'Sarımsak', 'Maydanoz', 'Dereotu'
    ],
    'Zor': [
        'Galatasaray', 'Bilgisayar', 'Televizyon', 'Kütüphane', 'Fenerbahçe', 'Müze', 'Eczane', 'Şehir',
        'Otobüs', 'Kütüphane', 'Tiyatro', 'Yıldız', 'Müzikal', 'Deniz Feneri', 'Rota', 'Kalem Kutusu', 'Silgi', 'Fırça',
        'Tuval', 'Mutfak', 'Banyo', 'Kalem Kutusu', 'Silgi', 'Fırça', 'Rota', 'Harita', 'Kütüphane', 'Yüksek Hızlı Tren'
    ]
}
        
        self.ascii_stages = [
            """
                +---+
                    |
                    |
                    |
                   ===
            """,
            """
                +---+
                O   |
                    |
                    |
                   ===
            """,
            """
                +---+
                O   |
                |   |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|   |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
                   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
               /   ===
            """,
            """
                +---+
                O   |
               /|\  |
                |   |
               / \ ===
            """
        ]

        # Başlangıçta zoruk seviyesi ve ipucu ayarları
        self.zorluk_seviyesi = 'Kolay'
        self.ipucu_aktif = False

        self.kelime = ''
        self.tahmin = []
        self.hak = 6

        self.düzen = QHBoxLayout()
        self.sol_düzen = QVBoxLayout()

        self.kelime_etiket = QLabel(' '.join(self.tahmin), self)
        self.kelime_etiket.setFont(QFont('Arial', 24))
        self.sol_düzen.addWidget(self.kelime_etiket)

        self.hak_etiket = QLabel(f'Kalan Hakkınız: {self.hak}', self)
        self.hak_etiket.setFont(QFont('Arial', 14))
        self.sol_düzen.addWidget(self.hak_etiket)

        # Zorluk seviyesi seçim kutusu
        self.zorluk_seviyesi_kutusu = QComboBox(self)
        self.zorluk_seviyesi_kutusu.addItems(['Kolay', 'Orta', 'Zor'])
        self.zorluk_seviyesi_kutusu.setCurrentText(self.zorluk_seviyesi)
        self.zorluk_seviyesi_kutusu.currentTextChanged.connect(self.zorluk_seviyesi_degistir)
        self.sol_düzen.addWidget(self.zorluk_seviyesi_kutusu)

        # İpucu butonu
        self.ipucu_butonu = QPushButton('İpucu Al', self)
        self.ipucu_butonu.clicked.connect(self.ipucu_al)
        self.sol_düzen.addWidget(self.ipucu_butonu)

        # Harf tahmini için giriş alanı ve buton
        self.harf_girişi = QLineEdit(self)
        self.harf_girişi.setPlaceholderText('Harf giriniz...')
        self.sol_düzen.addWidget(self.harf_girişi)

        self.harf_tahmin_butonu = QPushButton('Harf Tahmini', self)
        self.harf_tahmin_butonu.clicked.connect(self.harf_tahmini)
        self.sol_düzen.addWidget(self.harf_tahmin_butonu)

        # Kelime tahmini için giriş alanı ve buton
        self.kelime_girişi = QLineEdit(self)
        self.kelime_girişi.setPlaceholderText('Kelimeyi tahmin ediniz...')
        self.sol_düzen.addWidget(self.kelime_girişi)

        self.kelime_tahmin_butonu = QPushButton('Kelime Tahmini', self)
        self.kelime_tahmin_butonu.clicked.connect(self.kelime_tahmini)
        self.sol_düzen.addWidget(self.kelime_tahmin_butonu)

        # Yeni oyun ve çıkış butonları
        self.buton_düzeni = QHBoxLayout()

        self.yeni_oyun_butonu = QPushButton('Yeni Oyun', self)
        self.yeni_oyun_butonu.clicked.connect(self.yeni_oyun)
        self.buton_düzeni.addWidget(self.yeni_oyun_butonu)

        self.çıkış_butonu = QPushButton('Çıkış', self)
        self.çıkış_butonu.clicked.connect(self.close)
        self.buton_düzeni.addWidget(self.çıkış_butonu)

        self.sol_düzen.addLayout(self.buton_düzeni)

        self.ascii_etiket = QLabel(self)
        self.ascii_etiket.setFont(QFont('Courier', 18))
        self.ascii_etiket.setText(self.ascii_stages[0])

        self.düzen.addLayout(self.sol_düzen)
        self.düzen.addWidget(self.ascii_etiket)
        
        self.setLayout(self.düzen)
        self.yeni_oyun()

    def zorluk_seviyesi_degistir(self, yeni_seviye):
        self.zorluk_seviyesi = yeni_seviye
        self.yeni_oyun()

    def ipucu_al(self):
        if self.ipucu_aktif:
            QMessageBox.information(self, 'İpucu', 'İpucu zaten kullanıldı.')
            return

        for i, karakter in enumerate(self.kelime):
            if self.tahmin[i] == '_':
                self.tahmin[i] = karakter
                break

        self.kelime_etiket.setText(' '.join(self.tahmin))
        self.ipucu_aktif = True

        if '_' not in self.tahmin:
            self.oyun_sonu(True)
        else:
            QMessageBox.information(self, 'İpucu', f'İpucu: {karakter} harfini buldunuz!')

    def harf_tahmini(self):
        harf = self.harf_girişi.text().upper()
        self.harf_girişi.clear()

        if len(harf) != 1 or not harf.isalpha():
            QMessageBox.warning(self, 'Hata', 'Lütfen geçerli bir harf girin.')
            return

        if harf in self.kelime:
            if harf in self.tahmin:
                QMessageBox.warning(self, 'Hata', 'Bu harfi zaten tahmin ettiniz.')
                return

            for i, karakter in enumerate(self.kelime):
                if karakter == harf:
                    self.tahmin[i] = harf

            self.kelime_etiket.setText(' '.join(self.tahmin))

            if '_' not in self.tahmin:
                self.oyun_sonu(True)
        else:
            self.hak -= 1
            self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
            self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

            if self.hak == 0:
                self.oyun_sonu(False)

    def kelime_tahmini(self):
        kelime = self.kelime_girişi.text().upper()
        self.kelime_girişi.clear()

        if kelime == self.kelime:
            self.tahmin = list(self.kelime)
            self.kelime_etiket.setText(' '.join(self.tahmin))
            self.oyun_sonu(True)
        else:
            self.hak -= 1
            self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
            self.ascii_etiket.setText(self.ascii_stages[6 - self.hak])

            if self.hak == 0:
                self.oyun_sonu(False)

    def oyun_sonu(self, kazandi):
        if kazandi:
            QMessageBox.information(self, 'Tebrikler', f'Tebrikler, kelimeyi buldunuz: {self.kelime}')
        else:
            QMessageBox.warning(self, 'Kaybettiniz', f'Hakkınız bitti, kelime: {self.kelime}')
        self.yeni_oyun()

    def yeni_oyun(self):
        self.kelime = choice(self.kelimeler[self.zorluk_seviyesi]).upper()
        self.tahmin = ['_'] * len(self.kelime)
        self.hak = 6
        self.ipucu_aktif = False
        self.kelime_etiket.setText(' '.join(self.tahmin))
        self.hak_etiket.setText(f'Kalan Hakkınız: {self.hak}')
        self.ascii_etiket.setText(self.ascii_stages[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    oyun = WordGuessingGame()
    oyun.show()
    sys.exit(app.exec_())
