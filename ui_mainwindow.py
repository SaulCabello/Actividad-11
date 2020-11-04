################################################################################
## Form generated from reading UI file 'particula.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(608, 407)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.red_spinBox, 6, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_2.addWidget(self.agregar_final_pushButton, 11, 0, 1, 4)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 10, 0, 1, 4)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_x_spinBox, 1, 2, 1, 2)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.green_spinBox, 8, 2, 1, 2)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_y_spinBox, 2, 2, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 9, 1, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout_2.addWidget(self.velocidad_lineEdit, 5, 2, 1, 2)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_x_spinBox, 3, 2, 1, 2)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_2.addWidget(self.id_lineEdit, 0, 2, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 12, 0, 1, 4)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 8, 1, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_y_spinBox, 4, 2, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.blue_spinBox, 9, 2, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.print = QPlainTextEdit(self.centralwidget)
        self.print.setObjectName(u"print")

        self.gridLayout.addWidget(self.print, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color(rgb):", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi