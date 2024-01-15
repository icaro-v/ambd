from imports import *

class ui(QMainWindow, QWidget, Ui_migr):
    def __init__(self) -> None:
        super(ui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ASSISTENTE DE MIGRAÇÃO DE BANCO DE DADOS")
        self.setCentralWidget(self.centralwidget)


    #  # --------------------        Botões        -------------------- #
               
        self.btn_vai_firebird.clicked.connect(self.vai_firebird)
        self.btn_volta_firebird.clicked.connect(self.vai_firebird)


        self.btn_vai_postgres.clicked.connect(self.vai_postgre)
        self.btn_volta_postgres.clicked.connect(self.vai_postgre)
        

        self.btn_procura_gdb.clicked.connect(self.procurar)


        self.btn_cria_base.clicked.connect(self.verifica_nome_pg)
        self.btn_busca_dump.clicked.connect(self.procurar)
        self.btn_zera_base.clicked.connect(self.zerar)


        self.btn_vai_confirmacao.clicked.connect(self.vai_confirmacao)


        self.btn_processar.clicked.connect(self.processa)
        self.btn_procura_local.clicked.connect(self.procura_local)

        self.btn_guarda_dump.clicked.connect(self.guardar)
        self.btn_concluir.clicked.connect(self.conclui)


        self.msg_banco_criado.setHidden(True)
        self.icon_banco_criado.setHidden(True)

        self.msg_base_importada.setHidden(True)
        self.icon_base_importada.setHidden(True)

        self.imgs()


    def imgs(self):
        pixmap = QPixmap()
        pixmap.loadFromData(binario(3))
        self.label_7.setPixmap(pixmap)

        pixmap.loadFromData(binario(0))
        self.label_3.setPixmap(pixmap)

        pixmap.loadFromData(binario(2))
        self.label_4.setPixmap(pixmap)

        pixmap.loadFromData(binario(1))
        self.label_8.setPixmap(pixmap)

        pixmap.loadFromData(binario(3))
        self.label_9.setPixmap(pixmap)


    def vai_firebird(self):
        self.paginas.setCurrentWidget(self.firebird)

    
    def vai_postgre(self):
        indice_atual = self.paginas.currentIndex()

        if (self.paginas.widget(indice_atual).objectName() == 'firebird'):
            self.valida_gdb()
            
            return
                        
        self.paginas.setCurrentWidget(self.postgresql)

    
    def valida_gdb(self):
            entrada = self.caminho_gdb.text()

            if(os.path.exists(entrada)):
                if(entrada.endswith(".GDB")):
                    self.paginas.setCurrentWidget(self.postgresql)
                    return

            self.msg = msg(0)
            self.msg.show()
            self.caminho_gdb.setText("")
            
                    
    def procurar(self):
        caminho = QFileDialog.getOpenFileName(self, str("Open File"), "", str("All files (*)"));
        
        indice_atual = self.paginas.currentIndex()
        pagina_atual = self.paginas.widget(indice_atual).objectName()

        if(pagina_atual == 'firebird'):
            self.caminho_gdb.setText(caminho[0])
        
        if(pagina_atual == 'postgresql'):
            self.caminho_base_zerada.setText(caminho[0])


    def verifica_nome_pg(self):
        nome_base = self.nome_nova_base.text()
        botao_zerar = self.btn_zera_base.setDisabled

        if ((len(nome_base) > 0) and (nome_base.isspace() == False)):
            if(base_ja_existe(nome_base)):
                self.msg = msg(2)
                self.msg.show()
                return

            
            criar_base_pg(nome_base)
            self.nome_nova_base.setDisabled(True)
            self.btn_cria_base.setDisabled(True)

            if (botao_zerar):
                self.btn_zera_base.setDisabled(False)

            self.msg_banco_criado.setText(f"Base de Dados {nome_base} criada com sucesso!")
            self.msg_banco_criado.setHidden(False)
            self.icon_banco_criado.setHidden(False)
            
            return
    
        self.msg = msg(1)
        self.msg.show()
        self.nome_nova_base.setText("")

        
    def zerar(self):
        falta_criar_base = self.icon_banco_criado.isHidden()
        caminho_base_zerada = self.caminho_base_zerada.text()

        if (falta_criar_base):
            self.msg = msg(3)
            self.msg.show()            
            return

        if ((len(caminho_base_zerada) > 0) and (caminho_base_zerada.isspace() == False)):
            self.setCursor(Qt.WaitCursor)


            importa_base_zerada(self.nome_nova_base.text(), caminho_base_zerada)

            self.setCursor(Qt.ArrowCursor)

            self.caminho_base_zerada.setDisabled(True)
            self.btn_busca_dump.setDisabled(True)

            self.btn_zera_base.setDisabled(True)
            self.msg_base_importada.setHidden(False)
            self.icon_base_importada.setHidden(False)
            return

        self.msg = msg(5)
        self.msg.show()
        return

    
    def vai_confirmacao(self):
        falta_criar_base = self.icon_banco_criado.isHidden()
        falta_zerar_base = self.icon_base_importada.isHidden()

        if (falta_criar_base):
            self.msg = msg(3)
            self.msg.show()
            return
        
        if (falta_zerar_base):
            self.msg = msg(4)
            self.msg.show()
            return

        self.confirmar.setText(f"""BANCO DE DADOS DE ORIGEM (Firebird)
Diretório de Origem: {self.caminho_gdb.text()}

-------------------------------------------------------------

BANCO DE DADOS DE DESTINO (PostgreSQL)
Base de Dados de Destino: {self.nome_nova_base.text()}""")

        self.paginas.setCurrentWidget(self.confirmacao)


    def processa(self):
        self.tabelas = Tabelas(self.caminho_gdb.text(), self.nome_nova_base.text())

        self.tabelas.migrar(self.progressBar)

        self.paginas.setCurrentWidget(self.guarda)


    def procura_local(self):
        local = QFileDialog.getExistingDirectory(self, str("Open Directory"), "")
    
        self.caminho_base_importada.setText(local)


    def guardar(self):
        local = self.caminho_base_importada.text()
        nome_nova_base = self.nome_nova_base.text()
        
        if(os.path.exists(local)):

            self.setCursor(Qt.WaitCursor)

            dump(nome_nova_base, local)


            self.paginas.setCurrentWidget(self.conclusao)
            self.setCursor(Qt.ArrowCursor)
            return
        

        self.msg = msg(6)
        self.msg.show()
        self.caminho_base_importada.setText("")


    def conclui(self):
        pg = psycopg2.connect(
            database = 'postgres',
            user = 'postgres',
            password = 'Supinf12!',
            host = ip
        )

        pg.autocommit = True

        cur = pg.cursor()

        sql = f"SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '{self.nome_nova_base.text()}' AND usename = 'postgres';"

        cur.execute(sql)

        cur.execute(f'drop database {self.nome_nova_base.text()}')      

        pg.close()
        
        app.closeAllWindows()
    

def inicia_app():
    window.show()
    sys.exit(app.exec())


app = QApplication(sys.argv)
window = ui()
