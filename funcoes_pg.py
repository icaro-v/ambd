import psycopg2, os, socket, os

ip = socket.gethostbyname(socket.gethostname())

pg = psycopg2.connect(
        database = "postgres",
        user = 'postgres',
        password = 'Supinf12!',
        host = ip
    )

pg.autocommit = True


def base_ja_existe(nome_base):
    cur = pg.cursor()
    cur.execute(f'''select datname from pg_database''')
    bases = cur.fetchall()

    for nome in bases:
        if (nome[0] == nome_base):
            return 1
    
    return 0


def criar_base_pg(nome_base):
    cur = pg.cursor()
    cur.execute(f'''CREATE database {nome_base};''')
    pg.close()


def edita_bat(opcao, nome_base, caminho_dump):
    with open('base.bat', 'w') as bat:
        bat.write(f'''SET PGPASSWORD=Supinf12!
SET PGUSER=postgres
SET PGHOST={ip}
SET PGDATABASE={nome_base}\n\n''')
        
        if (opcao == 0):
            bat.write(f'psql -f "{caminho_dump}"')


        if (opcao == 1):
            bat.write(f'pg_dump -f "{caminho_dump}/{nome_base}" --format=c\n\n')
            bat.write(f'''SET PGPASSWORD=Supinf12!
SET PGUSER=postgres
SET PGHOST={ip}
SET PGDATABASE=postgres\n\n''')
        
        bat.write('\nexit')


def importa_base_zerada():
    os.system('start base.bat')


def dump():
    os.system('start base.bat')

    pg.close()
    

def dropa():
    os.system('start base.bat')
