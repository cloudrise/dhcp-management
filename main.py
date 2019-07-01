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

def format_mac_address(mac):
    return ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))

def print_user_details():
    user_list = get_all_users()
    for user in user_list:
        print(user[0], user[1], user[2], format_mac_address(user[3]), user[4])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Select one of the following action: list")
    args = parser.parse_args()

    if args.action == "list":
        print_user_details()

if __name__ == '__main__':
    main()