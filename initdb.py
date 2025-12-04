import sqlite3
from helpers.logging import logger

DATABASE_NAME = "censoescolar.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)

    with open('schema.sql') as f:
        logger.info("Inciando a criação da tabela...")
        conn.executescript(f.read())
        
    conn.commit()
    logger.info("Tabela criada!")
    
    conn.close()

if __name__ == "__main__":
    create_tables()