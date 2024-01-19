import mysql.connector
import os
import logging
import traceback

log = logging.getLogger()
log.setLevel(logging.INFO)

config = {
    'host': 'localhost',
    'user': os.environ['MYSQL_ID'],
    'passwd': os.environ['MYSQL_PW'],
    'db': os.environ['MYSQL_DB_QUIZ']
}


# DB接続情報
def conn_db():
    conn = mysql.connector.connect(**config)
    return conn


# 受け取ったSQLを実行する
def try_conn(conn, sql, params=None):
    res = []
    cursor = conn.cursor(prepared=True)
    try:
        # SQLにパラメータを渡す場合
        if params:
            log.info(f"sql: {sql}, params: {params}")
            cursor.execute(sql, params)
        else:
            log.info(f"sql: {sql}")
            cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            res.append(row)
        return res

    except Exception as e:
        log.error(traceback.format_exc())
        log.error(f"sql: {sql}")
        raise e

    finally:
        cursor.close()
