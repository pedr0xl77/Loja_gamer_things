import mysql.connector
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
        comando_inserir = f"INSERT INTO tbl_Produto (nome, preco, estoque, id_categoria, id_marca) VALUES (%s, %s, %s, %s, %s);"

        id_categoria = verificador("tbl_Categoria", "nome", self.categoria_nome)
        id_marca = verificador("tbl_Marca", "nome", self.marca_nome)

        banco = conectar()
        cursor = banco.cursor()

        try:
            cursor.execute(comando_inserir, (self.nome, self.preco, self.estoque, id_categoria, id_marca))
            banco.commit()
            print("produto cadastrado com sucesso")
        except mysql.connector.errors.IntegrityError as ErroDuplicidade:

            if ErroDuplicidade.errno == 1062:
                print("esse produto ja existe")
                return
            else:
                print("erro de integridade")
            
        
        cursor.close()
        banco.close()

        


def validacao_universal(mensagem, tipo_esperado, positivo_obrigatorio=True):
    while True:
        try:
            entrada = input(mensagem).strip()

            #validação universal para verificar se o campo está vazio
            if not entrada:
                print("Erro: O campo não pode ser vazio.")
                continue

            #validação para texto
            if tipo_esperado == str:
                if not any(c.isalpha() for c in entrada):
                    raise ValueError("O texto deve conter letras.")
                return entrada

            #troca de , por . para permitir a entrada de números decimais
            if tipo_esperado == float:
                entrada = entrada.replace(",", ".")
            #validação para números
            numero = tipo_esperado(entrada)

            if positivo_obrigatorio == True and numero <= 0:
                raise ValueError("O número deve ser maior que zero.")

            return numero
        except ValueError:
            if tipo_esperado == str:
                print("Erro: O texto deve conter letras.")
            elif tipo_esperado == int:
                print("Erro: Deve ser um numero inteiro maior que zero.")
            else:
                print("Erro: Deve ser um numero decimal maior que zero.")

def listar_produtos():
    comando_listar = "SELECT p.id_produto, p.nome, p.preco, p.estoque, c.nome AS categoria, m.nome AS marca FROM tbl_Produto p JOIN tbl_Categoria c ON p.id_categoria = c.id_categoria JOIN tbl_Marca m ON p.id_marca = m.id_marca ORDER BY p.id_produto;"

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(comando_listar)
    produtos = cursor.fetchall()

    cursor.close()
    banco.close()

    if not produtos:
        print("Não ha produtos cadastrados")
        return
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}, Categoria: {produto[4]}, Marca: {produto[5]}")



def deletar_produto(id_produto):
    comando_deletar = "DELETE FROM tbl_Produto WHERE id_produto = %s;"

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(comando_deletar, (id_produto,))
    banco.commit()

    cursor.close()
    banco.close()


def editar_produto(id_produto, novo_nome, novo_preco, novo_estoque, nova_categoria_nome, nova_marca_nome):
    comando_editar = "UPDATE tbl_Produto SET nome = %s, preco = %s, estoque = %s, id_categoria = %s, id_marca = %s WHERE id_produto = %s;"

    id_categoria = verificador("tbl_Categoria", "nome", nova_categoria_nome)
    id_marca = verificador("tbl_Marca", "nome", nova_marca_nome)

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(comando_editar, (novo_nome, novo_preco, novo_estoque, id_categoria, id_marca, id_produto))
    banco.commit()

    cursor.close()
    banco.close()