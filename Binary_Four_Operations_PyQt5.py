from PyQt5 import QtWidgets, QtGui, QtCore
import sys

# Decimal ve Binary dönüşüm fonksiyonları
def dec(binary_list):
    return int(''.join(str(bit) for bit in binary_list), 2)

def bin(decimal):
    return [int(bit) for bit in format(decimal, 'b')]

def data_type_control(x):
    if all(char in '01' for char in x):
        return x
    else:
        return "I think something's wrong"

def bin_toplama(liste1, liste2):
    liste1.reverse()
    liste2.reverse()
    elde = 0
    sonuc = []
    for i in range(max(len(liste1), len(liste2))):
        bit1 = liste1[i] if i < len(liste1) else 0
        bit2 = liste2[i] if i < len(liste2) else 0
        toplam = bit1 + bit2 + elde
        sonuc.append(toplam % 2)
        elde = 1 if toplam >= 2 else 0
    if elde:
        sonuc.append(1)
    sonuc.reverse()
    return sonuc

def bin_cikarma(liste1, liste2):
    a = [1] + [0] * (len(liste1) - 1)
    liste3 = liste2[::-1]
    liste4 = bin_toplama(liste3, a)
    liste5 = bin_toplama(liste1, liste4)
    while len(liste5) > len(liste1):
        liste5.pop(0)
    return liste5

def bin_carpma(liste1, liste2):
    i, j = dec(liste1), dec(liste2)
    return bin(i * j)

def bin_bolme(liste1, liste2):
    i, j = dec(liste1), dec(liste2)
    return bin(i // j)

def binary_listeye_cevir(liste):
    return [int(i) for i in liste]

# PyQt5 arayüzü
class BinaryCalculatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Binary Calculator')
        self.setGeometry(100, 100, 600, 500)

        # Main layout
        layout = QtWidgets.QVBoxLayout()

        # Title
        title = QtWidgets.QLabel("Binary Calculator", self)
        title.setFont(QtGui.QFont('Arial', 20, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # Input fields
        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setPlaceholderText("Binary value 1")
        self.input1.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(self.input1)

        self.input2 = QtWidgets.QLineEdit(self)
        self.input2.setPlaceholderText("Binary value 2")
        self.input2.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(self.input2)

        # Operation selection
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setFont(QtGui.QFont('Arial', 12))
        self.comboBox.addItem("Addition", "1")
        self.comboBox.addItem("Subtraction", "2")
        self.comboBox.addItem("Multiplication", "3")
        self.comboBox.addItem("Division", "4")
        layout.addWidget(self.comboBox)

        # Buttons
        self.calculateButton = QtWidgets.QPushButton('Calculate', self)
        self.calculateButton.setFont(QtGui.QFont('Arial', 12))
        self.calculateButton.clicked.connect(self.calculate)
        layout.addWidget(self.calculateButton)

        self.exitButton = QtWidgets.QPushButton('Exit', self)
        self.exitButton.setFont(QtGui.QFont('Arial', 12))
        self.exitButton.clicked.connect(QtWidgets.qApp.quit)
        layout.addWidget(self.exitButton)

        # Output field
        self.resultTextEdit = QtWidgets.QTextEdit(self)
        self.resultTextEdit.setFont(QtGui.QFont('Arial', 12))
        self.resultTextEdit.setReadOnly(True)
        layout.addWidget(self.resultTextEdit)

        self.setLayout(layout)
    
    def calculate(self):
        liste1 = self.input1.text()
        liste2 = self.input2.text()

        if data_type_control(liste1) == "I think something's wrong" or data_type_control(liste2) == "I think something's wrong":
            self.resultTextEdit.setText("Invalid input")
            return

        liste1 = binary_listeye_cevir(liste1)
        liste2 = binary_listeye_cevir(liste2)
        
        l1, l2 = len(liste1), len(liste2)
        if l1 != l2:
            if l1 < l2:
                for _ in range(l2-l1):
                    liste1.insert(0, 0)
            else:
                for _ in range(l1-l2):
                    liste2.insert(0, 0)

        operation = self.comboBox.currentData()
        if operation == '1':
            result = bin_toplama(liste1, liste2)
        elif operation == '2':
            result = bin_cikarma(liste1, liste2)
        elif operation == '3':
            result = bin_carpma(liste1, liste2)
        elif operation == '4':
            result = bin_bolme(liste1, liste2)
        else:
            result = "Invalid operation"

        self.resultTextEdit.setText(''.join(map(str, result)))
        self.input1.clear()
        self.input2.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    calculatorApp = BinaryCalculatorApp()
    calculatorApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()