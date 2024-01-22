import psycopg2, fdb, socket, datetime


class Tabelas:
    def __init__(self, caminho, nome_nova_base):
        ip_local = socket.gethostbyname(socket.gethostname())

        self.conexao_fb = fdb.connect(host=ip_local, database=caminho,user="sysdba",password="masterkey")

        self.conexao_pg = psycopg2.connect(host=ip_local, database=nome_nova_base, user='postgres', password = 'Supinf12!')

        self.conexao_pg.autocommit = True

        self.fb = self.conexao_fb.cursor()
        self.pg = self.conexao_pg.cursor()
 
        self.tabelas = [('departamento', []), ('cadcus', []), ('departamento_item', []), ('cadram', []), ('cadconta', []), 
                        ('tronco', []), ('grupo_tronco', []), ('grupo_tronco_item', []), ('filtro', []), ('cliente', []),
                        ('telefone', []), ('plano', []), ('cadoper', []), ('cadoper_item', []), ('horario_operadora', []),
                        ('cadpar', ['parimagem']), ('cadope', ['foto']), ('cadaux', []), ('identificador_entrada', []), ('opcional', [])]


    def alter_sequence(self, sequencia, inicio):
        self.pg.execute(f"SELECT setval('{sequencia}', {inicio});")
        self.conexao_pg.commit()


    def deleta(self, tabela):
        self.pg.execute(f"delete from {tabela}")


    def limpa_bd(self):
        for tabela in self.tabelas:
            self.deleta(tabela[0])

        self.alter_sequence('g_cadcha', 1)
        self.alter_sequence('g_cadram', 1)
        self.alter_sequence('g_plano', 1)
        # self.alter_sequence('g_cliente', 1)
        
        self.conexao_pg.commit()


    def move(self, lista, tira, poe):
        aux = lista[tira]
        del(lista[tira])
        lista.insert(poe, aux)


    def corrige_time(self, lista, indice):
        if (lista[indice] != None):
            lista[indice] = lista[indice].strftime("%Y-%m-%d %H:%M:%S")


    def corrige_sequences(self):
        try:
            self.fb.execute("SELECT max(chanum) FROM cadcha;")
        except:
            self.fb.execute("SELECT count(*) FROM cadcha;")

        seq_cadcha = self.fb.fetchall()[0][0]


        try:
            self.fb.execute("SELECT max(nreg) FROM cadram;")
        except:
            self.fb.execute("SELECT count(*) FROM cadram;")

        seq_cadram = self.fb.fetchall()[0][0] 


        try:
            self.fb.execute("SELECT max(cd_plano) FROM plano;")
        except:
            self.fb.execute("SELECT count(*) FROM plano;")

        seq_plano = self.fb.fetchall()[0][0]  


        try:
            self.fb.execute("SELECT max(chanum) FROM cliente;")
        except:
            self.fb.execute("SELECT count(*) FROM cliente;")

        seq_cli = self.fb.fetchall()[0][0]  



        if(seq_cadcha == None):
            seq_cadcha = 1

        if(seq_cadram == None):
            seq_cadram = 1

        if(seq_plano == None):
            seq_plano = 1

        if(seq_cli == None):
            seq_cli = 1

        self.alter_sequence('g_cadcha', seq_cadcha)
        self.alter_sequence('g_cadram', seq_cadram)    
        self.alter_sequence('g_plano', seq_plano)
        self.alter_sequence('g_cliente', seq_cli)

        self.conexao_pg.commit()


    def aumenta(self, barra):
       progressBar = barra
       progressBar.setValue(progressBar.value() + 6)

    
    def converte(self, dados, remove = None):
        tabela = dados[0]

        if dados[1]:
            remove = dados[1]

        fb = self.fb.execute(f'select FIRST 1 * from {tabela}')
        lista_fb = [desc[0].lower() for desc in fb.description]

        self.pg.execute(f'select * from {tabela} limit 1')
        pg = self.pg.description
        lista_pg = [desc.name.lower() for desc in pg]

        lista_final = [elemento_fb for elemento_pg, elemento_fb in zip(lista_pg, lista_fb) if elemento_fb == elemento_pg]
           
        if remove != None:
            for a in remove:
                if a in lista_final:
                    lista_final.remove(a)
                    
        s = len(lista_final) * '%s, '
        s = s[:-2]

        colunas = ', '.join(lista_final)

        query = self.fb.execute(f'select {colunas} from {tabela}')
        cql = query.fetchall()


        for registro in cql:
            registro = list(registro)
        
            for i, e in enumerate(registro):
                if (type(e) == datetime.datetime):
                    e = self.corrige_time(registro, i)

            registro = tuple(registro)

            try:
                self.pg.execute(f"""INSERT INTO {tabela} ({colunas}) VALUES ({s});""", registro)
            except:
                with open('nao_conv.txt', 'a') as arq:
                    arq.write(f"INSERT INTO {tabela} ({colunas}) VALUES {registro};\n")

        self.conexao_pg.commit()


    def migrar(self, barra):
        self.limpa_bd()

        for tabela in self.tabelas:
            try:
                self.converte(tabela)             
            except Exception as e:
                with open('nao_conv.txt', 'a') as arq:
                    arq.write(f"{e}:\n{tabela}\n\n")
            
            self.aumenta(barra)
        
        self.corrige_sequences()

        self.pg.close()
        
        self.fb.close()
