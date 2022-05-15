import sqlite3

# Criando Banco de Dados
Conexao = sqlite3.connect('Banco_Dados')

# Apontar para o banco
Cursor = Conexao.cursor()

# Criando uma tabela
# Cursor.execute(
#     'CREATE TABLE Minha_Tabela ( Data text, Nome text, Idade real )'
# )

# Fazer um commit
Conexao.commit()

# Inserir valores
Cursor.execute('INSERT INTO Minha_Tabela VALUES ( "27/01/2021", "Lucas", "30" )')
Cursor.execute('INSERT INTO Minha_Tabela VALUES ( "01/01/2021", "Odemir", "30" )')

import random

# Loop
for loop in range(10):

    # Gerando numeros aleatorios
    num = random.randint(18, 65)
    dia = random.randint(1, 28)
    mes = random.randint(1, 12)
    Cursor.execute(f'INSERT INTO Minha_Tabela VALUES ( "{dia}/{mes}/2021", "Lucas", {num} )')

# Query de consultas
Consulta = Cursor.execute(' SELECT * FROM Minha_Tabela').fetchall()

# Query usando "="
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome = 'Odemir'
    '''
).fetchall()

# Query usando ">"
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Idade > 30
    '''
).fetchall()

# Query usando BETWEEN
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Idade BETWEEN 20 AND 25
    '''
).fetchall()

print(Consulta)

