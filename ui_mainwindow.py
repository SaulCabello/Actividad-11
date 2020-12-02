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
        MainWindow.resize(625, 528)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionId_ascendente = QAction(MainWindow)
        self.actionId_ascendente.setObjectName(u"actionId_ascendente")
        self.actionVelocidad_ascendente = QAction(MainWindow)
        self.actionVelocidad_ascendente.setObjectName(u"actionVelocidad_ascendente")
        self.actionDistancia_descendente = QAction(MainWindow)
        self.actionDistancia_descendente.setObjectName(u"actionDistancia_descendente")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_2.addWidget(self.id_lineEdit, 0, 1, 1, 2)

        self.mostrar_grafo_pushButton = QPushButton(self.groupBox)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_grafo_pushButton, 9, 0, 1, 3)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox_3)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.destino_x_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 2, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox_3)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.destino_y_spinBox, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 6, 0, 1, 3)

        self.mostrar_datos_pushButton = QPushButton(self.groupBox)
        self.mostrar_datos_pushButton.setObjectName(u"mostrar_datos_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_datos_pushButton, 8, 0, 1, 3)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout_2.addWidget(self.velocidad_lineEdit, 3, 1, 1, 2)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_2.addWidget(self.agregar_final_pushButton, 7, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox_2)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_y_spinBox, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox_2)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_x_spinBox, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_4)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_4)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.green_spinBox, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_4)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.blue_spinBox, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 4, 0, 1, 3)


        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)

        self.print = QPlainTextEdit(self.tab)
        self.print.setObjectName(u"print")

        self.gridLayout_8.addWidget(self.print, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 2)

        self.tabla_mostrar_pushButton = QPushButton(self.tab_2)
        self.tabla_mostrar_pushButton.setObjectName(u"tabla_mostrar_pushButton")

        self.gridLayout_4.addWidget(self.tabla_mostrar_pushButton, 1, 0, 1, 2)

        self.tabla_id_lineEdit = QLineEdit(self.tab_2)
        self.tabla_id_lineEdit.setObjectName(u"tabla_id_lineEdit")

        self.gridLayout_4.addWidget(self.tabla_id_lineEdit, 2, 0, 1, 1)

        self.tabla_buscar_pushButton = QPushButton(self.tab_2)
        self.tabla_buscar_pushButton.setObjectName(u"tabla_buscar_pushButton")

        self.gridLayout_4.addWidget(self.tabla_buscar_pushButton, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 625, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrden_ascendente = QMenu(self.menubar)
        self.menuOrden_ascendente.setObjectName(u"menuOrden_ascendente")
        self.menuOrden_descendente = QMenu(self.menubar)
        self.menuOrden_descendente.setObjectName(u"menuOrden_descendente")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrden_ascendente.menuAction())
        self.menubar.addAction(self.menuOrden_descendente.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrden_ascendente.addAction(self.actionId_ascendente)
        self.menuOrden_ascendente.addAction(self.actionVelocidad_ascendente)
        self.menuOrden_descendente.addAction(self.actionDistancia_descendente)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.actionId_ascendente.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.actionVelocidad_ascendente.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.actionDistancia_descendente.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar grafo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.mostrar_datos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar datos", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Color(rgb)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabla_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabla_id_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar id", None))
        self.tabla_buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrden_ascendente.setTitle(QCoreApplication.translate("MainWindow", u"Orden ascendente", None))
        self.menuOrden_descendente.setTitle(QCoreApplication.translate("MainWindow", u"Orden descendente", None))
    # retranslateUi