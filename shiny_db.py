import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    database = "shiny_pokemon.db"
    start = """CREATE TABLE IF NOT EXISTS shiny_hunts (
        target text PRIMARY KEY, gen integer NOT NULL,
        encounters integer);"""
    conn = create_connection(database)

    if conn:
        create_table(conn, start)
    else:
        print("Error")
