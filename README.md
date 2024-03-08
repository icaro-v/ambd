# assistente-de-migração-de-banco-de-dados

O AMBD foi feito para poupar tempo e automatizar o processo de conversão de bases de dados dos clientes do Soma Tarifador.

A aplicação:
 - se conecta à base Firebird do cliente
 - cria uma nova base PostgreSQL e se conecta à ela  
 - realiza o upload de uma base de dados zerada do Soma Tarifador na base em Postgre
 - copia os dados da base em Firebird
 - converte e insere os dados em Postgre
 - gera um dump da base Postgre pronto para ser implantado no cliente
 
Ao fim do processo, o dump pode ser utilizado no cliente no momento da implantação, com todos os dados necessários para o funcionamento do software, coletando novos registros e exibindo também os antigos.
