#---------------------------------------------------------------------------------------------------------------------------------------"

import sys, os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit,
    QMessageBox
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import tkinter as tk
import calendario
import generar_pdf
import datos
import csv

columns = ['id']


def borrar():
    with open('data.csv',"w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow("1")
    with open('data2.csv',"w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow("2")
    with open('data3.csv',"w") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow("3")

#---------------------------------------------------------------------------------------------------------------------------------------"

class VentanaPython(QMainWindow):# HERECIA 
    def __init__(self): # CONSTRUCTOR
        super().__init__()
        self.pesonalizarVentana()
        self.personalizarComponentes()

    def pesonalizarVentana(self):
        self.setWindowTitle("LOGIN")  # Crear una ventana y poner un título
        self.setFixedSize(480, 330) # Poner un ancho y altura a la ventana y no redimensiona
        self.setStyleSheet("background-color: lightgray;") # Color de fondo
        self.pnlPrincipal = QWidget() # Crear un contenedor principal
        self.setCentralWidget(self.pnlPrincipal) # Establecer el contenedor principal para nuestra ventana
        ruta_relativa = "data/contrasena.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

#---------------------------------------------------------------------------------------------------------------------------------------"
        
    def personalizarComponentes(self):

        self.lblLogin = QLabel("LOGIN",self.pnlPrincipal) #Crear objeto label
        self.lblLogin.setFont(QFont("Courier New", 12))
        self.lblLogin.setStyleSheet("color: #FF0000;") #Color letra RGB
        self.lblLogin.setAlignment(Qt.AlignCenter)
        self.lblLogin.setGeometry(190, 60, 100, 20)

        self.txtLogin = QLineEdit(self.pnlPrincipal)
        self.txtLogin.setGeometry(190, 90, 100, 20)
        self.txtLogin.setFont(QFont("Courier New", 9))
        self.txtLogin.setAlignment(Qt.AlignCenter)
        self.txtLogin.setStyleSheet("color: blue;")   

        self.lblPassword = QLabel("PASSWORD",self.pnlPrincipal) #Crear objeto label
        self.lblPassword.setFont(QFont("Courier New", 12))
        self.lblPassword.setStyleSheet("color: #FF0000;") #Color letra RGB
        self.lblPassword.setAlignment(Qt.AlignCenter)
        self.lblPassword.setGeometry(190, 120, 100, 20)

        self.txtPassword = QLineEdit(self.pnlPrincipal)
        self.txtPassword.setGeometry(190, 150, 100, 20)
        self.txtPassword.setFont(QFont("Courier New", 9))
        self.txtPassword.setAlignment(Qt.AlignCenter)
        self.txtPassword.setStyleSheet("color: blue;")  
        self.txtPassword.setEchoMode(QLineEdit.Password)                

        self.botAceptar = QPushButton("ACEPTAR", self.pnlPrincipal)
        self.botAceptar.setFont(QFont("Courier New", 8))
        self.botAceptar.setStyleSheet("background-color: black; color: white;")
        self.botAceptar.setGeometry(190, 180, 100, 20)
        self.botAceptar.clicked.connect(self.botAceptarClic)       

        self.lblE = QLabel("", self)
        self.lblE.setFont(QFont("Courier New", 12))
        self.lblE.setStyleSheet("color: #FF0000;")
        self.lblE.setAlignment(Qt.AlignCenter)
        self.lblE.setGeometry(0, 250, 480, 20)

#---------------------------------------------------------------------------------------------------------------------------------------"          

    def botAceptarClic(self):
        login = self.txtLogin.text()
        password1 = self.txtPassword.text()
        for i in range(len(datos.nombre)):
            if datos.nombre[i] == login and datos.password[i] == password1:
                QMessageBox.information(self,"INFORMACION","USUARIO CORRECTO")
                self.abrirVentana(datos.nombre[i],datos.vacaciones[i],datos.departamento[i],datos.empresa[i],datos.al_vacas,datos.al_vacas2,datos.al_vacas3,datos.fiestas[i], datos.permisos[i])
                borrar()
                break
        else:
            QMessageBox.information(self,"INFORMACION","USUARIO INCORRECTO")

#---------------------------------------------------------------------------------------------------------------------------------------"            

    def abrirVentana(self, nombre,vacaciones,departamento,empresa,al_vacas, fiestas, permisos,al_vacas2,al_vacas3):
        #self.objeto_ventana_menu = calendario.Ventana(nombre, vacaciones,departamento,empresa,al_vacas)
        self.objeto_ventana_menu = calendario.Ventana(nombre, vacaciones,departamento,empresa,al_vacas, fiestas, permisos,al_vacas2,al_vacas3)
        #self.objeto_ventana_menu2 = generar_pdf(nombre,departamento,empresa)
        self.objeto_ventana_menu.show()
        self.close()

#---------------------------------------------------------------------------------------------------------------------------------------"         

if __name__ == '__main__':       # METODO PRINCIPAL
    app = QApplication(sys.argv) # ABRIR APLICACION
    ventana = VentanaPython()    # Objeto de la ventana
    ventana.show()               # Muestra la ventana
    sys.exit(app.exec_())        # CERRAR APLICACION