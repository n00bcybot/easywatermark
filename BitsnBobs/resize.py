from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QResizeEvent Example")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Resize the window", self)
        self.label.move(20, 20)

    def resizeEvent(self, event):
        # Get the new size from the QResizeEvent
        new_size = event.size()  # QSize object containing the new size
        width = new_size.width()
        height = new_size.height()

        # Update label text with the new size
        self.label.setText(f"Window size: {width} x {height}")
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
