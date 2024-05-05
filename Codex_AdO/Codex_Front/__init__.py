import sys
from Codex_AdO.Codex_Front import Front
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Front.MainWindow()
    window.show()
    sys.exit(app.exec())


