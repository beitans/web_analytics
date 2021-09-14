from codecs import ignore_errors
import imaplib
from datetime import datetime
import time
import mysql.connector
import email
from email.header import decode_header

#Function to make Information ready for SQL Import
def decode_and_format(data_input):
    try:
        try:
            data_input = data_input.decode("utf-8",errors = "ignore")
        except:
            pass
        output_string = data_input.replace('"','').replace("'","")
    except:
        pass
    return output_string

def save_new_mail_to_mysql():
    print(str(datetime.now())+" ----- Looking for new Mail ----- ")

    #Mail connection
    email_user = 'beitans.alerts@gmail.com'
    email_pass = 'alert1!PW'
    mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
    mail.login(email_user, email_pass)
    mail.select('"Inbox"')
    #Mail search
    _,data = mail.search(None, 'UNSEEN') #   "UNSEEN" or "ALL" possible

    #Database connection
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="alert_database"
    )
    #Pointer onto database
    mycursor = mydb.cursor()

    #Mail Processing if new Mails are found
    for email_id in data[0].split():
        print(" ------------------  New Mail has been found  -------------------  ")
        _,fetched_data = mail.fetch(email_id, '(RFC822)' )
        raw_email = fetched_data[0][1].decode('utf-8', errors= "ignore")
        email_content = email.message_from_string(raw_email)
        header_list = []
        for header in ['subject', 'from', 'to', 'date']:
            decoded_header , _ = decode_header(email_content[header])[0]
            print("{}: {}".format(header,decode_and_format(decoded_header)))
            header_list.append(decode_and_format(decoded_header))
        text_html, text_plain = "" , ""
        for part in email_content.walk():
            if part.get_content_type() == "text/plain":
                text_plain = decode_and_format(part.get_payload(decode=True))
            if part.get_content_type() == "text/html":
                text_html = decode_and_format(part.get_payload(decode=True))
       
        print("Started SQL INSERT")
        mycursor.execute(f'INSERT INTO raw_mail_dump(header_subject , header_from, header_to, \
        header_timestamp, text_plain, text_html) VALUES ("{header_list[0]}","{header_list[1]}","{header_list[2]}"\
        ,"{header_list[3]}","{text_plain}","{text_html}" );')
        mydb.commit()
        print(" ------------ Mail Successfully recieved and stored ------------- ")


for x in range(10000):
    save_new_mail_to_mysql()
    time.sleep(30)

