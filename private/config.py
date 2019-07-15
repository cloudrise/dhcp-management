### EMAIL ###
SMTP_USERNAME = "my.email@gmail.com"
SMTP_PASSWORD = "my_password"
SMTP_PORT = 587
SMTP_SERVER = "smtp.gmail.com"
MAIL_TO = "receiver@domain.com"
MAIL_SUBJECT = "IP LIST"

### GLOBAL CONFIGURATION VARIABLES ###
PATH_MONTHLY_REPORTS = "./private/"
SH_NAME = "StudentHouse."
PATH_TO_USER_LIST_FILE = "/etc/dhcpd/dhcplist.conf"
START_IP="192.168.1.10"
DATABASE_HOST="127.0.0.1"
DATABSE_USER="login"
DATABASE_PASSWORD="password"
DATABASE_NAME="dhcp_clients"
TABLE_NAME="clients"

DATABASE_CONFIG = {
  'user': DATABSE_USER,
  'password': DATABASE_PASSWORD,
  'host': DATABASE_HOST,
  'database': DATABASE_NAME
}