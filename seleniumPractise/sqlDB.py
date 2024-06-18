import os

import mysql.connector

MySqlUserName = os.getenv("MY_SQL_DB_USER", None)
MySqlPassword = os.getenv("DB_PASSWORD", None)
MySqlHost = os.getenv("MY_SQL_DB_HOST", None)
MySqlDb = os.getenv("MY_SQL_DB_NAME", None)


def create_db_conn_mysql():
    """
    :return: creates the dbControllers connection
    """
    mydb = mysql.connector.connect(host=MySqlHost, user=MySqlUserName, password=MySqlPassword, database=MySqlDb)
    return mydb


def getDataFromSQLQuery(queryString):
    """
    :param queryString:
    :return: returns the query results
    """
    myDbPtr = create_db_conn_mysql()
    myCursor = myDbPtr.cursor()
    myCursor.execute(queryString)

    res = myCursor.fetchall()
    res_list = []
    for each_row in res:
        res_list.append(each_row)

    return res_list


sqlstr  = "SELECT * From sys.EMP"
data_list = getDataFromSQLQuery(sqlstr)
print(data_list)

def insert_data_into_table(table_name=None, ):
    """Insert data into table"""
    myDbPtr = create_db_conn_mysql()
    myCursor = myDbPtr.cursor()

    insert_query = "INSERT INTO sys.{table_name} VALUES (2, 'amit', 'ee', 'swe', 003444, '01-12-2022');".format(
                    table_name)
