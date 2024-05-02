from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, \
    QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
from PySide2.QtGui import QFont
from Codex_AdO.Codex_Back import Creator, User
import pandas as pd
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ordenamiento de Datos")
        self.setStyleSheet("background-color: #add8e6;")

        main_layout = QHBoxLayout()

        # Organizando botones y combobox a la izquierda
        left_layout = QVBoxLayout()

        self.label1 = QLabel("Seleccione el método de ordenamiento:")
        self.label1.setFont(QFont("Arial", 12))
        self.label1.setStyleSheet("color: #333;")
        left_layout.addWidget(self.label1)

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("1 - BubbleSort")
        self.comboBox1.addItem("2 - BucketSort")
        self.comboBox1.addItem("3 - CountingSort")
        self.comboBox1.addItem("4 - HeapSort")
        self.comboBox1.addItem("5 - InsertionSort")
        self.comboBox1.addItem("6 - MergeSort")
        self.comboBox1.addItem("7 - QuickSort")
        self.comboBox1.addItem("8 - RadixSort")
        self.comboBox1.addItem("9 - SelectionSort")
        self.comboBox1.setFont(QFont("Arial", 12))
        left_layout.addWidget(self.comboBox1)

        self.label2 = QLabel("Seleccione la columna:")
        self.label2.setFont(QFont("Arial", 12))
        self.label2.setStyleSheet("color: #333;")
        left_layout.addWidget(self.label2)

        self.comboBox2 = QComboBox()
        self.comboBox2.addItem("mujeres")
        self.comboBox2.addItem("hombres")
        self.comboBox2.addItem("edad")
        self.comboBox2.setFont(QFont("Arial", 12))
        left_layout.addWidget(self.comboBox2)

        self.button_ordenar = QPushButton("Mostrar Información Ordenada")
        self.button_ordenar.setFont(QFont("Arial", 12))
        self.button_ordenar.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; padding: 10px 24px; cursor: pointer; border-radius: 5px;")
        left_layout.addWidget(self.button_ordenar)

        self.button_sin_ordenar = QPushButton("Mostrar Información sin Ordenar")
        self.button_sin_ordenar.setFont(QFont("Arial", 12))
        self.button_sin_ordenar.setStyleSheet(
            "background-color: #f44336; color: white; border: none; padding: 10px 24px; cursor: pointer; border-radius: 5px;")
        left_layout.addWidget(self.button_sin_ordenar)

        main_layout.addLayout(left_layout)

        # Añadiendo la tabla a la derecha
        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.button_ordenar.clicked.connect(self.mostrar_informacion_ordenada)
        self.button_sin_ordenar.clicked.connect(self.mostrar_informacion_sin_ordenar)

    def mostrar_informacion_ordenada(self):
        try:
            seleccion_metodo = self.comboBox1.currentText()
            metodo_elegido = int(seleccion_metodo.split(" - ")[0])
            columna = self.comboBox2.currentText()

            ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

            datos = requests.get(ruta)
            datos.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa

            datos_json = datos.json()
            datos_df = pd.json_normalize(datos_json)

            metodo_nombre = seleccion_metodo.split(" - ")[1]
            metodo = User.Usuario.obtener_metodo_ordenamiento(metodo_elegido)
            if metodo is not None:
                creator = Creator.Creator()

                ordenamiento = datos_df[columna].astype(int)
                array_ordenado = creator.ordenar(metodo_elegido, ordenamiento, columna)[0]

                datos_df[columna] = array_ordenado
                datos_df.sort_values(by=columna, inplace=True)

                mensaje = f"Se mostró la información ordenada de la columna '{columna}' utilizando el método {metodo_nombre}."
                self.mostrar_tabla(datos_df, mensaje)
                # Mostrar el mensaje en una ventana emergente
                QMessageBox.information(self, "Información", mensaje)

        except requests.exceptions.RequestException as e:
            # Manejar el error cuando no hay conexión a Internet
            QMessageBox.critical(self, "Error", "No hay conexión a Internet. No se puede consumir el API.")
        except Exception as e:
            # Manejar otros errores genéricos
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def mostrar_informacion_sin_ordenar(self):
        try:
            columnas = ["edad", "hombres", "mujeres"]

            ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

            datos = requests.get(ruta)
            datos.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa

            datos_json = datos.json()
            datos_df = pd.json_normalize(datos_json)

            mensaje = "Se mostró la información sin ordenar de todas las columnas."
            self.mostrar_tabla(datos_df[columnas], mensaje)
            # Mostrar el mensaje en una ventana emergente
            QMessageBox.information(self, "Información", mensaje)

        except requests.exceptions.RequestException as e:
            # Manejar el error cuando no hay conexión a Internet
            QMessageBox.critical(self, "Error", "No hay conexión a Internet. No se puede consumir el API.")
        except Exception as e:
            # Manejar otros errores genéricos
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def mostrar_tabla(self, df, mensaje):
        self.table.clear()
        self.table.setColumnCount(len(df.columns))
        self.table.setRowCount(len(df))
        self.table.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.table.setItem(i, j, item)






