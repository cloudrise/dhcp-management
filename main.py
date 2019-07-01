import mysql.connector
import argparse
import private.config ## edit here to config


def get_all_users():
    connection = mysql.connector.connect(**private.config.DATABASE_CONFIG)
    cursor = connection.cursor()
    query = ("SELECT id, first_name, last_name, hex(mac), inet_ntoa(ip) FROM clients")
    cursor.execute(query)

    user_list = cursor.fetchall()

    connection.close()

    return user_list

def format_printable_mac(mac):
    mac = str.upper(mac)
    return ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))

def print_user_details():
    user_list = get_all_users()
    for user in user_list:
        print(user[0], user[1], user[2], format_printable_mac(user[3]), user[4])

def add_new_user():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    mac = input("MAC: ")

    query = ("INSERT INTO clients"
             "(first_name, last_name, ip, mac)" 
             "VALUES (%(first_name)s, %(last_name)s, IFNULL((SELECT MAX(t.ip)+1 FROM clients AS t), INET_ATON(%(start_ip)s)), UNHEX(%(mac)s))")
    data_query = {
        'first_name' : first_name,
        'last_name' : last_name,
        'start_ip' : private.config.START_IP,
        'mac' : mac
    }

    connection = mysql.connector.connect(**private.config.DATABASE_CONFIG)

    cursor = connection.cursor()

    cursor.execute(query, data_query)

    connection.commit()
    cursor.close()
    connection.close()

    print('stop here')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Select one of the following action: list")
    args = parser.parse_args()

    if args.action == "list":
        print_user_details()

    elif args.action == "add":
        add_new_user()

if __name__ == '__main__':
    main()