# 📦 Stock Manager

Sistema funcional para gerenciamento de produtos e vendas em estoque.  

---

## 🧰 Funcionalidades

- ✅ Cadastro de produtos
- ✅ Verificação de Produto por ID
- ✅ Listagem completa de produtos
- ✅ Atualização de estoque
- ✅ Remoção de produtos
- ✅ Registro de vendas com validação do estoque disponível
- ✅ Banco de dados local com criação automática de tabelas
- ✅ Interface via terminal com menu interativo


## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- SQLite (`sqlite3`) 

---

## 📁 Estrutura do Projeto

```bash
.
├── main.py               # Menu interativo e fluxo principal
├── produto.py            # Classe Produto: métodos para CRUD de produtos
├── venda.py              # Classe Venda: registro de vendas e controle de estoque
├── database.py           # Classe Database: criação e conexão com banco SQLite
├── estoque.db            # Banco de dados SQLite gerado automaticamente

## 📌 Observações

- Este projeto foi idealizado e implementado por Mateus Vitalino, como projeto do curso de Desenvolvimento Full Stack (Back-end).  
- Serve como aplicação prática dos conceitos aprendidos durante as aulas.  
- Estrutura modular e código claro para facilitar futuras melhorias e manutenções.

