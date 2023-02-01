import sys
from PyQt5 import uic
from ejemplo3 import inf
from VirtualMouse import Handt
from PyQt5.QtWidgets import QDialog, QSplashScreen, QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time
from imagenes import images

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap("fondo.jpg")
        self.setPixmap(pixmap)
    def progress(self):
        for i in range(1):
            time.sleep(0.08)
            self.barra.setValue(i)




class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana1.ui", self)
        self.pushButton_2.clicked.connect(self.fun_ventana2)

    def fun_ventana2(self):
        uic.loadUi("ventana2.ui", self)
        self.iniciar.clicked.connect(self.funcion_activar)


    def funcion_activar(self):
        self.iniciar.setEnabled(False)
        self.etiqueta.setText("Proceso: EN CURSO")
        x = 0
        z = 0
        h = True
        while h == True:
            x = Handt()
            if x == 0:
                z = inf()
            if x == 1:
                break
            if z == 1:
                break

        self.iniciar.setEnabled(True)
        self.etiqueta.setText("Proceso: DETENIDO")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()

    window = ejemplo_GUI()
    window.show()

    splash.finish(window)
    #app.exec_()
    sys.exit(app.exec_())

