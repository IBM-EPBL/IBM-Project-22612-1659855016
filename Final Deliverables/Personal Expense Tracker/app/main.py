import ibm_db
try:
    ibm_db_conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=fbm40876;PWD=3M8QIjLHz4KNYIYN;SECURITY=SSL;SSLServerCertificate=/home/user/Sprint 4/expense_project/DigiCertGlobalRootCA.crt;", "", "")
    print("Connected successfully!")
except:
    print("Connection failed!")

# conn = ibm_db_dbi.Connection(ibm_db_conn)
# print(1)
# conn.tables('SYSCAT', '%')
# print(1)
