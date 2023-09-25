import psycopg2, fdb, socket, datetime


class Tabelas:
    def __init__(self, caminho, nome_nova_base):
        ip_local = socket.gethostbyname(socket.gethostname())

        self.conexao_fb = fdb.connect(host=ip_local, database=caminho,user="sysdba",password="masterkey")

        self.conexao_pg = psycopg2.connect(host=ip_local, database=nome_nova_base, user='postgres', password = 'Supinf12!')

        self.conexao_pg.autocommit = True

        self.fb = self.conexao_fb.cursor()
        self.pg = self.conexao_pg.cursor()

    
    def alter_sequence(self, sequencia, inicio):
        self.pg.execute(f"SELECT setval('{sequencia}', {inicio});")
        self.conexao_pg.commit()


    def deleta(self, tabela):
        self.pg.execute(f"delete from {tabela}")


    def limpa_bd(self):
        tabelas = ['departamento', 'departamento_item', 'cadcus', 'cadram', 'cadconta', 'tronco', 'grupo_tronco', 'grupo_tronco_item', 'filtro', 'cliente', 'telefone', 'plano', 'cadoper', 'cadoper_item', 'horario_operadora', 'cadpar', 'cadope', 'cadaux', 'identificador_entrada', 'opcional']

        for tabela in tabelas:
            self.deleta(tabela)

        self.alter_sequence('g_cadcha', 1)
        self.alter_sequence('g_cadram', 1)
        self.alter_sequence('g_plano', 1)
        self.alter_sequence('g_cliente', 1)
        
        self.conexao_pg.commit()


    def move(self, lista, tira, poe):
        aux = lista[tira]
        del(lista[tira])
        lista.insert(poe, aux)


    def inverte_coluna(self, lista, prim, seg):
        a = lista.index(prim)
        b = lista.index(seg)
        lista[a], lista[b] = lista[b], lista[a]

    
    def inverte_ordem(self, lista, prim, seg):
        lista[prim], lista[seg] = lista[seg], lista[prim]


    def corrige_time(self, lista, indice):
        if (lista[indice] != None):
            lista[indice] = lista[indice].strftime("%Y-%m-%d %H:%M:%S")


    def cadpar(self):
        cur = self.fb.execute("select * from cadpar")
        parametros = cur.fetchall()[0]

        colunas_banco = [desc[0].lower() for desc in cur.description]
        
        if(len(colunas_banco) > 217):
            colunas_banco = colunas_banco[0:217]
            parametros = parametros[0:217]

        self.inverte_coluna(colunas_banco, 'parfusohorario', 'ao_executa_assistente')

        self.inverte_coluna(colunas_banco, 'suporte_soma', 'ao_executa_assistente')

        self.inverte_coluna(colunas_banco, 'contasagenda', 'ao_executa_assistente')


        self.move(colunas_banco, 201, 211)


        self.inverte_coluna(colunas_banco, 'parhrpesq', 'habilita_thread')

        # Criar um dicionário para armazenar os resultados
        dicionario = {}

        for col, value in zip(colunas_banco, parametros):
            dicionario[col] = value

        del(dicionario['valorramal'])
        del(dicionario['ao_inverte_data'])


        self.inverte_ordem(dicionario, 'parfusohorario', 'ao_executa_assistente')  

        self.inverte_ordem(dicionario, 'suporte_soma', 'parfusohorario')  
        self.inverte_ordem(dicionario, 'contasagenda', 'suporte_soma')  
        self.inverte_ordem(dicionario, 'cadin_nome_email', 'cadin_porta') 
        self.inverte_ordem(dicionario, 'cadin_usuario', 'cadin_nome_email') 
        self.inverte_ordem(dicionario, 'cadin_senha', 'cadin_usuario') 
        self.inverte_ordem(dicionario, 'ao_requer_autenticacao', 'cadin_senha') 
        self.inverte_ordem(dicionario, 'ao_txt_exp_numerico', 'ao_requer_autenticacao') 

        self.inverte_ordem(dicionario, 'ao_exp_ddd_separado', 'ao_txt_exp_numerico') 

        self.inverte_ordem(dicionario, 'ao_taxa', 'ao_exp_ddd_separado') 
        self.inverte_ordem(dicionario, 'tipo_taxa', 'ao_taxa') 
        self.inverte_ordem(dicionario, 'tipo_taxa', 'paracrescimo')
        self.inverte_ordem(dicionario, 'paracrescimo', 'paracrescimomin')
        self.inverte_ordem(dicionario, 'parhrpesq', 'habilita_thread')  


        dicionario['parimagem'] = None

        valores = list(dicionario.values())

        for i, e in enumerate(valores):
            if (type(e) == datetime.datetime):
                e = self.corrige_time(valores, i)

        self.pg.execute("""INSERT INTO cadpar (nreg, partxs, partxicm, parseg, parprcimp, partarminnac, partxacre, partarminint, partarint, parminacres, parposramal, parnumramal, parposdata, parnumdata, parposhora, parnumhora, parposdurhor, parnumdurhor, parposdurmin, parnumdurmin, parposdurseg, parnumdurseg, parposnr, parnumnr, parposdest, parnumdest, partippabx, parcommport, parstopbits, parbauderate, pardatabits, parparidade, parxonent, parxonsai, partotcarac, partempomanha, partempotarde, partemponoite, partempomad, parcodarea, parultreg, partel0900min, horcelini, horcelfim, horcelini2, horcelifim2, desccel, celprcarea, celprcest, cor, parlic, curva_a, curva_b, curva_c, parimagem, parmindest, sublinha_relatorio, vl_cobrar, localidade, uf_localidade, receber_ligacoes, valor_ligacoes_recebidas, parpos_identrada, parnum_identrada, parposdurmin_e, parnumdurmin_e, parposdurhor_e, parnumdurhor_e, parposdurseg_e, parnumdurseg_e, parposhora_e, parnumhora_e, parposdata_e, parnumdata_e, parposramal_e, parnumramal_e, parposnr_e, parnumnr_e, ao_codigo_area, ao_hrfim, ao_datawindows, operadora_padrao, vigencia, ao_vigencia, modelo, parpostronco, parnumtronco, parpostronco_e, parnumtronco_e, parposcodigo, parnumcodigo, ao_rotacusto, ao_segduracao, ao_senha, ao_dt_americano, ao_dt_s_formato, ao_hr_s_formato, ao_rotacusto_tronco, ao_scheduler, reldia, periodicidade, ao_recebida, dt_reldia, fromadress, fromname, subject, smtp, userid, parpospmam_e, parnumpmam_e, parpospmam, parnumpmam, ao_valor_cheio, local_mesa_pc, ao_autenticacao, senha_autenticacao, prioridade, ao_confirmacao, usuario_info, forma_scheduler, dt_reldia_n, email_info, email, ao_txt_tpdados, ao_txt_tptipo, ao_txt_exp, ao_txt_dir, ao_txt_file, ao_data_det, ao_data_det_e, parpos_data_dia, parnum_data_dia, parpos_data_dia_e, parnum_data_dia_e, parpos_data_mes, parnum_data_mes, parpos_data_mes_e, parnum_data_mes_e, parpos_data_ano, parnum_data_ano, parpos_data_ano_e, parnum_data_ano_e, ao_fator_convert, ao_tipo_convert, vl_tipo_convert, tcp_host, tcp_porta, tcp_tipo, ao_utiliza_tempo_espera, parposdurmin_e2, parnumdurmin_e2, parposdurseg_e2, parnumdurseg_e2, versao_bd, ao_portamanual, ao_menu, ao_rel_particular, ao_formato_relatorio, ao_tarifa_ligacao, ao_atualizacao, email_responsavel, ao_multi_site, intervalo_alternancia, host_pabx, porta_pabx, senha_proxy, porta_proxy, usuario_proxy, servidor_proxy, ao_autenticacao_proxy, porta_internet, ao_utiliza_proxy, ao_importa_sem_telefone, tolerancia, ao_mascara_telefone, celprcreg, parsite, paritem, atualiza_status_ramais, parposadicional, parnumadicional, parposadicional_e, parnumadicional_e, usuario_pabx, senha_usuario_pabx, utiliza_login_pabx, parfusohorario, suporte_soma, qtd_bilhete_tarifacao, contasagenda, ao_executa_assistente, ao_gera_arq_separador, separador_arq, database_mysql, ao_txt_exp_entrante, dsmysql, ao_processador, parreiniciatcp, ramaisagenda, cadin_smtp, cadin_nome_email, cadin_usuario, cadin_senha, ao_requer_autenticacao, ao_txt_exp_numerico, ao_exp_ddd_separado, ao_taxa, tipo_taxa, paracrescimo, paracrescimomin, cadin_porta, ao_txt_exp_ramal, pardatpesq, habilita_thread, parhrpesq) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (valores))

        self.conexao_pg.commit()
    

    def departamento(self):
        #   ========   DEPARTAMENTO   ========   +
        cur = self.fb.execute("select * from departamento")
        departamentos = cur.fetchall()

        colunas_banco = [desc[0].lower() for desc in cur.description]
        colunas_desejadas = ('cd_departamento', 'ds_departamento', 'email', 'valor_limite', 'tempo_limite')

        # Criar um dicionário para armazenar os resultados
        dicionario = {}

        # Iterar pelas linhas e criar um dicionário para cada linha
        for linha in departamentos:
            dic_da_linha = {}
            for col, value in zip(colunas_banco, linha):
                dic_da_linha[col] = value
            dicionario[len(dicionario) + 1] = dic_da_linha

        for chave, dados in dicionario.items():
            dep = [dados[coluna] for coluna in colunas_desejadas]
            
            self.inverte_ordem(dep, 3, 4)

            dep = tuple(dep)

            self.pg.execute("""INSERT INTO departamento (cd_departamento, ds_departamento, email, tempo_limite, valor_limite) VALUES (%s, %s, %s, %s, %s);""", dep)

        self.conexao_pg.commit()

    
    def cadcus(self):
        #   ========   CADCUS   ========   +
        cur = self.fb.execute('select * from cadcus')
        centros = cur.fetchall()

        colunas_banco = [desc[0].lower() for desc in cur.description]
        colunas_desejadas = ('cuscod', 'cusdes', 'flag', 'email_responsavel', 'empresa', 'valor_limite', 'tempo_limite')

        # Criar um dicionário para armazenar os resultados
        dicionario = {}

        # Iterar pelas linhas e criar um dicionário para cada linha
        for linha in centros:
            dic_da_linha = {}
            for col, value in zip(colunas_banco, linha):
                dic_da_linha[col] = value
            dicionario[len(dicionario) + 1] = dic_da_linha

        for chave, dados in dicionario.items():
            centro = [dados[coluna] for coluna in colunas_desejadas]
            
            self.inverte_ordem(centro, 5, 6)

            centro = tuple(centro)

            self.pg.execute("""INSERT INTO cadcus (cuscod, cusdes, flag, email_responsavel, empresa, tempo_limite, valor_limite) VALUES (%s, %s, %s, %s, %s, %s, %s);""", centro)

            self.conexao_pg.commit()

        #   ========   DEPARTAMENTO_ITEM   ========   +
        self.fb.execute("select * from departamento_item")
        vinculos = self.fb.fetchall()

        for vinculo in vinculos:    
            self.pg.execute("""INSERT INTO DEPARTAMENTO_ITEM (CD_DEPARTAMENTO, CUSCOD) VALUES (%s, %s);""", vinculo)

        self.conexao_pg.commit()


    def cadram(self):
        self.fb.execute("select * from cadram")
        ramais = self.fb.fetchall()

        for ramal in ramais:            
            ramal = list(ramal)

            self.corrige_time(ramal, 15)
            self.corrige_time(ramal, 16)

            self.inverte_ordem(ramal, 18, 20)

            ramal.insert(22, None)

            ramal.append(None)

            print(len(ramal))
            ramal = tuple(ramal)

            for a, e in enumerate(ramal):
                print(f'{a} -- {e} -- {type(e)}')
            

            self.pg.execute("""INSERT INTO cadram
            (ramcod, ramdes, ramtel, cuscod, flag, email, valor_ramal, flag_pre_aviso, flag_vencimento, tempo_ramal, agrega_servico, ao_bloqueado, ramal_liberado, ao_tarifa_entrante, nreg, vigencia_inicial, vigencia_final, numero_registro, ao_exibe_agenda, senha_ramal_ip, ao_ramal_ip, msg_ramal_ip, ao_ramail_ip, ao_tarifa_entrantestronco, localizacao, observacao, ao_passa_supervisao, ao_envia_email, ao_vigencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", ramal)

        self.conexao_pg.commit()


    def cadconta(self):
        self.fb.execute("select * from cadconta")
        contas = self.fb.fetchall()

        for conta in contas:
            self.pg.execute("""INSERT INTO cadconta (contacod, contades, cuscod, email, valor_conta, flag_pre_aviso, flag_vencimento, tempo_conta, ao_bloqueado, conta_liberada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", conta)

        self.conexao_pg.commit()


    def tronco(self):
        self.fb.execute("select * from tronco")
        troncos = self.fb.fetchall()

        for tronco in troncos:
            self.pg.execute("""INSERT INTO tronco (codigo, descricao, opercod, ao_utiliza_subsistema, identificador_subsistema, pais_tarifacao, codigo_area, corporativo_conta, ao_tarifa_entrante, opercod_entrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", tronco)

        self.conexao_pg.commit()


    def gp_tronco(self):
        #   ========   GRUPO_TRONCO   ========   +
        self.fb.execute("select * from grupo_tronco")
        grupos = self.fb.fetchall()

        for grupo in grupos:
            self.pg.execute("""INSERT INTO grupo_tronco (nreg, descricao, qtd_tronco) VALUES (%s, %s, %s);""", grupo)

        self.conexao_pg.commit()

        #   ========   GRUPO_TRONCO_ITEM   ========   +
        self.fb.execute("select * from grupo_tronco_item")
        gtis = self.fb.fetchall()
        
        for gti in gtis:
            self.pg.execute("""INSERT INTO grupo_tronco_item (nreg, grupo_tronco, tronco) VALUES (%s, %s, %s);""", gti)

        self.conexao_pg.commit()


    def filtro(self):
        self.fb.execute("select * from filtro")
        filtros = self.fb.fetchall()

        for filtro in filtros:
            filtro = list(filtro)
            
            filtro.append(None)
            
            filtro = tuple(filtro)

            self.pg.execute("""INSERT INTO filtro (cd_filtro, descricao, ao_controle, cd_filtro_new, numero_digitos, duracao_minima, posicao_filtro, sequencia, ao_manter_tam_original, ao_plano, ao_serv) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", filtro)       

        self.conexao_pg.commit()


    def agenda(self):
        #   ========   CLIENTE   ========   +
        self.fb.execute("select * from cliente")
        clientes = self.fb.fetchall()

        for cliente in clientes:
            cliente = list(cliente)
            
            self.corrige_time(cliente, 20)

            self.corrige_time(cliente, 24)
            
            cliente = tuple(cliente)

            self.pg.execute("""INSERT INTO cliente(cd_cliente, no_cliente, sobrenome, apelido, cpf, rg, estado_civil, no_conjuge, casa_propia, tempo_servico, tempo_residencia, telefone, telefone2, telefone3, fax, celular, email, cargo, atividade, proprietario, data_cadastro, observacao, vl_renda_familiar, pessoa, dt_nascimento, produtor_rural, ao_retem_iss, ao_telefone, ao_telefone2, ao_telefone3, ao_fax, ao_celular, endereco, bairro, numero, cep, cidade, uf, naturalidade, nacionalidade, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", cliente)

        self.conexao_pg.commit()

        #   ========   TELEFONE   ========   +
        self.fb.execute("select * from telefone")
        telefones = self.fb.fetchall()

        for telefone in telefones:
            self.pg.execute("""INSERT INTO telefone (cd_cliente, nr_telefone, nome, ramal, tipo, ao_particular, operador, ao_bloqueado, ao_validado, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", telefone)

        self.conexao_pg.commit()


    def operadoras(self):
        #   ========   CADOPER   ========   +
        self.fb.execute("select * from cadoper")
        opers = self.fb.fetchall()

        for oper in opers:
            self.pg.execute("""INSERT INTO cadoper (opercod, operdes, vigencia, intervalo_local, inicio_local, valor_minimo_local, intervalo_ddd, inicio_ddd, intervalo_ddi, inicio_ddi, intervalo_cel, inicio_cel, flag_insercao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", oper)

        self.conexao_pg.commit()

        #   ========   CADOPER_ITEM   ========   +
        self.fb.execute("select * from cadoper_item")
        cois = self.fb.fetchall()

        for coi in cois:
            coi = list(coi)

            if (coi[2] != None):
                coi[2] = int(coi[2])

            coi = tuple(coi)

            self.pg.execute("""INSERT INTO cadoper_item (nreg, opercod, vigencia, regiao, setor, tipo, flag_insercao) VALUES (%s, %s, %s, %s, %s, %s, %s);""", coi)

        self.conexao_pg.commit()


    def hr_operadora(self):
        self.fb.execute("select * from horario_operadora")
        hrs = self.fb.fetchall()

        for hr in hrs:
            hr = list(hr)

            self.corrige_time(hr, 13)            
            self.corrige_time(hr, 14)

            hr = tuple(hr)  
        
            self.pg.execute("""INSERT INTO horario_operadora (nreg, operadora, setor, descricao, seg, ter, qua, qui, sex, sab, dom, feriado, tipo, hora_inicial, hora_final, valor, vigencia, valor_minimo, ddd_d1, minimo_ddd_d1, ddd_d2, minimo_ddd_d2, ddd_d3, minimo_ddd_d3, ddd_d4, minimo_ddd_d4, ddi_d1, minimo_ddi_d1, ddi_d2, minimo_ddi_d2, ddi_d3, minimo_ddi_d3, ddi_d4, minimo_ddi_d4, ddi_d5, minimo_ddi_d5, ddi_d6, minimo_ddi_d6, ddi_d7, minimo_ddi_d7, ddi_d8, minimo_ddi_d8, vc1, minimo_vc1, vc2, minimo_vc2, vc3, minimo_vc3, pulso_unico, flag_insercao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", hr)

        self.conexao_pg.commit()


    def cadope(self):
        self.fb.execute("select * from cadope")
        cadopes = self.fb.fetchall()

        for cadope in cadopes:
            cadope = list(cadope)

            cadope[4] = None

            cadope.insert(11, None)
            cadope.insert(11, None)
            cadope.insert(11, None)
        
            self.pg.execute("""INSERT INTO cadope (opecod, openom, opesen, email, foto, ao_monitor, opepage, ao_consulta_valor_real, ao_supervisor, login_web, senha_web, "valid", "role", ao_exibe_dashboard, ramal_operador, ao_supervisor_cc, ao_supervisor_dep, ao_acesso_total_web) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", cadope)

        self.conexao_pg.commit()


    def cadaux(self):
        self.fb.execute("select * from cadaux")
        cadaux = self.fb.fetchall()

        for aux in cadaux:
            self.pg.execute("""insert into cadaux (horas) values (%s);""", aux)

        self.conexao_pg.commit()


    def id_entrada(self):
        self.fb.execute("select * from identificador_entrada")
        ids = self.fb.fetchall()

        for id in ids:
            self.pg.execute("""insert into identificador_entrada (identificador) values (%s);""", id)

        self.conexao_pg.commit()


    def opcional(self):
        self.fb.execute("select * from opcional")
        opc = self.fb.fetchall()

        for op in opc:
            self.pg.execute("""INSERT INTO opcional (posicao, tamanho, valor, cd_opcional, descricao, aoparametro) VALUES (%s, %s, %s, %s, %s, %s);""", op)

        self.conexao_pg.commit()


    def corrige_sequences(self):
        self.fb.execute("SELECT max(chanum) FROM cadcha;")
        seq_cadcha = self.fb.fetchall()[0][0]

        if(seq_cadcha == None):
            seq_cadcha = 1

        self.fb.execute("SELECT max(nreg) FROM cadram;")
        seq_cadram = self.fb.fetchall()[0][0] 

        if(seq_cadram == None):
            seq_cadram = 1

        self.alter_sequence('g_cadcha', seq_cadcha)
        self.alter_sequence('g_cadram', seq_cadram)    

        self.conexao_pg.commit()

        
    def migrar(self):
        self.limpa_bd()

        self.cadpar()  

        self.departamento()

        self.cadcus()

        self.cadram()

        self.cadconta()

        self.tronco()

        self.gp_tronco()

        self.filtro()

        self.agenda()

        self.operadoras()

        self.hr_operadora()

        self.cadope()

        self.cadaux()

        self.id_entrada()

        self.opcional()

        self.corrige_sequences()

        self.pg.close()
