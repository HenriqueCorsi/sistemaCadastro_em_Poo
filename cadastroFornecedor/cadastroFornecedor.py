import mysql.connector
from classe import CadastroFornecedor

# Criando a minha conexão com o banco de dados
myconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='654321',
    database='projeto_cadastro',
)
# Estabelencendo os meus parametros para o objeto fornecedor01.
fornecedor01 = CadastroFornecedor('Imperial Soluções', '34.031.388/0001-00', 'Luiza', 'Luiza.Imperia@imperial.com',
                                  '1175454545', 'Av. Parnaíba, 454', 'São Paulo', 'SP')

# cursor -> será o responsavel por executar os comandos da minha conexão.
cursor = myconnection.cursor()

# Inserindo os parametros do meu objeto dentro da tabela "cadastro_fornecedor" , utilizando sintaxe sql.
comando = f'INSERT INTO cadastro_fornecedor (nome_fornecedor, cnpj_fornecedor, contato_fornecedor, email_fornecedor,' \
          f'telefone_fornecedor, endereço_fornecedor, cidade_fornecedor, uf_fornecedor    )' \
          f'VALUES ("{fornecedor01.razao_social}", "{fornecedor01.cnpj}", "{fornecedor01.contato}", ' \
          f'"{fornecedor01.email}", "{fornecedor01.telefone}", "{fornecedor01.enderco}", "{fornecedor01.cidade}", ' \
          f'"{fornecedor01.uf}")'

cursor.execute(comando)  # executando o comando
myconnection.commit()  # usado para quando for editar o banco de dados

# Encerrando a conexão com o banco de dado.
cursor.close()
myconnection.close()