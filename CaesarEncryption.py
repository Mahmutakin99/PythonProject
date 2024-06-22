import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QSpinBox, QHBoxLayout

def caesar_cipher(choice, text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_list = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if choice == 'encode':
                new_position = (position + shift) % len(alphabet)
            elif choice == 'decode':
                new_position = (position - shift) % len(alphabet)
            new_letter = alphabet[new_position]
            letter_list += new_letter
        else:
            letter_list += letter  # Insert non-letter characters as they are
    return letter_list

class CaesarCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caesar Encryption')
        
        # Adjust window sizes
        self.resize(400, 700)  # Fixed dimension
        #self.setFixedSize(800, 600)  # Fixed dimensions (cannot be changed)
        # Alternatively you can set minimum and maximum sizes:
        self.setMinimumSize(400, 700)
        self.setMaximumSize(1920, 1080)

        # Set background image
        #self.setStyleSheet("""
        #    QWidget {
        #        background-image: url('background.png');
        #        background-repeat: no-repeat;
        #        background-position: center;
        #        background-size: cover;
        #    }
        #""")

        layout = QVBoxLayout()

        self.choice_label = QLabel('Choice your transaction:')
        self.choice_combo = QComboBox()
        self.choice_combo.addItem('encode')
        self.choice_combo.addItem('decode')

        self.text_label = QLabel('Write your message:')
        self.text_input = QTextEdit()
        #self.text_input.setStyleSheet("""
        #    QTextEdit {
        #        background-image: url('background.png');
        #        background-repeat: no-repeat;
        #        background-position: center;
        #        background-attachment: fixed;
        #        border: 1px solid black;
        #    }
        #""")

        self.shift_label = QLabel('Enter shift number:')
        self.shift_input = QSpinBox()
        self.shift_input.setRange(1, 28)

        self.result_label = QLabel('Result:')
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        #self.result_output.setStyleSheet("""
        #    QTextEdit {
        #        background-image: url('background.png');
        #        background-repeat: no-repeat;
        #        background-position: center;
        #        background-attachment: fixed;
        #        border: 1px solid black;
        #    }
        #""")

        self.run_button = QPushButton('Run')
        self.run_button.clicked.connect(self.run_caesar)

        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.close_application)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.exit_button)

        layout.addWidget(self.choice_label)
        layout.addWidget(self.choice_combo)
        layout.addWidget(self.text_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def run_caesar(self):
        choice = self.choice_combo.currentText()
        text = self.text_input.toPlainText().lower()
        shift = self.shift_input.value()
        result = caesar_cipher(choice, text, shift)
        self.result_output.setText(result)
        self.text_input.clear()  # Clear text input field

    def close_application(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CaesarCipherApp()
    ex.show()
    sys.exit(app.exec_())
