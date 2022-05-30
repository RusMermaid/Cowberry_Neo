import Functions.ui

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #MainWindow - основное окно
        MainWindow.resize(796, 340) #изначальный размер окна
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) #установка курсора при наведении на окно приложения
        self.centralwidget = QtWidgets.QWidget(MainWindow) #centralwidget - основа для кнопок
        self.centralwidget.setObjectName("centralwidget") #присвоение centralWidget имени centralwidget
        self.code_btn = QtWidgets.QPushButton(self.centralwidget) #кнопка "Кодировать"
        self.code_btn.setGeometry(QtCore.QRect(10, 20, 121, 41)) #размеры кнопки "Кодировать"
        font = QtGui.QFont() #создание шрифта (везде он будет одинаковый)
        font.setFamily("Times New Roman") #используется Times New Roman
        font.setPointSize(14) #размер шрифта - 14
        self.code_btn.setFont(font) #установка шрифта для кнопки "Кодировать"
        self.code_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #установка курсора, показывающего \
        # возможность нажатия на кнопку "Кодировать"
        self.code_btn.setObjectName("code_btn") #название кнопки "Кодировать" - code_btn
        self.input_box = QtWidgets.QLineEdit(self.centralwidget) #создание input_box - в это окно будет записываться \
        # текст для кодирования
        self.input_box.setGeometry(QtCore.QRect(140, 20, 641, 41)) #размер поля ввода
        self.input_box.setFont(font) #шрифт в поле ввода
        self.input_box.setObjectName("input_box") #название объекта поля ввода
        self.return_label = QtWidgets.QLabel(self.centralwidget) #создание поля вывода сообщения об успешном кодировании
        self.return_label.setGeometry(QtCore.QRect(10, 70, 771, 31)) #размер поля вывода сообщения \
        #об успешном кодировании
        self.return_label.setFont(font) #установка шрифта в поле вывода сообщения об успешном кодировании
        self.return_label.setText("") #изначально текста в поле вывода нет
        self.return_label.setObjectName("return_label") #название объекта поля вывода
        self.decode_btn = QtWidgets.QPushButton(self.centralwidget) #создание кнопки "Декодировать"
        self.decode_btn.setGeometry(QtCore.QRect(10, 130, 121, 41)) #размер кнопки "Декодировать"
        self.decode_btn.setFont(font) #установка шрифта для кнопки "Декодировать"
        self.decode_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #установка курсора, показывающего \
        # возможность нажатия на кнопку "Декодировать"
        self.decode_btn.setObjectName("decode_btn") #присвоение имени объекту кнопки "Декодировать"
        self.img_input_box = QtWidgets.QLineEdit(self.centralwidget) #создание поля ввода для пути изображения
        self.img_input_box.setGeometry(QtCore.QRect(140, 130, 641, 41)) #размер поля ввода пути сообщения
        self.img_input_box.setFont(font) #установка шрифта для данного поля
        self.img_input_box.setObjectName("img_input_box") #название объекта данного поля
        self.decoded_text_box = QtWidgets.QTextEdit(self.centralwidget) #создание поля для вывода раскодированного изображения
        self.decoded_text_box.setGeometry(QtCore.QRect(140, 180, 641, 151)) #размер данного поля
        self.decoded_text_box.setReadOnly(True) #поле вывода раскодированного текста нельзя редактировать
        self.decoded_text_box.setFont(font) #установка шрифта для поля вывода
        self.decoded_text_box.setObjectName("decoded_text_box") #название объекта поля вывода
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget) #создание кнопки "Очистить"
        self.clear_btn.setGeometry(QtCore.QRect(10, 180, 121, 41)) #размер копки "Очистить"
        self.clear_btn.setFont(font) #установка шрифта в кнопке "Очистить"
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #установка курсора, показывающего \
        # возможность нажатия на кнопку "Очистить"
        self.clear_btn.setObjectName("clear_btn") #название объекта кнопки "Очистить"
        MainWindow.setCentralWidget(self.centralwidget) #Mainwindow - это centralwidget

        self.code_btn.clicked.connect(lambda: Functions.ui.coding(self.input_box.text(), self.return_label))
        #прием значений при нажатии на кнопку "Кодировать"

        self.decode_btn.clicked.connect(lambda: Functions.ui.decoding(self.img_input_box.text(), self.decoded_text_box))
        #прием значений при нажатии на кнопку "Декодировать"

        self.clear_btn.clicked.connect(lambda: Functions.ui.clear(self.input_box, self.decoded_text_box, self.img_input_box, self.return_label))
        # прием значений при нажатии на кнопку "Очистить"

        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): #Отображение интерфейса
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cowberry"))
        MainWindow.setWindowIcon(QtGui.QIcon('CowBerry.png'))
        self.code_btn.setText(_translate("MainWindow", "Кодировать"))
        self.decode_btn.setText(_translate("MainWindow", "Декодировать"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))


if __name__ == "__main__": #запуск окна
    try: #для Mac/Linux
        from PyQt5.QtWinExtras import QtWin

        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
    except ImportError:
        pass
    import sys
    app = QtWidgets.QApplication(sys.argv) #создание переменной app
    app.setWindowIcon(QtGui.QIcon('CowBerry.png')) #установка иконки программы
    MainWindow = QtWidgets.QMainWindow() #присвоение значения MainWindow
    MainWindow.setWindowIcon(QtGui.QIcon('CowBerry.png')) #отображение иконки в приложении
    ui = Ui_MainWindow() #создание интерфейса
    ui.setupUi(MainWindow) #подключение интерфейса
    MainWindow.show() #отображение Mainwindow
    sys.exit(app.exec_()) #Выход из приложения при закрытии программы
