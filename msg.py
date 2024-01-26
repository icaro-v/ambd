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
        titulo = [
            "Atenção!",
            "Nome da base incorreto!",
            "Base já existente!",
            "Não há base criada!",
            "Falta zerar base",
            "Caminho da base incorreto!",''
            "Destino inválido!"
        ]

        self.setWindowTitle(titulo[num])

        mensagens = [
        """Não foi possível encontar o arquivo DADOS.GDB no diretório informado.\n\nPor favor informe outro diretório.""",
        """Por favor, informe corretamente um nome para a base que será criada.""",
        """Já existe uma base com o nome informado. Por favor, escolha outro nome.""",
        """É preciso criar uma base para receber os dados gerados. Por favor, crie uma para poder prosseguir.""",
        """É necessário importar uma base zerada do Tarifador. Por favor, realize a importação para prosseguir.""",
        """Não foi possível encontar a base zerada no diretório informado.\n\nPor favor informe outro diretório.""",
        """O destino da base convertida não pode ser encontrado. Por favor, informe um destino válido."""
        ]

        self.label = QLabel(mensagens[num])
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setFixedSize(self.sizeHint())
