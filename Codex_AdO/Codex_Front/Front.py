from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, \
    QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
from PySide6.QtGui import QFont
from Codex_AdO.Codex_Back import Creator, User
import pandas as pd
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ordenamiento de Datos")
        self.setStyleSheet("background-color: #add8e6;")

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.label1 = QLabel("Seleccione el método de ordenamiento:")
        self.label1.setFont(QFont("Arial", 12))
        self.label1.setStyleSheet("color: #333;")
        left_layout.addWidget(self.label1)

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("1 - RadixSort")
        self.comboBox1.addItem("2 - MergeSort")
        self.comboBox1.addItem("3 - BucketSort")
        self.comboBox1.addItem("4 - HeapSort")
        self.comboBox1.addItem("5 - InsertionSort")
        self.comboBox1.addItem("6 - QuickSort")
        self.comboBox1.addItem("7 - BubbleSort")
        self.comboBox1.addItem("8 - SelectionSort")
        self.comboBox1.addItem("9 - CountingSort")
        self.comboBox1.setFont(QFont("Arial", 12))
        left_layout.addWidget(self.comboBox1)

        self.label2 = QLabel("Seleccione la columna:")
        self.label2.setFont(QFont("Arial", 12))
        self.label2.setStyleSheet("color: #333;")
        left_layout.addWidget(self.label2)

        self.comboBox2 = QComboBox()
        self.comboBox2.addItem("vehiculos")
        self.comboBox2.addItem("pasajeros")
        self.comboBox2.setFont(QFont("Arial", 12))
        left_layout.addWidget(self.comboBox2)

        self.button_sort = QPushButton("Mostrar Información Ordenada")
        self.button_sort.setFont(QFont("Arial", 12))
        self.button_sort.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; padding: 10px 24px; cursor: pointer; "
            "border-radius: 5px;")
        left_layout.addWidget(self.button_sort)

        self.button_not_sort = QPushButton("Mostrar Información sin Ordenar")
        self.button_not_sort.setFont(QFont("Arial", 12))
        self.button_not_sort.setStyleSheet(
            "background-color: #f44336; color: white; border: none; padding: 10px 24px; cursor: pointer; "
            "border-radius: 5px;")
        left_layout.addWidget(self.button_not_sort)

        self.button_sort_all = QPushButton("Ordenar Todas")
        self.button_sort_all.setFont(QFont("Arial", 12))
        self.button_sort_all.setStyleSheet(
            "background-color: #FFA500; color: white; border: none; padding: 10px 24px; cursor: pointer; "
            "border-radius: 5px;")
        left_layout.addWidget(self.button_sort_all)

        main_layout.addLayout(left_layout)

        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.button_sort.clicked.connect(self.ordered_information)
        self.button_not_sort.clicked.connect(self.information_without_order)
        self.button_sort_all.clicked.connect(self.sort_all_columns)

    def ordered_information(self):
        try:
            selected_methods = self.comboBox1.currentText()
            chosen_method = int(selected_methods.split(" - ")[0])

            route = "https://www.datos.gov.co/resource/aesn-q83n.json"

            data = requests.get(route)
            data.raise_for_status()

            data_json = data.json()
            data_df = pd.json_normalize(data_json)

            method_name = selected_methods.split(" - ")[1]
            method = User.User.get_sort_method(chosen_method)
            if method is not None:
                creator = Creator.Creator()

                # Seleccionar la columna a ordenar
                column_to_sort = self.comboBox2.currentText()

                # Convertir todas las columnas relevantes a tipos numéricos si es posible
                relevant_columns = ["vehiculos", "pasajeros"]
                for col in relevant_columns:
                    data_df[col] = pd.to_numeric(data_df[col], errors='coerce')

                # Ordenar los valores de la columna seleccionada y mantener el orden relativo de las filas
                sorted_indices = data_df.sort_values(by=column_to_sort).index

                # Aplicar el mismo orden a todo el DataFrame
                data_df = data_df.loc[sorted_indices]

                # Mostrar el DataFrame ordenado en la tabla
                self.show_table(data_df)

                message = f"Se mostró la información ordenada de la columna {column_to_sort} utilizando el método {method_name}"
                QMessageBox.information(self, "Información", message)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error al hacer la solicitud: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")

    def information_without_order(self):
        try:
            columnas = ["vehiculos", "pasajeros", "lugar", "estado", "mes", "a_o"]

            route = "https://www.datos.gov.co/resource/aesn-q83n.json"

            data = requests.get(route)
            data.raise_for_status()

            data_json = data.json()
            data_df = pd.json_normalize(data_json)

            message = "Se mostró la información sin ordenar de todas las columnas."
            self.show_table(data_df[columnas])

            QMessageBox.information(self, "Información", message)

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, "Error", "No hay conexión a Internet. No se puede consumir el API.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def sort_all_columns(self):
        try:
            selected_method = self.comboBox1.currentText()
            method_name = selected_method.split(" - ")[1]

            route = "https://www.datos.gov.co/resource/aesn-q83n.json"

            data = requests.get(route)
            data.raise_for_status()

            data_json = data.json()
            data_df = pd.json_normalize(data_json)

            creator = Creator.Creator()

            relevant_columns = ["vehiculos", "pasajeros"]

            for column in relevant_columns:
                # Convertir la columna a tipo numérico si es posible
                data_df[column] = pd.to_numeric(data_df[column], errors='coerce')

            for column in relevant_columns:
                column_values = data_df[column].dropna().tolist()  # Eliminar NaNs antes de ordenar
                method_index = int(selected_method.split(" - ")[0])
                ordered_values, _ = creator.method_order(method_index, column_values, column)
                data_df[column] = ordered_values

            self.show_table(data_df)

            message = f"Se mostró la información ordenada de todas las columnas utilizando el método {method_name}."
            QMessageBox.information(self, "Información", message)

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, "Error", "No hay conexión a Internet. No se puede consumir el API.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def show_table(self, df):
        self.table.clear()
        self.table.setColumnCount(len(df.columns))
        self.table.setRowCount(len(df))
        self.table.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.table.setItem(i, j, item)