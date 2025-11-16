import pandas as pd
import sqlite3

banco = sqlite3.connect("../censoescolar.db")

caminho_csv = "microdados_ed_basica_2024.csv"

for row in pd.read_csv(caminho_csv, sep=";", encoding="latin1", chunksize=50000):

    ie_nordeste = row[row["NO_REGIAO"] == "Nordeste"]

    csv = ie_nordeste[[
        "CO_ENTIDADE",
        "NO_ENTIDADE",
        "CO_UF",
        "CO_MUNICIPIO",
        "QT_MAT_BAS",
        "QT_MAT_PROF",
        "QT_MAT_EJA",
        "QT_MAT_ESP"
    ]]

    csv.columns = [
        "codigo",
        "nome",
        "co_uf",
        "co_municipio",
        "qt_mat_bas",
        "qt_mat_prof",
        "qt_mat_eja",
        "qt_mat_esp"
    ]

    csv = csv.fillna(0)
    csv.to_sql("tb_instituicao", banco, if_exists="append", index=False)

banco.close()

