import mysql.connector
import private.config ## edit here to config


def generate_user_list():

    connection = mysql.connector.connect(**private.config.DATABASE_CONFIG)
    cursor = connection.cursor()
    query = ("SELECT first_name, last_name, hex(mac), inet_ntoa(ip) FROM clients")
    cursor.execute(query)

    for (first_name, last_name, mac, ip) in cursor:
        print(first_name, last_name, mac, ip)


generate_user_list()