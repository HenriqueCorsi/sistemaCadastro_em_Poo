import mysql.connector
from classe import CadastroClientesPF

# Criando a minha conexão com o Banco de Dados.
myconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='654321',
    database='projeto_cadastro',
)
# Estabelencendo os meus parametros para o objeto cliente01_pf.
cliente01_pf = CadastroClientesPF('Gabriel Alencar dos Santos', '488.103.975-71', '1995/06/01', '1196854587',
                                  'Gabriel.Alencar@gmail.com.com', 'Rua Parati, 404')

# cursor -> será o responsavel por executar os comandos da minha conexão.
cursor = myconnection.cursor()

# Inserindo os parametros do meu objeto dentro da tabela "cadastro_cliente_pf" , utilizando sintaxe sql.
comando = f'INSERT INTO cadastro_cliente_pf (nome_cliente_pf, cpf_cliente_pf, data_nascimento_cliente_pf, ' \
          f'telefone_cliente_pf, email_cliente_pf, endereço_cliente_pf) VALUES ("{cliente01_pf.nome_completo}", ' \
          f'"{cliente01_pf.cpf}", "{cliente01_pf.data_nasc}", "{cliente01_pf.telefone}", "{cliente01_pf.email}", ' \
          f'"{cliente01_pf.endereco}")'

cursor.execute(comando)  # executando o comando
myconnection.commit()  # usado para quando for editar o banco de dados

# Encerrando a conexão com o banco de dado.
cursor.close()
myconnection.close()
