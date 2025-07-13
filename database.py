import sqlite3

class Database:
    def __init__(self, db_name="estoque.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # Tabela de Produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        ''')

        # Tabela de Vendas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER,
                quantidade INTEGER NOT NULL,
                data_venda TEXT NOT NULL,
                FOREIGN KEY(produto_id) REFERENCES produtos(id)
            )
        ''')

        self.connection.commit()

    def get_connection(self):
        return sqlite3.connect("estoque.db")