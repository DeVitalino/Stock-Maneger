from produto import Produto
from venda import Venda


def menu():
    p = Produto()
    v = Venda()

    while True:
        print("\n=== MENU ===")
        print("1. CADASTRAR")
        print("2. LISTAR")
        print("3. ATUALIZAR ")
        print("4. REMOVER")
        print("5. REGISTAR")
        print("0. SAIR")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            quantidade = int(input("Quantidade: "))
            preco = int(input("Preço: "))
            p.cadastrar_produto(nome, descricao, quantidade, preco)
            print("Produto cadastrado com sucesso.")

        elif opcao == "2":
            produtos = p.listar_produtos()
            for prod in produtos:
                print(prod)

        elif opcao == "3":
            produto_id = int(input("ID do produto: "))
            nova_qtd = int(input("Nova quantidade: "))
            p.atualizar_quantidade(produto_id, nova_qtd)
            print("Quantidade atualizada.")

        elif opcao == "4":
            produto_id = int(input("ID do produto a remover: "))
            p.remover_produto(produto_id)
            print("Produto removido.")

        elif opcao == "5":
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade vendida: "))
            sucesso = v.registrar_venda(produto_id, quantidade)
            if sucesso:
                print("Venda registrada.")
            else:
                print("Erro: Estoque insuficiente ou produto não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
