import pymssql

def get_conn():
    conn = pymssql.connect(host='localhost',
                           user='sa',
                           password='reallyStrongPwd123',
                           database='Linksmith')
    return conn