#!/usr/bin/python
import pandas as pd
from datetime import date
import streamlit as st

import pyhdb
import snowflake.connector
import sys,traceback
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas


import hashlib

def conn_snowflake():
    conn = snowflake.connector.connect(
        user ='VENUGOPAL.MALIREDDY@SERVICENOW.COM',
        authenticator='externalbrowser',
        account='servicenow-edpdev',
        warehouse='SNOW_DEV_WH',
        database='SFD_EDW',
        schema ='Sourcing'
        )
    sf_cur = conn.cursor()
    return(sf_cur)

import pyhdb
def connect_hana():
    connection = pyhdb.connect(host="10.230.179.9",port=30115,user="Content_Migration",password="SJ0@1nWdspB$n")
    cursor = connection.cursor()
    return(cursor)

from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

def connect_snowflake():
    con = create_engine(URL(
        user ='VENUGOPAL.MALIREDDY@SERVICENOW.COM',
        authenticator='externalbrowser',
        account='servicenow-edpdev', 
        warehouse='DEV_DEVELOPER_WH',    # 'SNOW_DEV_WH',
        database=  'DEV_EDW_LS',         #'SFD_EDW',
        schema = 'FINANCE_AP_EM'        #'Sourcing'
        ))
    #sf_cur = con.cursor()
    return(con)



def read_data_hana(hana_tbl, hana_cur):
   cur_hana_tbl = hana_cur.execute("select * from _SYS_BIC." +hana_tbl)
   #st.write(" HANA Tble Q= ","select * from _SYS_BIC." +hana_tbl)
   df_hana_tbl = pd.DataFrame(cur_hana_tbl.fetchall())
   df_hana_tbl.columns  = [i[0] for i in cur_hana_tbl.description]
   return(df_hana_tbl)
   #cur_prline_hana= cursor.execute('select * from "SURF_RT"."U_PURCHASE_REQUEST_LINE_ITEMS"')   

def read_data_sf(sf_tbl, sf_cur):
   #sf_cur.execute('use "DEV_EDW_LS"') 
   cur_sf_tbl = sf_cur.execute("select * from " +sf_tbl)
   st.write ("SF SQL=","select * from " +sf_tbl)
   df_sf_tbl = cur_sf_tbl.fetch_pandas_all()   
   #df_sf_tbl = pd.read_sql(cur_sf_tbl, con =sf_cur )
   #df_sf_tbl.columns  = [i[0] for i in cur_sf_tbl.description]
   return(df_sf_tbl)
#def read_hana_data(hana_tbl, hana_cur):
    

# Snowflake
'''
def connectSnowflake:
    create_engine(URL(
        user ='VENUGOPAL.MALIREDDY@SERVICENOW.COM',
        authenticator='externalbrowser',
        account='servicenow-edpdev',
        warehouse='SNOW_DEV_WH',
        database='SFD_EDW',
        schema ='Sourcing'
))
'''

def write_snowflake(hana_cur):
    df_hana_tbl.to_sql(sf_tbl, con = engine,index=False, method = pd_writer)

def write_snowflake(hana_cur):
    df_hana_tbl.to_sql(sf_tbl, con = engine,index=False, method = pd_writer)

#----------ADMIN-------------------------------------------------------
def create_users():
	cur.execute('CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)')


def add_userdata(username,password):
	cur.execute('INSERT INTO users(username,password) VALUES (%s,%s)',(username,password))
	db.commit()

def login_user(username,password):
	cur.execute('SELECT * FROM users WHERE username =%s AND password = %s',(username,password))
	data = cur.fetchall()
	return data

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

#-----------------------------------------------------------------------
def create_table():
	cur.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')
	
#---------------------------------------PRODUCT -------------------------------------------------	
def read_sales_order():
	sql = "SELECT * FROM salesorderdetails" 
	cur.execute(sql)
	salesorder = cur.fetchall()
	#cur.close()
	return salesorder

def get_salesOrder(ordernum):
	sql = "SELECT * salesorderdetails where order_id ="+ordernum
	cur.execute(sql)
	salesorder = cur.fetchone()	
	#cur.close()
	return salesorder


	


