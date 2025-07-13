from database import Database

class Produto:
    def __init__(self):
        self.db = Database().get_connection()

    def cadastrar_produto(self, nome, descricao, quantidade, preco):
        cursor = self.db.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, descricao, quantidade, preco)
            VALUES (?, ?, ?, ?)
        ''', (nome, descricao, quantidade, preco))
        self.db.commit()

    def listar_produtos(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM produtos")
        return cursor.fetchall()

    def atualizar_quantidade(self, produto_id, nova_quantidade):
        cursor = self.db.cursor()
        cursor.execute('''
            UPDATE produtos
            SET quantidade = ?
            WHERE id = ?
        ''', (nova_quantidade, produto_id))
        self.db.commit()

    def remover_produto(self, produto_id):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
        self.db.commit()
