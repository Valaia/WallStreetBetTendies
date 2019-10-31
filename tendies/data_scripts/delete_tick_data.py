import collections
import datetime
import json
import psycopg2
import requests
import urllib


def delete_stock_tick_from_db(stock_symbols):
    conn = psycopg2.connect(
        host="fa19-cs411-048.cs.illinois.edu",
        database="wsb_tendies",
        user="wsb_django_user",
        password="411_wsb_tendies"
    )
    cur = conn.cursor()

    for stock_symbol in stock_symbols:
        delete_stock_tick_data_query = \
            'DELETE FROM StockTickData WHERE stock_symbol=\'{}\''.format(stock_symbol)
        cur.execute(delete_stock_tick_data_query)
        conn.commit()

    cur.close()

'''
try:
    delete_stock_tick_from_db(['FB', 'AMZN'])
except (Exception, psycopg2.DatabaseError) as error:
    print('ERROR with deleting tick data: ', error)
'''
