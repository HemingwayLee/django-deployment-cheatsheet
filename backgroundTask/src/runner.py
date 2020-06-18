import os, sys
import psycopg2
import traceback
from time import sleep
from psycopg2 import sql

def doPreprocessing(id, conn, stmt, cursor):
    cursor.execute(stmt, (1, id))
    conn.commit()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def doOcr(id, conn,  stmt, cursor):
    cursor.execute(stmt, (2, id))
    conn.commit()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def annotate(id, conn, stmt, cursor):
    cursor.execute(stmt, (3, id))
    conn.commit()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def finish(id, conn, stmt, cursor):
    cursor.execute(stmt, (4, id))
    conn.commit()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def run(conn):
    print("task is running", flush=True)
    
    cursor = conn.cursor()
    queryStmt = sql.SQL("""
        UPDATE main_mytask SET processing = TRUE
        WHERE id = (
            SELECT id FROM main_mytask
            WHERE status = 0 AND processing = FALSE LIMIT 1)
        RETURNING id, filename, status""")

    updateStmt = sql.SQL("UPDATE main_mytask SET status = %s WHERE id = %s")

    try:
        cursor.execute(queryStmt)
        conn.commit()
        record = cursor.fetchone()

        print(record, flush=True)

        if record is None:
            print("no file uploaded", flush=True)
        else:
            doPreprocessing(record[0], conn, updateStmt, cursor)
            doOcr(record[0], conn, updateStmt, cursor)
            annotate(record[0], conn, updateStmt, cursor)
            finish(record[0], conn, updateStmt, cursor)
    except:
        print(traceback.format_exc(), flush=True)

def setup():
    print("setup", flush=True)

    user = os.environ["DBUSER"]
    pwd = os.environ["DBPASS"]
    host = os.environ["DBHOST"]
    dbname = os.environ["DBNAME"]

    try:
        conn = psycopg2.connect(f"dbname='{dbname}' user='{user}' host='{host}' password='{pwd}'")
        print("connected", flush=True)
    except:
        print(traceback.format_exc(), flush=True)
    
    while True:
        run(conn)
        sleep(3)

if __name__ == "__main__":
    try:
        setup()
    except:
        print(traceback.format_exc(), flush=True)
