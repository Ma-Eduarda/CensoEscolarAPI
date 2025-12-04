import sqlite3
from flask import Flask, request, jsonify
from marshmallow import ValidationError

from models.InstituicaoEnsino import InstituicaoEnsinoSchema
from helpers.logging import logger
from helpers.application import app
from helpers.database import get_conn


@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200

@app.get("/instituicoesensino/ranking/<int:ano>")
def getInstituicoesEnsinoRanking(ano: int):
    
    logger.info(f"get - /instituicoesensino/ranking/{ano}")
    
    if ano not in [2022, 2023, 2024]:
        logger.error(f"Ano inválido: {ano}")
        return jsonify({"erro": "Ano inválido. Use 2022, 2023 ou 2024."}), 400

    try:
        conn = get_conn()
        cursor = conn.cursor()

        statement = """
            SELECT *
            FROM tb_instituicao
            WHERE nu_ano_censo = ?
            ORDER BY qt_mat_total DESC
            LIMIT 10
        """

        cursor.execute(statement, (ano,))
        resultset = cursor.fetchall()

        instituicaoEnsinoResponse = []
        ranking = 1 
        for row in resultset:
            instituicaoEnsinoResponse.append({
                "id": row["id"],
                "nu_ano_censo": row["nu_ano_censo"],
                "no_entidade": row["no_entidade"],
                "co_entidade": row["co_entidade"],
                "no_uf": row["no_uf"],
                "sg_uf": row["sg_uf"],
                "co_uf": row["co_uf"],
                "no_municipio": row["no_municipio"],
                "co_municipio": row["co_municipio"],
                "no_mesorregiao": row["no_mesorregiao"],
                "co_mesorregiao": row["co_mesorregiao"],
                "no_microrregiao": row["no_microrregiao"],
                "co_microrregiao": row["co_microrregiao"],
                "no_regiao": row["no_regiao"],
                "co_regiao": row["co_regiao"],
                "qt_mat_bas": row["qt_mat_bas"],
                "qt_mat_prof": row["qt_mat_prof"],
                "qt_mat_eja": row["qt_mat_eja"],
                "qt_mat_esp": row["qt_mat_esp"],
                "qt_mat_fund": row["qt_mat_fund"],
                "qt_mat_inf": row["qt_mat_inf"],
                "qt_mat_med": row["qt_mat_med"],
                "qt_mat_zr_na": row["qt_mat_zr_na"],
                "qt_mat_zr_rur": row["qt_mat_zr_rur"],
                "qt_mat_zr_urb": row["qt_mat_zr_urb"],
                "qt_mat_total": row["qt_mat_total"],
                "nu_ranking": ranking
            })
            ranking += 1
            
        cursor.close()
        return jsonify(instituicaoEnsinoResponse), 200

    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500   
    

@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    
    logger.info("get - /instituicoesensino")
    
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 100))
    offset = (page - 1) * limit ## /instituicoesensino?page=1
    
    try:
        conn = get_conn()
        cursor = conn.cursor()
    
        statement = "SELECT * FROM tb_instituicao LIMIT ? OFFSET ?"
        cursor.execute(statement, (limit, offset))
        resultset = cursor.fetchall()

        instituicaoEnsinoResponse = []
        for row in resultset:
            instituicaoEnsinoResponse.append({
                "id": row["id"],
                "nu_ano_censo" : row["nu_ano_censo"],
                "no_entidade" : row["no_entidade"],
                "co_entidade" : row["co_entidade"],
                "no_uf" : row["no_uf"],
                "sg_uf" : row["sg_uf"],
                "co_uf" : row["co_uf"],
                "no_municipio" : row["no_municipio"],
                "co_municipio" : row["co_municipio"],
                "no_mesorregiao" : row["no_mesorregiao"],
                "co_mesorregiao" : row["co_mesorregiao"],
                "no_microrregiao" : row["no_microrregiao"],
                "co_microrregiao" : row["co_microrregiao"],
                "no_regiao" : row["no_regiao"],
                "co_regiao" : row["co_regiao"],
                "qt_mat_bas" : row["qt_mat_bas"],
                "qt_mat_prof" : row["qt_mat_prof"],
                "qt_mat_eja" : row["qt_mat_eja"],
                "qt_mat_esp" : row["qt_mat_esp"],
                "qt_mat_fund" : row["qt_mat_fund"],
                "qt_mat_inf" : row["qt_mat_inf"],
                "qt_mat_med" : row["qt_mat_med"],
                "qt_mat_zr_na" : row["qt_mat_zr_na"],
                "qt_mat_zr_rur" : row["qt_mat_zr_rur"],
                "qt_mat_zr_urb" : row["qt_mat_zr_urb"],
                "qt_mat_total" : row["qt_mat_total"]
            })
            
        cursor.close()
        return jsonify(instituicaoEnsinoResponse), 200
    
    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500        


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesById(id: int):
    
    logger.info(f"get - /instituicoesensino/{id}")
    
    try:
        conn = get_conn()
        cursor = conn.cursor()

        statement = "SELECT * FROM tb_instituicao WHERE id = ?"
        cursor.execute(statement, (id,))

        row = cursor.fetchone()

        if row:
            instituicaoEnsino = {
                "id": row["id"],
                "nu_ano_censo" : row["nu_ano_censo"],
                "no_entidade" : row["no_entidade"],
                "co_entidade" : row["co_entidade"],
                "no_uf" : row["no_uf"],
                "sg_uf" : row["sg_uf"],
                "co_uf" : row["co_uf"],
                "no_municipio" : row["no_municipio"],
                "co_municipio" : row["co_municipio"],
                "no_mesorregiao" : row["no_mesorregiao"],
                "co_mesorregiao" : row["co_mesorregiao"],
                "no_microrregiao" : row["no_microrregiao"],
                "co_microrregiao" : row["co_microrregiao"],
                "no_regiao" : row["no_regiao"],
                "co_regiao" : row["co_regiao"],
                "qt_mat_bas" : row["qt_mat_bas"],
                "qt_mat_prof" : row["qt_mat_prof"],
                "qt_mat_eja" : row["qt_mat_eja"],
                "qt_mat_esp" : row["qt_mat_esp"],
                "qt_mat_fund" : row["qt_mat_fund"],
                "qt_mat_inf" : row["qt_mat_inf"],
                "qt_mat_med" : row["qt_mat_med"],
                "qt_mat_zr_na" : row["qt_mat_zr_na"],
                "qt_mat_zr_rur" : row["qt_mat_zr_rur"],
                "qt_mat_zr_urb" : row["qt_mat_zr_urb"],
                "qt_mat_total" : row["qt_mat_total"]
            }
            return jsonify(instituicaoEnsino), 200
        
        cursor.close()
        return jsonify({"erro": "Instituição não encontrada"}), 404
    
    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500   


@app.post("/instituicoesensino")
def setInstituicoesEnsino():
    
    logger.info("post - /instituicoesensino")
    
    try:
        instituicaoData = request.get_json()
        
        schema = InstituicaoEnsinoSchema()
        instituicaoEnsino = schema.load(instituicaoData)
        
        qt_mat_total = [
            instituicaoEnsino["qt_mat_bas"], instituicaoEnsino["qt_mat_prof"],
            instituicaoEnsino["qt_mat_eja"], instituicaoEnsino["qt_mat_esp"],
            instituicaoEnsino["qt_mat_fund"], instituicaoEnsino["qt_mat_inf"],
            instituicaoEnsino["qt_mat_med"], instituicaoEnsino["qt_mat_zr_na"],
            instituicaoEnsino["qt_mat_zr_rur"], instituicaoEnsino["qt_mat_zr_urb"]
        ]
        
        qt_mat_total = sum(qt_mat_total)
        
        conn = get_conn()
        cursor = conn.cursor()
        
        statement = """
            INSERT INTO tb_instituicao (nu_ano_censo, no_entidade, co_entidade, no_uf, sg_uf, co_uf, no_municipio,
            co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao, no_regiao, co_regiao, qt_mat_bas, 
            qt_mat_prof, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_zr_na, qt_mat_zr_rur, qt_mat_zr_urb, qt_mat_total)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(statement, (
            instituicaoEnsino["nu_ano_censo"],
            instituicaoEnsino["no_entidade"],
            instituicaoEnsino["co_entidade"],
            instituicaoEnsino["no_uf"],
            instituicaoEnsino["sg_uf"],
            instituicaoEnsino["co_uf"],
            instituicaoEnsino["no_municipio"],
            instituicaoEnsino["co_municipio"],
            instituicaoEnsino["no_mesorregiao"],
            instituicaoEnsino["co_mesorregiao"],
            instituicaoEnsino["no_microrregiao"],
            instituicaoEnsino["co_microrregiao"],
            instituicaoEnsino["no_regiao"],
            instituicaoEnsino["co_regiao"],
            instituicaoEnsino["qt_mat_bas"],
            instituicaoEnsino["qt_mat_prof"],
            instituicaoEnsino["qt_mat_eja"],
            instituicaoEnsino["qt_mat_esp"],
            instituicaoEnsino["qt_mat_fund"],
            instituicaoEnsino["qt_mat_inf"],
            instituicaoEnsino["qt_mat_med"],
            instituicaoEnsino["qt_mat_zr_na"],
            instituicaoEnsino["qt_mat_zr_rur"],
            instituicaoEnsino["qt_mat_zr_urb"],
            qt_mat_total
        ))
        conn.commit()
        
        id = cursor.lastrowid
        
        instituicaoData.update({
            "id": id,
            "qt_mat_total": qt_mat_total
        })
        
        cursor.close()
        return instituicaoData, 201
    
    except ValidationError as err:
        logger.error(f"Validation error: {err.messages}")
        return err.messages, 400
    except sqlite3.Error as e:
        logger.error(f"SQLite error: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500


@app.put("/instituicoesensino/<int:id>")
def atualizarInstituicoesEnsino(id):
    
    logger.info(f"put - /instituicoesensino/{id}")
    
    try:
        instituicaoData = request.get_json()
        
        schema = InstituicaoEnsinoSchema()
        instituicaoEnsino = schema.load(instituicaoData)
        
        qt_mat_total = [
            instituicaoEnsino["qt_mat_bas"], instituicaoEnsino["qt_mat_prof"],
            instituicaoEnsino["qt_mat_eja"], instituicaoEnsino["qt_mat_esp"],
            instituicaoEnsino["qt_mat_fund"], instituicaoEnsino["qt_mat_inf"],
            instituicaoEnsino["qt_mat_med"], instituicaoEnsino["qt_mat_zr_na"],
            instituicaoEnsino["qt_mat_zr_rur"], instituicaoEnsino["qt_mat_zr_urb"]
        ]
        
        qt_mat_total = sum(qt_mat_total)
        
        conn = get_conn()
        cursor = conn.cursor()
        
        statement = """
            UPDATE tb_instituicao SET
                nu_ano_censo = ?, no_entidade = ?, co_entidade = ?, no_uf = ?, sg_uf = ?, co_uf = ?,
                no_municipio = ?, co_municipio = ?, no_mesorregiao = ?, co_mesorregiao = ?,
                no_microrregiao = ?, co_microrregiao = ?, no_regiao = ?, co_regiao = ?,
                qt_mat_bas = ?, qt_mat_prof = ?, qt_mat_eja = ?, qt_mat_esp = ?,
                qt_mat_fund = ?, qt_mat_inf = ?, qt_mat_med = ?,
                qt_mat_zr_na = ?, qt_mat_zr_rur = ?, qt_mat_zr_urb = ?, qt_mat_total = ?
            WHERE id = ?   
        """
        cursor.execute(statement, (
            instituicaoEnsino["nu_ano_censo"],
            instituicaoEnsino["no_entidade"],
            instituicaoEnsino["co_entidade"],
            instituicaoEnsino["no_uf"],
            instituicaoEnsino["sg_uf"],
            instituicaoEnsino["co_uf"],
            instituicaoEnsino["no_municipio"],
            instituicaoEnsino["co_municipio"],
            instituicaoEnsino["no_mesorregiao"],
            instituicaoEnsino["co_mesorregiao"],
            instituicaoEnsino["no_microrregiao"],
            instituicaoEnsino["co_microrregiao"],
            instituicaoEnsino["no_regiao"],
            instituicaoEnsino["co_regiao"],
            instituicaoEnsino["qt_mat_bas"],
            instituicaoEnsino["qt_mat_prof"],
            instituicaoEnsino["qt_mat_eja"],
            instituicaoEnsino["qt_mat_esp"],
            instituicaoEnsino["qt_mat_fund"],
            instituicaoEnsino["qt_mat_inf"],
            instituicaoEnsino["qt_mat_med"],
            instituicaoEnsino["qt_mat_zr_na"],
            instituicaoEnsino["qt_mat_zr_rur"],
            instituicaoEnsino["qt_mat_zr_urb"],
            qt_mat_total,
            id
        ))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            return jsonify({"erro": "Instituição não encontrada"}), 404
        
        instituicaoEnsino["id"] = id
        instituicaoEnsino["qt_mat_total"] = qt_mat_total
        
        cursor.close()
        return jsonify(instituicaoEnsino), 200
    
    except ValidationError as err:
        logger.error(f"Validation error: {err.messages}")
        return err.messages, 400
    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500   


@app.delete("/instituicoesensino/<int:id>")
def deletarInstituicoesEnsino(id):
    
    logger.info(f"delete - /instituicoesensino/{id}")
    
    try:
        conn = get_conn()
        cursor = conn.cursor()
        
        statement = "DELETE FROM tb_instituicao WHERE id = ?"
        cursor.execute(statement, (id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            return jsonify({"erro": "Instituição não encontrada"}), 404
        
        cursor.close()
        return jsonify({"message": "Instituição deletada!"}), 200

    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500   
