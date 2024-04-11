import smtplib
my_gmail="test@gmail.com"
password="mailpassword"  #App Passsword for details check readme file

connection=smtplib.SMTP("smtp.gmail.com")  # The SMTP server address, like "smtp.gmail.com,"
                                        # can differ depending on your service provider.
                                        #Please refer to the readme file for any potential errors
connection.starttls()
connection.login(user=my_gmail,password=password)
connection.sendmail(from_addr=my_gmail,
                    to_addrs="mailmewith123@gmail.com",
                    msg="subject:Wassup\n\n hi dude\n\n how do you do\n\n-varun")
connection.close()

#
# #if above code don't work then try below code which is little changed

import smtplib
my_gmail="test@gmail.com"
password="mailpassword"
connection=smtplib.SMTP_SSL("smtp.gmail.com",465)
# connection.starttls()
connection.login(user=my_gmail,password=password)
connection.sendmail(from_addr=my_gmail,
                    to_addrs="mailmewith123@gmail.com",
                    msg="subject:Wassup\n\n hi dude\n\n how do you do\n\n-varun")
connection.close()