import mysql.connector
from classe import CadastroClientePJ

# Criando a minha conexão com o banco de dados
myconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='654321',
    database='projeto_cadastro',
)
# Estabelencendo os meus parametros para o objeto cliente01_pj.
cliente01_pj = cliente02_pj = CadastroClientePJ('Dell Produtos', '51.614.658/0001-24', 'Helena', '1138054511',
                                                'Helena.Dell@dell.com', 'Av. Nazaré, 478', 'Campinas')

# cursor -> será o responsavel por executar os comandos da minha conexão.
cursor = myconnection.cursor()

# Inserindo os parametros do meu objeto dentro da tabela "cadastro_cliente_pj" , utilizando sintaxe sql.
comando = f'INSERT INTO cadastro_cliente_pj (nome_cliente_pj, cnpj_cliente_pj, contato_cliente_pj, ' \
          f'telefone_cliente_pj, email_cliente_pj, endereço_cliente_pj, cidade_cliente_pj) ' \
          f'VALUES ("{cliente02_pj.nome_empresa}", ' \
          f'"{cliente01_pj.cnpj}", "{cliente01_pj.contato}", "{cliente01_pj.telefone}", "{cliente01_pj.email}", ' \
          f'"{cliente01_pj.endereco}", "{cliente01_pj.cidade}")'

cursor.execute(comando)  # executando o comando
myconnection.commit()  # usado para quando for editar o banco de dados

# Encerrando a conexão com o banco de dado.
cursor.close()
myconnection.close()

