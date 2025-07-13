from database import Database
from datetime import datetime

class Venda:
    def __init__(self):
        self.db = Database().get_connection()

    def registrar_venda(self, produto_id, quantidade):
        cursor = self.db.cursor()

        # Atualizar estoque
        cursor.execute('SELECT quantidade FROM produtos WHERE id = ?', (produto_id,))
        resultado = cursor.fetchone()

        if resultado and resultado[0] >= quantidade:
            nova_quantidade = resultado[0] - quantidade
            cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto_id))

            # Registrar venda
            data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                INSERT INTO vendas (produto_id, quantidade, data_venda)
                VALUES (?, ?, ?)
            ''', (produto_id, quantidade, data_venda))

            self.db.commit()
            return True
        else:
            return False
