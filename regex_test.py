import re
import mysql.connector




mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="alert_database"
)


str_test = """=== Web - 4 neue Ergebnisse für [hackathon] ===

Code Connect Hackathon 2021
Now to get to the good stuff, below are the keys dates and information for
this years Hackathon! Hackathon Judges. Patrick Kremer. Staff Cloud ...
<https://www.google.com/url?rct=j&sa=t&url=https://vmwarecodeconnect.github.io/CodeConnect2021/hackathon/&ct=ga&cd=CAEYACoSMTg2MjA3MTMyMzY1NzQ3MDI0MhpmODc2NGIzNWUwODQzYmMwOmNvbTplbjpVUw&usg=AFQjCNGJwygJ9u1WuVDutfHoscj4NWH-uQ>

TechTogether Boston
We even have a prize for the hacker that attends the most events during the
hackathon. Did you know that last year TechTogether hackathons had an ...
<https://www.google.com/url?rct=j&sa=t&url=https://techtogether-boston.devpost.com/&ct=ga&cd=CAEYASoSMTg2MjA3MTMyMzY1NzQ3MDI0MhpmODc2NGIzNWUwODQzYmMwOmNvbTplbjpVUw&usg=AFQjCNG2nlALcJkhf73AZajR4hIN3LO0aA>

Application submission repository for Fixstars Amplify Hackathon 2021 -
GitHub
Application submission repository for Fixstars Amplify Hackathon 2021 -
GitHub - speQtrum/Fixstars_Amplify_Hackathon_2021: Application submission
...
<https://www.google.com/url?rct=j&sa=t&url=https://github.com/speQtrum/Fixstars_Amplify_Hackathon_2021&ct=ga&cd=CAEYAioSMTg2MjA3MTMyMzY1NzQ3MDI0MhpmODc2NGIzNWUwODQzYmMwOmNvbTplbjpVUw&usg=AFQjCNELIvYLhwTLG4oflSgf8xKEEVz4rg>

XiaoMi Off Campus Drive 2022 | XiaoMi ODE2CODE Hackathon 2022 - Freaky
Diodes
Xiaomi Off Campus Drive 2022, Xiaomi ODE2CODE Hackathon 2022, Mi
Recruitment Drive 2022, Latest Off Campus Drives for 2022 Batch, Xiaomi
Careers ...
<https://www.google.com/url?rct=j&sa=t&url=https://freakydiodes.com/xiaomi-off-campus-drive-2022-xiaomi-ode2code-hackathon-2022/&ct=ga&cd=CAEYAyoSMTg2MjA3MTMyMzY1NzQ3MDI0MhpmODc2NGIzNWUwODQzYmMwOmNvbTplbjpVUw&usg=AFQjCNEFkeQbgqxk5XRwyryhhzS8Y27ZTw>


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Diesen Google Alert nicht mehr erhalten:
<https://www.google.com/alerts/remove?source=alertsmail&hl=en&gl=US&msgid=MTg2MjA3MTMyMzY1NzQ3MDI0&s=AB2Xq4hc4JHGp7cEoWqSbS3lXZ9PGrlZzG9uBA0>

Weiteren Google Alert erstellen:
<https://www.google.com/alerts?source=alertsmail&hl=en&gl=US&msgid=MTg2MjA3MTMyMzY1NzQ3MDI0>

Melde dich an, um deine Alerts zu verwalten:
<https://www.google.com/alerts?source=alertsmail&hl=en&gl=US&msgid=MTg2MjA3MTMyMzY1NzQ3MDI0>






"""

def extract_and_store_alert_information(str_test, mydb):
    links = []
    titles = []

    str1 = str_test[3:150]
    zahl2 = str1.find("===")
    print(zahl2)
    str2= str_test[0:zahl2+4]
    zahl = [int(s) for s in str2.split() if s.isdigit()]
    zahl = zahl[0]
    topic = re.findall(r"\[(.*)\]",str2)
    topic = topic[0]
    print(str2)
    print(topic)

    for x in range(zahl):
        link = re.findall(r"(<)(.*)(>)",str_test)
        print(link[x][1])
        links.append(link[x][1])

    for x in range(zahl):
        title = re.findall(r"\n\n(.*)",str_test)
        print(title[x])
        titles.append(title[x])

    mycursor = mydb.cursor()
    print(type(topic))
    print("Extracted " + str(zahl) + " Alerts from the Group " + topic)

    for x in range(zahl):
        if topic == "hachathon":
            mycursor.execute(f'INSERT INTO hackathon_database(topic, headline, link) VALUES ("{topic}","{titles[x]}","{links[x]}" );')
        else:
            mycursor.execute(f'INSERT INTO hackathon_database(topic, headline, link) VALUES ("{topic}","{titles[x]}","{links[x]}" );')
        mydb.commit()
    
    print("Inserted Alerts into the database")

extract_and_store_alert_information(str_test, mydb)