import smtplib, ssl, random, time

port = 465  # For SSL
password = input("Type your password and press enter: ")

#---------------------

sender_email = "beitans.newsletter@gmail.com"
receiver_email = "jscheifel98@web.de"

#------

message = """\
Subject: I love you :)

And here I am testing my programming skills ;)
You get """ + str(random.randint(1,10)) +" free kisses next time we see us !"


#---------------------

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login("beitans.newsletter@gmail.com", password)
        print("login successfull")
    except:
        print("login not successfull")
    for x in range(10):
        server.sendmail(sender_email, receiver_email, message)
        time.sleep(2)


print("Programm Finished! Thanks for Using Beitans Newsletter Analysis ;)")