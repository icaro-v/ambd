import psycopg2, os, socket, subprocess
from time import sleep

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
    cur.execute(f'''CREATE database "{nome_base}";''')
    pg.close()


def importa_base_zerada(nome_base, caminho_base_zerada):
    nome_base = nome_base
    base_zerada = caminho_base_zerada

    os.environ["PGPASSWORD"] = "Supinf12!"
    os.environ["PGUSER"] = "postgres"
    os.environ["PGHOST"] = ip 
    os.environ["PGDATABASE"] = nome_base

    drop_schema = "drop schema if exists public cascade;"
    restore = f'pg_restore -d {nome_base} "{base_zerada}"'

    subprocess.run(f'psql -c "{drop_schema}"', shell=True)
    subprocess.run(restore, shell=True)


def dump(nome_base, caminho_nova_base):
    nome_base = nome_base
    caminho = caminho_nova_base

    os.environ["PGPASSWORD"] = "Supinf12!"
    os.environ["PGUSER"] = "postgres"
    os.environ["PGHOST"] = ip 
    os.environ["PGDATABASE"] = nome_base

    nome_dump = f'{caminho}/{nome_base}'

    subprocess.run(f'pg_dump -f "{nome_dump}" --format=c', shell=True)
    
    pg.close()
