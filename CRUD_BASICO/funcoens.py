from conexão import conectar


def verificador(tabela="", coluna="", valor="" ):
    comando_pesquisar = f"SELECT * FROM {tabela} WHERE {coluna} = %s;"
    comando_criar = f"INSERT INTO {tabela} ({coluna}) VALUES (%s);"

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(comando_pesquisar,(valor,))
    resultado = cursor.fetchone()

    cursor.close()
    banco.close()
    

    if resultado is not None:
        id_categoria = resultado[0]
        return id_categoria
    else:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(comando_criar,(valor,))
        banco.commit()
        id_categoria = cursor.lastrowid

        cursor.close()
        banco.close()
        return id_categoria

    

class Produto:
    def __init__(self, nome, preco, estoque, categoria_nome, marca_nome):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria_nome = categoria_nome
        self.marca_nome = marca_nome

    def cadastrar_produto(self):
        banco = conectar()
        cursor = banco.cursor()

        id_categoria = verificador("tbl_Categoria", "nome", self.categoria_nome)
        id_marca = verificador("tbl_Marca", "nome", self.marca_nome)

        comando_inserir = f"INSERT INTO tbl_Produto (nome, preco, estoque, id_categoria, id_marca) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(comando_inserir, (self.nome, self.preco, self.estoque, id_categoria, id_marca))
        banco.commit()

        cursor.close()
        banco.close()

