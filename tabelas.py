import psycopg2, fdb, socket


class Tabelas:
    def __init__(self, caminho, nome_nova_base):
        ip_local = socket.gethostbyname(socket.gethostname())

        self.conexao_fb = fdb.connect(host=ip_local, database=caminho,user="sysdba",password="masterkey")

        self.conexao_pg = psycopg2.connect(host=ip_local, database=nome_nova_base, user='postgres', password = 'Supinf12!')

        self.conexao_pg.autocommit = True

        self.fb = self.conexao_fb.cursor()
        self.pg = self.conexao_pg.cursor()

    
    def alter_sequence(self, sequencia, inicio):
        # print(f'{sequencia}: {inicio}')
        self.pg.execute(f"ALTER SEQUENCE {sequencia} RESTART WITH {inicio};")
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


    def inverte_ordem(self, lista, prim, seg):
        lista[prim], lista[seg] = lista[seg], lista[prim]


    def corrige_time(self, lista, indice):
        if (lista[indice] != None):
                lista[indice] = lista[indice].strftime("%Y-%m-%d %H:%M:%S")


    def cadpar(self):
        self.fb.execute("select * from cadpar")
        par = self.fb.fetchall()

        self.pg.execute("""INSERT INTO cadpar (nreg, partxs, partxicm, parseg, parprcimp, partarminnac, partxacre, partarminint, partarint, parminacres, parposramal, parnumramal, parposdata, parnumdata, parposhora, parnumhora, parposdurhor, parnumdurhor, parposdurmin, parnumdurmin, parposdurseg, parnumdurseg, parposnr, parnumnr, parposdest, parnumdest, partippabx, parcommport, parstopbits, parbauderate, pardatabits, parparidade, parxonent, parxonsai, partotcarac, partempomanha, partempotarde, partemponoite, partempomad, parcodarea, parultreg, partel0900min, horcelini, horcelfim, horcelini2, horcelifim2, desccel, celprcarea, celprcest, cor, parlic, curva_a, curva_b, curva_c, parimagem, parmindest, sublinha_relatorio, vl_cobrar, localidade, uf_localidade, receber_ligacoes, valor_ligacoes_recebidas, parpos_identrada, parnum_identrada, parposdurmin_e, parnumdurmin_e, parposdurhor_e, parnumdurhor_e, parposdurseg_e, parnumdurseg_e, parposhora_e, parnumhora_e, parposdata_e, parnumdata_e, parposramal_e, parnumramal_e, parposnr_e, parnumnr_e, ao_codigo_area, ao_hrfim, ao_datawindows, operadora_padrao, vigencia, ao_vigencia, modelo, parpostronco, parnumtronco, parpostronco_e, parnumtronco_e, parposcodigo, parnumcodigo, ao_rotacusto, ao_segduracao, ao_senha, ao_dt_americano, ao_dt_s_formato, ao_hr_s_formato, ao_rotacusto_tronco, ao_scheduler, reldia, periodicidade, ao_recebida, dt_reldia, fromadress, fromname, subject, smtp, userid, parpospmam_e, parnumpmam_e, parpospmam, parnumpmam, ao_valor_cheio, local_mesa_pc, ao_autenticacao, senha_autenticacao, prioridade, ao_confirmacao, usuario_info, forma_scheduler, dt_reldia_n, email_info, email, ao_txt_tpdados, ao_txt_tptipo, ao_txt_exp, ao_txt_dir, ao_txt_file, ao_data_det, ao_data_det_e, parpos_data_dia, parnum_data_dia, parpos_data_dia_e, parnum_data_dia_e, parpos_data_mes, parnum_data_mes, parpos_data_mes_e, parnum_data_mes_e, parpos_data_ano, parnum_data_ano, parpos_data_ano_e, parnum_data_ano_e, ao_fator_convert, ao_tipo_convert, vl_tipo_convert, tcp_host, tcp_porta, tcp_tipo, ao_utiliza_tempo_espera, parposdurmin_e2, parnumdurmin_e2, parposdurseg_e2, parnumdurseg_e2, versao_bd, ao_portamanual, ao_menu, ao_rel_particular, ao_formato_relatorio, ao_tarifa_ligacao, ao_atualizacao, email_responsavel, ao_multi_site, intervalo_alternancia, host_pabx, porta_pabx, senha_proxy, porta_proxy, usuario_proxy, servidor_proxy, ao_autenticacao_proxy, porta_internet, ao_utiliza_proxy, ao_importa_sem_telefone, tolerancia, ao_mascara_telefone, celprcreg, parsite, paritem, atualiza_status_ramais, parposadicional, parnumadicional, parposadicional_e, parnumadicional_e, usuario_pabx, senha_usuario_pabx, utiliza_login_pabx, parfusohorario, suporte_soma, qtd_bilhete_tarifacao, contasagenda, ao_executa_assistente, ao_gera_arq_separador, separador_arq, database_mysql, ao_txt_exp_entrante, dsmysql, ao_processador, parreiniciatcp, ramaisagenda, cadin_smtp, cadin_nome_email, cadin_usuario, cadin_senha, ao_requer_autenticacao, ao_txt_exp_numerico, ao_exp_ddd_separado, ao_taxa, tipo_taxa, paracrescimo, paracrescimomin, cadin_porta, ao_txt_exp_ramal, pardatpesq, habilita_thread, parhrpesq, ao_cadram_automatico, ao_trata_extensao, ao_zeroesq, ao_inverte_data, duracao_como_hr_de, cd_contrato_soliden) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", par)
        
        self.conexao_pg.commit()


    def departamento(self):
        #   ========   DEPARTAMENTO   ========   +
        self.fb.execute("select * from departamento")
        departamentos = self.fb.fetchall()

        for dep in departamentos:
            dep = list(dep[0:-2])
            
            self.inverte_ordem(dep, 3, 4)

            dep = tuple(dep)

            self.pg.execute("""INSERT INTO departamento (cd_departamento, ds_departamento, email, tempo_limite, valor_limite, ao_envia_email)VALUES (%s, %s, %s, %s, %s, %s);""", dep)

        self.conexao_pg.commit()


    def cadcus(self):
        #   ========   CADCUS   ========   +
        cur = self.fb.execute('select * from cadcus')
        centros = cur.fetchall()

        for centro in centros:
            centro = list(centro[0:-2])

            self.inverte_ordem(centro, 5, 6)
            self.inverte_ordem(centro, 7, 8)

            centro = tuple(centro)

            self.pg.execute("""INSERT INTO cadcus (cuscod, cusdes, flag, email_responsavel, empresa, tempo_limite, valor_limite, ao_padrao, ao_envia_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", centro)

        self.conexao_pg.commit()

        #   ========   DEPARTAMENTO_ITEM   ========   +
        self.fb.execute("select * from departamento_item")
        vinculos = self.fb.fetchall()

        self.pg.execute('delete from departamento_item')
        self.conexao_pg.commit()

        for vinculo in vinculos:    
            self.pg.execute("""INSERT INTO DEPARTAMENTO_ITEM (CD_DEPARTAMENTO, CUSCOD) VALUES (%s, %s);""", vinculo)

        self.conexao_pg.commit()


    def cadram(self):
        self.fb.execute("select * from cadram")
        ramais = self.fb.fetchall()

        for ramal in ramais:
            ramal = list(ramal)

            self.inverte_ordem(ramal, 19, 20)

            ramal.insert(22, None)

            self.inverte_ordem(ramal, 21, 23)

            self.corrige_time(ramal, 15)
            self.corrige_time(ramal, 16)

            ramal = tuple(ramal)

            self.pg.execute("""INSERT INTO cadram
            (ramcod, ramdes, ramtel, cuscod, flag, email, valor_ramal, flag_pre_aviso, flag_vencimento, tempo_ramal, agrega_servico, ao_bloqueado, ramal_liberado, ao_tarifa_entrante, nreg, vigencia_inicial, vigencia_final, numero_registro, ao_exibe_agenda, senha_ramal_ip, ao_ramal_ip, msg_ramal_ip, ao_ramail_ip, ao_tarifa_entrantestronco, localizacao, observacao, ao_passa_supervisao, ao_envia_email, ao_vigencia)
            VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", ramal)

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

        self.pg.execute("delete from cadope")
        self.conexao_pg.commit()

        for cadope in cadopes:
            cadope = list(cadope)

            cadope[4] = None

            cadope.insert(11, None)
            cadope.insert(11, None)

            self.move(cadope, 21, 13)
            self.move(cadope, 21, 18)

            cadope = tuple(cadope[0:-5])
        
            self.pg.execute("""INSERT INTO cadope (opecod, openom, opesen, email, foto, ao_monitor, opepage, ao_consulta_valor_real, ao_supervisor, login_web, senha_web, "valid", "role", ao_exibe_dashboard, ramal_operador, ao_supervisor_cc, ao_supervisor_dep, ao_acesso_total_web, nr_template, cor_botao, cor_botao_mouse, cor_panel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", cadope)

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

        self.pg.execute("delete from opcional")
        self.conexao_pg.commit()

        for op in opc:
            self.pg.execute("""INSERT INTO opcional (posicao, tamanho, valor, cd_opcional, descricao, aoparametro) VALUES (%s, %s, %s, %s, %s, %s);""", op)

        self.conexao_pg.commit()


    def corrige_sequences(self):
        self.fb.execute("select max(GEN_ID(G_CADCHA, 0)) from cadcha;")
        seq_cadcha = self.fb.fetchall()[0][0] + 2

        self.fb.execute("select max(GEN_ID(G_CADRAM, 0)) from cadram;")
        seq_cadram = self.fb.fetchall()[0][0] + 2

        self.alter_sequence('g_cadcha', seq_cadcha)
        self.alter_sequence('g_cadcha', seq_cadram)    

        self.conexao_pg.commit()

        # self.pg.execute("SELECT sequence_name, start_value  FROM information_schema.sequences WHERE sequence_name in ('g_cadram', 'g_cadcha')")

        # aa = self.pg.fetchall()

        # print(aa)

        
    def migrar(self):
        self.limpa_bd()

        # cadpar()     >>> pendente terminar

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
