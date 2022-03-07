# Snow Bridge ELT

from tkinter.ttk import Separator
import streamlit as st
import pandas as pd 

import streamlit.components.v1 as stc
from datetime import date
import ast
import matplotlib.pyplot as plt
#import seaborn as sns
from st_aggrid import AgGrid
from db_functions.db_functions import * 

# Data Viz Pkgs
#import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

import pyhdb
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine


hdr = st.columns((1,1))
with hdr[0]:
    pass
 	#st.image('./images/snowbridge.jfif')
    
with hdr[1]:
    title_container = st.container()

col1, col2 = st.columns([1, 5])
image = ''
with title_container:
    with col1:
        sb_img = './images/snowbridge.jfif'
        st.image(sb_img, width=120)
        #st.write("")
    with col2:
    	#st.markdown(" ## Hana")
    	col2.markdown(
    		f"<h1 style='text-align: center; color: #0C2E4F; background-color:#80B6A1; '>SNOW Bridge</h1>",
    		   		unsafe_allow_html=True,
    		
    		)

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:8px;border-radius:10px">

    <img src="./imags/salesorder.png" alt="" width="50" height="50">
    <h2 style="color:white;text-align:center;">Product Sales and Profit Management</h1>
    </div>

    """
    #<p style="color:white;text-align:center;">Digital House</p>
def main():
    st.write(" ")
    user = st.sidebar.text_input('User Name')
    passwd = st.sidebar.text_input('Password',type='password')
	#col1, col2 = st.sidebar.columns([1,1])
    
    if st.sidebar.button('Login'):        
        #create_usertable()
        hashed_pswd = make_hashes(passwd)
        global result
        result = login_user(user,check_hashes(passwd,hashed_pswd))
        st.session_state.authorized = 'yes'

        if result:
            st.sidebar.write( "User loggedin successfully")
            st.session_state.authorized = 'yes'

        else:
            st.sidebar.info(" Please check user id / password")
            authorized = 'no'
            st.session_state.authorized = 'no'
            
        if st.sidebar.button('SignUp'):
            #create_users()
            #hashed_pswd = make_hashes(passwd)
            #add_userdata(user,hashed_pswd)

            st.sidebar.write(' new user created')
            st.sidebar.info("Go to Login Menu to login")
     
    
	#-----------------------------------------------
    h2s_extract=st.sidebar.button(" Extract and Load")
	# st.sidebar.write("----------------------------")

    menu = ["Create","Read","Update","Delete"]
    #md = st.sidebar.selectbox("Menu",master_data)
    choice = st.sidebar.radio("Menu",menu)
    
    #st.sidebar.write("----------------------------")
    analysis = st.sidebar.button("Analyze ")
    help=st.sidebar.button("   Help")
    st.sidebar.write("----------------------------")
	
    #-------------------------------------------------------------------------#
    #if  h2s_extract:
    placeholder = st.empty()
    with st.form(key="extform",clear_on_submit=False):
        st.markdown("#")
        #with st.expander(" ",expanded=True):
        cont = st.container()
        if cont:
            ext_col= st.columns((1,1))
            with ext_col[0]:  
                sap_img = './images/sap.jfif'
                st.image(sap_img, width=114, caption='HANA') 
                #st.markdown("## HANA")
                hana_tbl = st.text_input("Enter HANA Table")
                
                #st.write("HANA = ", hana_tbl)
                hana_data = st.checkbox("Display HANA data")

            with ext_col[1]:                    
                sf_img = './images/snowflake.png'
                st.image(sf_img, width=70, caption='Snowflake')
                #st.markdown("## Snowflake")
                sf_tbl = st.text_input("Enter Snowflake Table",hana_tbl.split('.')[-1])
                #sf_tbl = sf_tbl[-2]
                #st.write("SF = ", sf_tbl)
                sf_data = st.checkbox("Display Snowflake data")
        
        extract = st.form_submit_button("Extract")


        #----------------------------------------------------------------------------
      
        # if hana_data:
        #     hana_cur = connect_hana()
        #     df_hana_data = read_data_hana(hana_tbl,hana_cur)
        #     st.write(df_hana_data.head(10))
        # if sf_data:
        #     df_sf_data = read_data_sf(sf_tbl,hana_tbl)
        #     st.write(df_sf_data)
        

        if extract:
            if hana_data:
            # Connect to HANA
                hana_cur = connect_hana()
                # Read Data
                df_hana_data = read_data_hana(hana_tbl,hana_cur)
                st.write(df_hana_data)

            if sf_data:
                sf_curr = conn_snowflake()
                df_sf_data = read_data_sf(sf_tbl,sf_curr)
                st.write(df_sf_data)
                # Connect to snowflake
                #connect_snowflake()
                # Write data to snowflake
                #write_snowflake(sf_tbl,sf_cur)



	

	#elif choice == "Delete":
	#	st.write(" Are yo sure you want to delete ?")



if __name__ == '__main__':
	main()
