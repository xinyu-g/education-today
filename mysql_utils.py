import pandas as pd
import queries as q
import mysql.connector
from sqlalchemy import create_engine, event
import consts as c
import numpy as np


def create_schema(queries):
    try:
        conn = mysql.connector.connect(
            host=c.HOST,
            user=c.USER,
            password=c.PASSWORD
        )

        cursor = conn.cursor()

        for query in queries:
            # print(query)
            cursor.execute(query)
        cursor.close()
        conn.commit()
    except mysql.connector.Error as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()


def insert(db, name, data):
    '''
    db: database name
    name: table name
    data: data entries to be inserted in pandas dataframe
    '''
    # conn = mysql.connector.connect(
    #         host=c.HOST,
    #         user=c.USER,
    #         password=c.PASSWORD,
    #         db=c.DB
    #     )

    # cursor = conn.cursor()

    # cols = ",".join(['`' + str(i) + '`' for i in data.columns.tolist()])

    # values = ",".join([r'%s'] * len(data.columns))

    # entries = [[None if type(y) == float and np.isnan(y) else y for y in x] for x in data.values]

    # sql = "INSERT INTO %s (%s) VALUES (%s)" % (
    #     name.lower(), cols, values)
    # print(sql)
    # cursor.executemany(sql, entries)
    # conn.commit()
    # for i, row in data.iterrows():
    #     sql = "INSERT INTO " + name.lower() + " (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    #     print(sql)
    #     cursor.execute(sql, tuple(row))

    #     conn.commit()
    conn_str = f'mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{db}'
    engine = create_engine(conn_str)

    # n = size
    # for da in [data[i:i+n] for i in range(0, data.shape[0], n)]:
    data.to_sql(con=engine, name=name.lower(), if_exists='append', index=False) #, method='multi')

    engine.dispose()
