import sqlite3

DATABASE_NAME = "censoescolar.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)

    with open('schema.sql') as f:
        conn.executescript(f.read())
        
    conn.commit()
    print("Tabela criada!")
    conn.close()

if __name__ == "__main__":
    create_tables()