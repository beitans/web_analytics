from codecs import ignore_errors
from datetime import datetime
import time
import mysql.connector
from email.header import decode_header
import pandas as pd
import html2text
import re


def sql_mail_dump_header_processing(mydb):
    mycursor = mydb.cursor()

      
    print("Started SQL Lookup")
    mycursor.execute('SELECT * FROM raw_mail_dump WHERE processed_flag IS NULL OR processed_flag = 0 LIMIT 10;')
    df = pd.DataFrame(mycursor, columns=['mail_id','processed_flag','header_subject','header_from','header_to','header_timestamp','text_plain','text_html'])
    df2 = df.copy()
    df2.drop(['processed_flag','header_to','text_plain','text_html'],axis=1, inplace=True)
    df2['header_from_name'] = df2['header_from']
    df2.rename(columns={'header_from': 'header_from_mail'},inplace=True)
    #df2['header_from_name'] =  [re.sub(r'(a-z\d)','', str(x)) for x in df['header_from_mail']]

    for text in df2.iterrows():
      #  mails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        print(text)


    #df2['header_from_name'] =  [re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", df['header_from_mail'])]










    print(df2.head(10))
    header_df = pd.DataFrame(columns=['mail_id','header_subject','header_from_mail','header_from_name','header_timestamp'])
    print(df.head(10))



    #mydb.commit()

    print("Test")



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="newsletter_database"
)

sql_mail_dump_header_processing(mydb)


