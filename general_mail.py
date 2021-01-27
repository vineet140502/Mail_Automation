import pandas as pd
import smtplib
import time
from PIL import Image

# change here
email = ""
pwd = ""

#change column names and file name according to your data
data = pd.read_csv("Mail_PMx.csv")
rows = data.shape[0]
names = data["Name"]
mails = data["Email"]
links = data["Links"]

#outlook may be replaced by gmail/zoho/anything else according to your mail id
server = smtplib.SMTP("smtp.outlook.com", 587)
server.starttls()
server.login(email,pwd)

for i in range(rows):
    subject = "Exciting News Ahead..."
    msg = """
Hello 

Greetings from E-cell IIT Guwahati, We very excited to share with you that in addition to the offer letter and certificates(which will be given after completion of UDGAM'21) we have partnered with cerifyme.online to provide you online badges that can be shared on Social Media. 

These badges are clickable and unique to every Campus ambassador. We encourage you to click on your unique badge link and share it on social media along with a few words. Sharing your badges on Linkedin is highly recommended.

Please find your badge link: . (In case of any confusion, please post your query on the WhatsApp group)

Regards, 

Team Public Relations, 

Udgam'21."""
    
    body = "Subject: {}\n\n{}".format(subject,msg)
    
    server.sendmail(email, mails[i],body)
    
    print("sent to no {} name {}".format(i+1,names[i]))
    
    time.sleep(1)
server.quit()

###### Note #####
# the code may stop after sending some particular number of mails there could be two reason - 
# 1. login timeout - run the code again after changing the range of for loop appropriately 
# 2. mail limit exceeded (depends on your mail provider) - ooooops!!! lets call it a day you cant send more mails today not even directly from the app/site