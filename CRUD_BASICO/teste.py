from funcoens import Produto,validacao_universal,listar_produtos,editar_produto,deletar_produto

#banco.commit() #edita o banco de dados
#cursor.fetchall() #pega todos os dados do banco de dados
#cursor.fetchone() #pega apenas o primeiro dado do banco de dados
#banco.close() #fecha a conexão com o banco de dados
#cursor.close() #fecha o cursor do banco de dados
#cursor.lastrowid #pega o id do último dado inserido no banco de dados
#cursor.execute(comando, (valor,)) #executa o comando no banco de dados


def menu():
    while True:
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Sair")

        escolha = validacao_universal("Escolha uma opção: ", int, positivo_obrigatorio = False)
        escolha = str(escolha)  # Converte a escolha para string para o match funcionar corretamente

        match escolha:
            case "1":
                nome = validacao_universal("Digite o nome do produto: ", str)
                preco = validacao_universal("Digite o preço do produto: ", float)
                estoque = validacao_universal("Digite a quantidade em estoque: ", int)
                categoria_nome = validacao_universal("Digite o nome da categoria: ", str)
                marca_nome = validacao_universal("Digite o nome da marca: ", str)

                produto = Produto(nome, preco, estoque, categoria_nome, marca_nome)
                produto.cadastrar_produto()

            case "0":
                print("Saindo do programa...")
                break

            case "2":
                listar_produtos()

            case "3":
                id_produto = validacao_universal("Digite o ID do produto a ser atualizado: ", int)
                novo_nome = validacao_universal("Digite o novo nome do produto: ", str)
                novo_preco = validacao_universal("Digite o novo preço do produto: ", float)
                novo_estoque = validacao_universal("Digite a nova quantidade em estoque: ", int)
                nova_categoria_nome = validacao_universal("Digite o novo nome da categoria: ", str)
                nova_marca_nome = validacao_universal("Digite o novo nome da marca: ", str)

                editar_produto(id_produto, novo_nome, novo_preco, novo_estoque, nova_categoria_nome, nova_marca_nome)
                print("Produto atualizado com sucesso!")

            case "4":
                id_produto = validacao_universal("Digite o ID do produto a ser deletado: ", int)
                deletar_produto(id_produto)
                print("Produto deletado com sucesso!")
menu()