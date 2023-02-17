from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super(Window. self).__init__()






def add_lable():
    print ("good")

def application():
    app = QApplication(sys.argv)  #Создание приложения в целом
    window = QMainWindow()   #Создание окна приложения

    window.setWindowTitle("Простая программа")
    window.setGeometry(300, 250, 350, 200)   #(2хсмещение окна, 2хразмер окна)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Базовая надпись")
    main_text.move(100, 100)
    main_text.adjustSize()   #Подстройка ширины объекта под содержимое

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Нажми на меня")
    btn.setFixedWidth(200)  #Ширина кнопки  
    btn.clicked.connect(add_lable)  #Вызов функции при нажатии на кнопку


    window.show()          #Демонстрация окна

    sys.exit(app.exec_())    #Корректное заврешение


if __name__ == "__main__": #Если запускается этот файл, как основной, то вызывается метод application                                      
    application()