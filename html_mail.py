import pandas as pd
import smtplib
import time
from email.message import EmailMessage

# change here
email = ""
pwd = ""

#change column names and file name according to your data
data = pd.read_csv("Mail_PMx.csv")
rows = data.shape[0]
names = data["Name"]
mails = data["Email"]

for i in range(rows):
    msg = EmailMessage()
    msg['Subject'] = 'Exciting News Ahead...'
    msg['From'] = email
    msg['To'] = mails[i]

    body = """

<!DOCTYPE html>
<html>

<body>
    <div class=" zm_-550953636255200717_parse_-5694217386090934512">
    <div class="x_741760336outerbox" style="padding-top: 30px; padding-bottom: 30px; background-color: rgb(240, 240, 240);">
        <div class="x_741760336content" style="padding: 15px; border-top: 4px rgb(30, 144, 255) solid; border-bottom: 4px rgb(30, 144, 255) solid; background-color: white;">
            <div>
                Hello {}!
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                <b>Does your brain process ideas and ways to make products better?</b> Do you want to be the beacon everyone else follows? Do you see yourself in the future among these genius sapiens with powerful insight, brilliant industry knowledge, and killer strategy?
 
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                <b>Then Product Management is for you!</b>
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                
 
                <b> But do you know, what is Product Management? </b>
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
 
Notable individuals like Sundar Pichai (former CEO of Google), Reid Hoffman (founder of LinkedIn), Marissa Mayer (former CEO of Yahoo) were all product managers in the initial phase of their career, before rising to more esteemed positions. 
            <br>
            </div>
            <div>
                <br>
            </div>
            <div>
Product Management is a role within a company that is responsible for product’s overall success, starting from dealing with new product development, business justification, planning, verification, forecasting, pricing, product launch, and marketing of a product or products at all stages of the product life cycle. 
 
 
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                
            
                <img class="imgs" src="https://www.mindtheproduct.com/wp-content/uploads/2011/07/what_is_a_product_manager.png" alt="" style="box-sizing: border-box;height: auto; max-width: 50%; display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%; ">
                
                <br>
            </div>
            
            <div>
                <br>
            </div>
            
            <div>
                Here, at IIT Guwahati, we present you with the opportunity to instill product management spirit in all you thinkers, tinkerers, problem solvers, and designers out there waiting and hoping for the right chance. 
 <br><br>
<b>Product Management Expedition — PMx</b> is a Product Case Study competition organized by Udgam, the E-Summit of IIT Guwahati. This time, PMx is bigger, better, and completely online. <b> Chances to win prizes worth 60K.</b>
 
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
           
           <br>
            </div>
            <div>
                <br>
            </div>
            <div class="x_741760336action-buttons" >
                <div class="x_741760336register" >
                    <button style = "background-color: #1E90FF; background-color: rgb(30, 144, 255); border-radius: 3px; padding: 10px 0; color: white; font-weight: 700; margin-right: 20px; width: 150px; text-align: center; margin: 0 auto;  border: none; padding: 15px; display: block; margin-left: auto; margin-right: auto;"> <a href="https://bit.ly/PMx2021" target="_blank" style = "color: white; text-decoration: none; font-size:15px" >
                        Register Here
                    </a></button>
                    
                </div>
            </div>
            <div>
                <br>
            </div>
            <div>
                <br>
            </div>
            
               <div>
          <b>Prerequisites</b>: What you need is only curiosity, a problem-solving attitude, and zeal to learn & improve and we shall take care of the rest. 
          <br> <br>
          Join us on slack <a href = "https://bit.ly/E-Cell_Product_Community" target="_blank" style = "color:blue;">
                       Here
                        </a> 
                        for regular updates and resources. Also, we will be providing mentorship from industry experts throughout the path.
                  <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                Please note:
                <list>
                    <ul>Team size should be 2 to 4</ul>
                    <ul>Teams can be inter-college. </ul>
                </list>
               
            </div>
            <div>
                <br>
            </div>
            <div>
                Regards,
                <br>
                Team PMx
                <br>
                Udgam 2021
                <br>
 
            </div>
           
            <div>
                <img class="imgs" src="https://i.imgur.com/YaWuCVH.png" alt="" style="box-sizing: border-box; max-width: 100%;">
                <br>
            </div>
            <div>
                <br>
            </div>
            <div>
                <hr style="opacity: 0.8;">
                <br>
            </div>
            <div style="margin-top: 5.0px;text-align: center;" class="x_741760336findon">
               <p> Find us on - </p>
              
            </div>
            <div class="x_741760336social" style="display: flex; text-align: center; margin: 0 auto; margin-top: 10px; width: 130px;">
                <div class="x_741760336facebook">
                    <a href="https://www.facebook.com/ecell.iitg" target="_blank">
                        <img style = "margin-right: 8px;" alt="" src="https://cdn.exclaimer.com/Handbook%20Images/facebook-icon_24x24.png">
                    </a>
                   
                </div>
                <div class="x_741760336twitter">
                    <a href="https://twitter.com/ecelliitg?s=20" target="_blank">
                        <img style = "margin-right: 8px;" alt="" src="https://cdn.exclaimer.com/Handbook%20Images/twitter-icon_24x24.png">
                    </a>
                   
                </div>
                <div class="x_741760336linkedin">
                    <a href="https://www.linkedin.com/company/13256987" target="_blank">
                        <img style = "margin-right: 8px;" alt="" src="https://cdn.exclaimer.com/Handbook%20Images/linkedin-icon_24x24.png">
                    </a>
                    
                </div>
                <div class="x_741760336instagram">
                    <a href="https://www.instagram.com/ecell_iitg/?igshid=1nd1y5qstu1wt" target="_blank">
                        <img style = "margin-right: 8px;" alt="" src="https://cdn.exclaimer.com/Handbook%20Images/instagram-icon_24x24.png">
                    </a>
                   
                </div>
            </div>
        </div>
    </div>
    <div>
        <br>
    </div>
</div>
</body>
</html>""".format(names[i])

    msg.add_alternative(body, subtype='html')

    #outlook may be replaced by gmail/zoho/anything else according to your mail id
    with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email, pwd)
        smtp.send_message(msg)
        smtp.quit()

    print("Sent to no. {} name {}".format(i,names[i]))

###### Note #####
# the code may stop after sending some particular number of mails there could be two reason - 
# 1. login timeout - run the code again after changing the range of for loop appropriately 
# 2. mail limit exceeded (depends on your mail provider) - ooooops!!! lets call it a day you cant send more mails today not even directly from the app/site