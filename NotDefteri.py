import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QFontDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.create_menus()

        self.setWindowTitle('Basit Not Defteri')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def create_menus(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('Dosya')
        edit_menu = menubar.addMenu('Düzen')

        open_action = QAction('Aç', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        save_action = QAction('Kaydet', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        font_action = QAction('Yazı Tipi', self)
        font_action.triggered.connect(self.change_font)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        edit_menu.addAction(font_action)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Dosya Aç', '.', 'Metin Dosyaları (*.txt)')
        if filename:
            with open(filename, 'r') as file:
                self.text_edit.setText(file.read())

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Dosya Kaydet', '.', 'Metin Dosyaları (*.txt)')
        if filename:
            with open(filename, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())