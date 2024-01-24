import sys, base64
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        with open(image_path, 'rb') as image_file:
            image_binary = image_file.read()
        
        image_base64 = base64.b64encode(image_binary).decode()
        img = base64.b64decode(image_base64)
        
        pixmap = QPixmap()
        pixmap.loadFromData(img)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        self.setWindowTitle("Visualizador de Imagem")
        self.setGeometry(100, 100, pixmap.width(), pixmap.height())

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        central_widget.setLayout(layout)


def main(image_path):
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_path)
    viewer.show()
    sys.exit(app.exec_())


main('imgs/conversor.ico')