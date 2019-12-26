from config.app_config import get_conn


def rows_with_connection(sql):

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)

    return  cursor.fetchall()



