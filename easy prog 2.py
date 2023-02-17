from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа") #Обращаемся к self, тк он находится в классе родителе
        self.setGeometry(300, 250, 350, 200)   #(2хсмещение окна, 2хразмер окна)

        self.new_text = QtWidgets.QLabel(self)  #Создание пустого объекта(надпись), принадлежащего окну


        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Базовая надпись")  #Переменная, которая принадлежит классу self
        self.main_text.move(100, 100)
        self.main_text.adjustSize()   #Подстройка ширины объекта под содержимое

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)  #Ширина кнопки  
        self.btn.clicked.connect(self.add_lable)  #Вызов функции при нажатии на кнопку #Метод add_lable тоже отностися к классу self

    def add_lable(self):  #Параметр self нужно передавать в любой метод внутри какого-либо класса
        self.new_text.setText("Вторая надпись")  #На объекте new_text надпись
        self.new_text.move(100,50)   #Расположение объекта(надписи)
        self.new_text.adjustSize()   #Подогнать объект под размер надписи

def application():
    app = QApplication(sys.argv)  #Создание приложения в целом
    window = Window()   #Создание окна приложения #Создание объекта на основе созданного класса Window



    window.show()          #Демонстрация окна

    sys.exit(app.exec_())    #Корректное заврешение


if __name__ == "__main__": #Если запускается этот файл, как основной, то вызывается метод application                                      
    application()