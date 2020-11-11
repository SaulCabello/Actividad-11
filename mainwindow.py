from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        self.ui.tabla_mostrar_pushButton.clicked.connect(self.tabla_mostrar)
        self.ui.tabla_buscar_pushButton.clicked.connect(self.tabla_buscar)

    @Slot()
    def tabla_mostrar(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen en x", "Origen en y", "Destino en x", "Destino en y", "Velocidad", "Distancia", "Red", "Green", "Blue"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.mainclass))

        row = 0
        for particula in self.mainclass:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, distancia_widget)
            self.ui.tabla.setItem(row, 7, red_widget)
            self.ui.tabla.setItem(row, 8, green_widget)
            self.ui.tabla.setItem(row, 9, blue_widget)

            row += 1
    
    @Slot()
    def tabla_buscar(self):
        id = self.ui.tabla_id_lineEdit.text()
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen en x", "Origen en y", "Destino en x", "Destino en y", "Velocidad", "Distancia", "Red", "Green", "Blue"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(1)

        encontrado = False
        for particula in self.mainclass:
            if id == particula.id:
                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, distancia_widget)
                self.ui.tabla.setItem(0, 7, red_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, blue_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f"La partícula con el id '{id}' no ha sido encontrada"
            )
    
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
        