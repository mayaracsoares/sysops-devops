from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

# Configurações do banco vindas das variáveis de ambiente do Compose
HOST = os.environ.get("HOST", "banco")
NAME = os.environ.get("NAME", "mural")
USER = os.environ.get("USER", "operario")
PASSWORD = os.environ.get("PASSWORD", "treino123")


def obter_conexao_banco():
    # Loop para esperar o Postgres subir completamente antes do Flask tentar conectar
    for _ in range(30):
        try:
            conn = psycopg2.connect(host=HOST, database=NAME, user=USER, password=PASSWORD)
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("Não foi possível conectar ao banco de dados Postgres.")


# Inicializa a tabela no banco
def init_banco():
    conn = obter_conexao_banco()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS contador (
            id SERIAL PRIMARY KEY,
            visitas INT NOT NULL DEFAULT 0
        );
    """
    )
    # Garante que existe pelo menos uma linha de registro
    cur.execute("SELECT COUNT(*) FROM contador;")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO contador (visitas) VALUES (0);")
    conn.commit()
    cur.close()
    conn.close()


def mensagem_boas_vindas():
    return {"esquadrao": "Bem vindo!", "status": "Online"}


@app.route("/")
def home():
    conn = obter_conexao_banco()
    cur = conn.cursor()

    # Atualiza e busca o contador de forma persistente
    cur.execute("UPDATE contador SET visitas = visitas + 1 WHERE id = 1;")
    cur.execute("SELECT visitas FROM contador WHERE id = 1;")
    total_visitas = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    dados = mensagem_boas_vindas()

    return jsonify({**dados, "total_visitas": total_visitas})


if __name__ == "__main__":
    init_banco()
    app.run(host="0.0.0.0", port=5000)
