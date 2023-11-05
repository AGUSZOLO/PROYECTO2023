import mysql.connector

from config import DB_CONFIG


def get_connection():
    connection = mysql.connector.connect(**DB_CONFIG)

    return connection


def get_conn_n_cursor(dictionary=False, named_tuple=False):
    connection = get_connection()

    if dictionary:
        cursor = connection.cursor(dictionary=True)
    elif named_tuple:
        cursor = connection.cursor(named_tuple=True)

    return connection, cursor
