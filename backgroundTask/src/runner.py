import os, time
import psycopg2
import traceback

def run(conn):
    print("hello, task")

def setup():
    print("setup")

    user = os.environ["DBUSER"]
    pwd = os.environ["DBPASS"]
    host = os.environ["DBHOST"]
    dbname = os.environ["DBNAME"]

    try:
        conn = psycopg2.connect(f"dbname='{dbname}' user='{user}' host='{host}' password='{pwd}'")
        print("connected")
    except:
        print(traceback.format_exc())
    
    while True:
        run(conn)
        time.sleep(3)

if __name__ == "__main__":
    try:
        setup()
    except:
        print(traceback.format_exc())
