
import sys
from Codex_AdO.Codex_Front import Front

if __name__ == "__main__":
    app = Front.QApplication(sys.argv)
    window = Front.MainWindow()
    window.show()
    sys.exit(app.exec_())


