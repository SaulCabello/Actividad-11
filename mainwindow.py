from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Particula.mainclass import MainClass
from Particula.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.mainclass = MainClass()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)

    @Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.mainclass.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Operacion exitosa",
                "El archivo " + ubicacion + " se abrio correctamente"
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo"
            )

    @Slot()
    def guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.mainclass.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Operacion exitosa",
                "El archivo " + ubicacion + " se guardo correctamente"
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al guardar el archivo"
            )
    
    @Slot()
    def agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.mainclass.agregar_inicio(particula)
    
    @Slot()
    def agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.mainclass.agregar_final(particula)
    
    @Slot()
    def mostrar(self):
        self.ui.print.clear()
        self.ui.print.insertPlainText(str(self.mainclass))