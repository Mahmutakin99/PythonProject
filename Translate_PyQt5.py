from PyQt5 import QtWidgets, QtGui, QtCore
from googletrans import Translator
import sys

class TranslatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Çeviri Uygulaması')
        self.setGeometry(100, 100, 600, 500)

        # Main layout
        layout = QtWidgets.QVBoxLayout()

        # Title
        title = QtWidgets.QLabel("Çeviri Uygulaması", self)
        title.setFont(QtGui.QFont('Arial', 20, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # Input text
        input_layout = QtWidgets.QVBoxLayout()
        input_label = QtWidgets.QLabel("Çevirmek İstediğiniz Metni Girin:", self)
        input_label.setFont(QtGui.QFont('Arial', 12))
        input_layout.addWidget(input_label)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setPlaceholderText("Metni buraya girin...")
        self.textEdit.setFont(QtGui.QFont('Arial', 12))
        input_layout.addWidget(self.textEdit)

        layout.addLayout(input_layout)

        # Language selection
        langLayout = QtWidgets.QHBoxLayout()
        langLabel = QtWidgets.QLabel("Hedef Dil: ", self)
        langLabel.setFont(QtGui.QFont('Arial', 12))
        langLayout.addWidget(langLabel)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setFont(QtGui.QFont('Arial', 12))
        self.comboBox.addItem("Türkçe", "tr")
        self.comboBox.addItem("İngilizce", "en")
        self.comboBox.addItem("Almanca", "de")
        self.comboBox.addItem("İspanyolca", "es")
        self.comboBox.addItem("Japonca", "ja")
        self.comboBox.addItem("Fransızca", "fr")
        self.comboBox.addItem("Rusça", "ru")
        langLayout.addWidget(self.comboBox)

        layout.addLayout(langLayout)

        # Translate button
        self.translateButton = QtWidgets.QPushButton('Çevir', self)
        self.translateButton.setFont(QtGui.QFont('Arial', 12))
        self.translateButton.clicked.connect(self.translateText)
        layout.addWidget(self.translateButton)
        
        self.exitButton = QtWidgets.QPushButton('Çıkış', self)
        self.exitButton.setFont(QtGui.QFont('Arial', 12))
        self.exitButton.clicked.connect(QtWidgets.qApp.quit)
        layout.addWidget(self.exitButton)

        # Output text
        output_layout = QtWidgets.QVBoxLayout()
        output_label = QtWidgets.QLabel("Çevrilen Metin:", self)
        output_label.setFont(QtGui.QFont('Arial', 12))
        output_layout.addWidget(output_label)

        self.resultTextEdit = QtWidgets.QTextEdit(self)
        self.resultTextEdit.setFont(QtGui.QFont('Arial', 12))
        self.resultTextEdit.setReadOnly(True)
        output_layout.addWidget(self.resultTextEdit)

        layout.addLayout(output_layout)

        self.setLayout(layout)
    
    def translateText(self):
        text = self.textEdit.toPlainText()
        targetLang = self.comboBox.currentData()
        
        if text.strip() == "":
            self.resultTextEdit.setText("Çevrilecek metni giriniz.")
            return
        
        translator = Translator()
        translation = translator.translate(text, dest=targetLang)
        self.resultTextEdit.setText(translation.text)
        self.textEdit.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    translatorApp = TranslatorApp()
    translatorApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()