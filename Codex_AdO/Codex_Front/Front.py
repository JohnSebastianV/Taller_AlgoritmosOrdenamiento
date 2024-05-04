from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, \
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
        self.comboBox2.addItem("mujeres")
        self.comboBox2.addItem("hombres")
        self.comboBox2.addItem("edad")
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
            selectedmethods = self.comboBox1.currentText()
            chosenmethod = int(selectedmethods.split(" - ")[0])
            column = self.comboBox2.currentText()

            route = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

            data = requests.get(route)
            data.raise_for_status()

            data_json = data.json()
            data_df = pd.json_normalize(data_json)

            methodname = selectedmethods.split(" - ")[1]
            method = User.User.get_sort_method(chosenmethod)
            if method is not None:
                creator = Creator.Creator()

                ordering = data_df[column].astype(int)
                arrayordering = creator.method_order(chosenmethod, ordering, column)[0]

                data_df[column] = arrayordering
                data_df.sort_values(by=column, inplace=True)

                message = f"Se mostró la información ordenada de la columna {column} utilizando el método {methodname}"
                self.show_table(data_df)

                QMessageBox.information(self, "Información", message)

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, "Error", "No hay conexión a Internet. No se puede consumir el API.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def information_without_order(self):
        try:
            columnas = ["edad", "hombres", "mujeres"]

            route = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

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

            route = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

            data = requests.get(route)
            data.raise_for_status()

            data_json = data.json()
            data_df = pd.json_normalize(data_json)

            creator = Creator.Creator()

            for column in ["edad", "hombres", "mujeres"]:
                column_values = data_df[column].astype(int).tolist()
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
