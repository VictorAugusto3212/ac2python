from database import get_connection 

class ProdutoRepository:
    def create(self, nome: str, descricao: str, preco: float, estoque: int, categoria: str):
        conn = get_connection()
        cursor = conn.cursor()


    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES (?, ?, ?, ?, ?)",
        (nome, descricao, preco, estoque, categoria)
    )
    conn.commit()
    ultimo_id = cursor.lastrowid
    cursor.close
