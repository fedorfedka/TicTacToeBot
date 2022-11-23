import sqlite3

NULL = 0

def create_table(database_name :str):
    with sqlite3.connect(database_name) as db:
        sql = db.cursor()
        sql.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
            requester_username TEXT,
            accepter_username TEXT,
            is_requester_turn INT
        )
        """)
        db.commit()

def insert_into(requester_username :str, accepter_username :str, is_requester_turn :str, database_name :str):
    with sqlite3.connect(database_name) as db:
        sql = db.cursor()
        sql.execute(f"""
        INSERT INTO sessions VALUES(?, ?, ?)
        """, (
            requester_username,
            accepter_username,
            is_requester_turn
        ))
        db.commit()

def set_into(requester_username :str, database_name :str):
    with sqlite3.connect(database_name) as db:
        sql = db.cursor()
        sql.execute("""
        
        """)

def find_by_requester(requester_username :str, database_name :str) -> list:
    with sqlite3.connect(database_name) as db:
        sql = db.cursor()
        result = sql.execute(f"""
        SELECT requester_username, accepter_username, is_requester_turn FROM sessions WHERE requester_username='{requester_username}'
        """).fetchall()
        return result

def delete_by_requester(requester_username :str, database_name :str):
    with sqlite3.connect(database_name) as db:
        sql = db.cursor()
        sql.execute(f"""
        DELETE FROM sessions WHERE requester_username='{requester_username}'
        """)
