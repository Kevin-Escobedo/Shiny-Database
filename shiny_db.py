import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("test.db")
    print("Database opened successfully")
