import pandas as pd
import datetime as dt
import smtplib
import random
email="replacewithsenderemail"
psw="replacewithpassword"
data = pd.read_csv("bday.csv")
dictr={(row["name"],row["email"]):(row["day"],row["month"]) for (index,row) in data.iterrows()}
currentdt=(dt.datetime.now().day,dt.datetime.now().month)
namnem=[n for n,m in dictr.items() if(m==currentdt)]
letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
for emnm in namnem:
    letter=random.choice(letters)
    with open (letter,"r") as cur:
        letterd=cur.read()
    letterd=letterd.replace("[NAME]",emnm[0])
    message=f"Subject:Happy Birthday!!!\n\n{letterd}"
    message=message.encode("utf-8")

    if(len(namnem)>0):
        connection=smtplib.SMTP_SSL("smtp.gmail.com")#Smtp address if your mail provider
        connection.login(user=email,password=psw)
        connection.sendmail(from_addr=email,to_addrs=emnm[1],msg=message)
        connection.close()

