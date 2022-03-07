import snowflake.connector as sf
import pandas as pd
import getpass

password = getpass.getpass("Enter your snowflake password: ")

# make changes as per your credentials
user='venu.malireddy'
account='servicenow-edpdev.snowflakecomputing.com'
database='SFD_DW'
warehouse='SNF_DEV_ROLE'
schema='SOURCING'
role='SNF_DEV_ROLE'

conn = sf.connect(user = venu.malireddy@servicenow.com
           password = Mvhmvhmvh1@3
           account = servicenow-edpdev.snowflakecomputing.com
    )
#---
def run_query(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
  
sql = f'use warehouse {warehouse}'
run_query(conn, sql)
    
try:
    warehouse_sql = 'use warehouse {}'.format(warehouse)
    run_query(conn, warehouse_sql)
    
    try:
        sql = 'alter warehouse {} resume'.format(warehouse)
        run_query(conn, sql)
    except:
        pass
    
    sql = 'use database {}'.format(database)
    run_query(conn, sql)
    
    sql = 'use role {}'.format(role)
    run_query(conn, sql)
    
    sql = f'use schema {schema}'
    run_query(conn, sql)

except Exception as e:
    print(e)
    

sql = 'select * from healthcare limit 20'
df = pd.read_sql(sql, conn)

df.tail(10)
