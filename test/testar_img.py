import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        image_path = 'imgs/converter.png'


        # # Carregar a imagem a partir do caminho especificado
        # with open(image_path, 'rb') as f:
        #     image_data = f.read()
        
        # Passo 1: Carregar a imagem como dados binários
        with open(image_path, 'rb') as image_file:
            image_binary = image_file.read()
        
        image_base64 = base64.b64encode(image_binary).decode()

        print(image_base64)

        exit()

        # with open('bin.txt', 'w') as bin:
        #     bin.write(image_base64)


        img = base64.b64decode(binario(2))

        pixmap = QPixmap()
        pixmap.loadFromData(img)

        # pixmap.loadFromData(image_data)



        # Criar um QLabel para exibir a imagem
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        # Configurar a janela principal
        self.setWindowTitle("Visualizador de Imagem")
        self.setGeometry(100, 100, pixmap.width(), pixmap.height())

        # Criar um layout para o widget principal
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


main('imgs/postgresql.png')