from helpers.logging import logger
import pandas as pd
import sqlite3

banco = sqlite3.connect("censoescolar.db")

caminho_csv = "helpers/data/microdados_ed_basica_2022.csv"

colunas = [
    "NU_ANO_CENSO",
    "NO_ENTIDADE",
    "CO_ENTIDADE",
    "NO_UF",
    "SG_UF",
    "CO_UF",
    "NO_MUNICIPIO",
    "CO_MUNICIPIO",
    "NO_MESORREGIAO",
    "CO_MESORREGIAO",
    "NO_MICRORREGIAO",
    "CO_MICRORREGIAO",
    "NO_REGIAO",
    "CO_REGIAO",
    "QT_MAT_BAS",
    "QT_MAT_PROF",
    "QT_MAT_EJA",
    "QT_MAT_ESP",
    "QT_MAT_FUND",
    "QT_MAT_INF",
    "QT_MAT_MED",
    "QT_MAT_ZR_NA",
    "QT_MAT_ZR_RUR",
    "QT_MAT_ZR_URB"
]

logger.info("Iniciando extração de dados do csv...")

for chunk in pd.read_csv(caminho_csv, sep=";", encoding="latin1", chunksize=50000, low_memory=False):

    for col in colunas:
        if col not in chunk.columns:
            chunk[col] = 0
            
    df = chunk[colunas]
    
    df = df.fillna(0)
    
    df["QT_MAT_TOTAL"] = (
        df["QT_MAT_BAS"] +
        df["QT_MAT_PROF"] +
        df["QT_MAT_EJA"] +
        df["QT_MAT_ESP"] +
        df["QT_MAT_FUND"] +
        df["QT_MAT_INF"] +
        df["QT_MAT_MED"] +
        df["QT_MAT_ZR_NA"] +
        df["QT_MAT_ZR_RUR"] +
        df["QT_MAT_ZR_URB"]
    )
    
    
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("tb_instituicao", banco, if_exists="append", index=False)

logger.info("Extração concluída!")
logger.info("Fechando conexão com o banco de dados...")

banco.close()
