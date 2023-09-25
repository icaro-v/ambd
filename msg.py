from PySide6.QtWidgets import  QVBoxLayout, QLabel, QWidget
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class msg(QWidget):
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()

    def __init__(self, num):
        super().__init__()
        
        layout = QVBoxLayout()
        titulo = []
        titulo.append("Erro!")
        titulo.append("Nome da base incorreto!")
        titulo.append("Base já existente!")
        titulo.append("Não há base criada!")
        titulo.append("Falta zerar base")
        titulo.append("Caminho da base incorreto!")
        titulo.append("Destino inválido!")

        self.setWindowTitle(titulo[num])

        self.label = []
        self.label.append(QLabel("""Não foi possível encontar o arquivo DADOS.GDB no diretório informado.\n\nPor favor informe outro diretório."""))

        self.label.append(QLabel("""Por favor, informe corretamente um nome para a base que será criada."""))

        self.label.append(QLabel("""Já existe uma base com o nome informado. Por favor, escolha outro nome."""))

        self.label.append(QLabel("""É preciso criar uma base para receber os dados gerados. Por favor, crie uma para poder prosseguir."""))

        self.label.append(QLabel("""É necessário importar uma base zerada do Tarifador. Por favor, realize a importação para prosseguir."""))

        self.label.append(QLabel("""Não foi possível encontar a base zerada no diretório informado.\n\nPor favor informe outro diretório."""))

        self.label.append(QLabel("""O destino da base convertida não pode ser encontrado. Por favor, informe um destino válido."""))


        layout.addWidget(self.label[num])
        self.setLayout(layout)
