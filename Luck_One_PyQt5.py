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