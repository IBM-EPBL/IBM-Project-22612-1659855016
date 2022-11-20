import ibm_db
print(1)
ibm_db_conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=fbm40876;PWD=3M8QIjLHz4KNYIYN;", "", "")
print(1)
import ibm_db_dbi
print(1)
conn = ibm_db_dbi.Connection(ibm_db_conn)
print(1)
conn.tables('SYSCAT', '%')
print(1)
