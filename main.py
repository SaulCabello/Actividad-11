import sys
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication()

main = MainWindow()

main.show()

sys.exit(app.exec_())