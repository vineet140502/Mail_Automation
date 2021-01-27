import pandas as pd
import smtplib
import time

# change here
email = ""
pwd = ""

#change column names and file name according to your data
data = pd.read_csv("leaders.csv")
rows = data.shape[0]
names = data["Player's Name"]
mails = data["Player's Email"] 
team = data['Team Name']
slot = data["Timing Slots"]

#outlook may be replaced by gmail/zoho/anything else according to your mail id
server = smtplib.SMTP("smtp.outlook.com", 587)
server.starttls()
server.login(email,pwd)


for i in range(rows):
    subject = "PMx 2021 Round 2 Presentation Slot Details."
    msg = """
Greetings from Team PMx,

In continuation of the previous email, we would like to share the details about your presentation with you.

Please find the slot allotted for your presentation below. Kindly note that a PM of the company will judge your live presentation. So, in order to comply with their time constraints, slots are finalised and not liable to change.

{} on 17th Jan 2021.

As has been stated in the PMx Round 2 Problem Statement, your team has to hand in two submissions: 

1) A written draft. 
2) A presentation deck. 

For that, we would like to remind you of the following deadlines:
    - The written draft has to be submitted on D2C handle by 16th Jan EOD.
    - The Presentation deck (in PDF format) must be submitted on the http://bit.ly/Pmx_submission by 16th Jan EOD.

If there's any confusion about the submission and presentation process, please have a look at the previous email or feel free to contact Team PMx.

On a final note, we believe that you are enthusiastic and confident about winning this competition and we wish you all the best for the same.

Reply to this mail if you've acknowledged your slot timing.

Regards,
Team PMx""".format(slot[i])
    
    body = "To: {}\r\nSubject: {}\n\n{}".format(mails[i],subject,msg)
    
    server.sendmail(email, mails[i],body)
    
    print("No. {} sent to mail id {} name {} of team {}".format(i,mails[i],names[i],team[i]))
    
    time.sleep(1)
server.quit()

###### Note #####
# the code may stop after sending some particular number of mails there could be two reason - 
# 1. login timeout - run the code again after changing the range of for loop appropriately 
# 2. mail limit exceeded (depends on your mail provider) - ooooops!!! lets call it a day you cant send more mails today not even directly from the app/site