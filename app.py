import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE_NAME = "censoescolar.db"

@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    statement = "SELECT * FROM tb_instituicao LIMIT 100 OFFSET 0"
    cursor.execute(statement)

    resultset = cursor.fetchall()

    instituicaoEnsinoResponse = []
    for row in resultset:
        instituicaoEnsinoResponse.append({
            "id": row[0],
            "codigo": row[1],
            "nome": row[2],
            "co_uf": row[3],
            "co_municipio": row[4],
            "qt_mat_bas": row[5],
            "qt_mat_prof": row[6],
            "qt_mat_eja": row[7],
            "qt_mat_esp": row[8]
        })

    conn.close()
    return jsonify(instituicaoEnsinoResponse), 200


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesById(id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    statement = "SELECT * FROM tb_instituicao WHERE id = ?"
    cursor.execute(statement, (id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        instituicaoEnsino = {
            "id": row[0],
            "codigo": row[1],
            "nome": row[2],
            "co_uf": row[3],
            "co_municipio": row[4],
            "qt_mat_bas": row[5],
            "qt_mat_prof": row[6],
            "qt_mat_eja": row[7],
            "qt_mat_esp": row[8]
        }
        return jsonify(instituicaoEnsino), 200
    return jsonify({"erro": "Instituição não encontrada"}), 404


@app.post("/instituicoesensino")
def setInstituicoesEnsino():
    instituicaoEnsino = request.get_json()

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    statement = """
        INSERT INTO tb_instituicao (codigo, nome, co_uf, co_municipio, qt_mat_bas, qt_mat_prof, qt_mat_eja, qt_mat_esp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(statement, (
        instituicaoEnsino["codigo"],
        instituicaoEnsino["nome"],
        instituicaoEnsino["co_uf"],
        instituicaoEnsino["co_municipio"],
        instituicaoEnsino["qt_mat_bas"],
        instituicaoEnsino["qt_mat_prof"],
        instituicaoEnsino["qt_mat_eja"],
        instituicaoEnsino["qt_mat_esp"]
    ))
    conn.commit()
    
    id_gerado = cursor.lastrowid
    conn.close()
    
    instituicaoEnsino["id"] = id_gerado
    return jsonify(instituicaoEnsino), 201


@app.put("/instituicoesensino/<int:id>")
def atualizarInstituicoesEnsino(id):
    instituicaoEnsino = request.get_json()
    
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    statement = """
        UPDATE tb_instituicao SET codigo = ?,nome = ?, co_uf = ?, co_municipio = ?, qt_mat_bas = ?, qt_mat_prof = ?, qt_mat_eja = ?, qt_mat_esp = ?
        WHERE id = ?   
    """
    cursor.execute(statement, (
        instituicaoEnsino["codigo"],
        instituicaoEnsino["nome"],
        instituicaoEnsino["co_uf"],
        instituicaoEnsino["co_municipio"],
        instituicaoEnsino["qt_mat_bas"],
        instituicaoEnsino["qt_mat_prof"],
        instituicaoEnsino["qt_mat_eja"],
        instituicaoEnsino["qt_mat_esp"],
        id
    ))
    conn.commit()
    conn.close()

    return jsonify(instituicaoEnsino), 200


@app.delete("/instituicoesensino/<int:id>")
def deletarInstituicoesEnsino(id):
    
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    statement = "DELETE FROM tb_instituicao WHERE id = ?"
    cursor.execute(statement, (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Instituição deletada!"}), 200
