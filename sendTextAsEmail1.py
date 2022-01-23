# 1st log into your account, then click on the icon of your account, then click
# on "Manage your Google Account" button, so a new window will be opened. Now
# click on the "Security" located on left side.So right pane will be changed,then
# scroll down below and click on "Less secure app access", so this will be opened
# Now click on the button in front of "Allow less secure apps: OFF" to make it ON.
# Then run the below code, so it will send mail.

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('sadiq114@gmail.com','11041975')#server.login('sender email','password')

server.sendmail('sadiq114@gmail.com','sadiqakbar@uop.edu.pk','Mail from python')#server.sendmail('sender email','Receiver email','Your message here')
print('Mail sent')# To know wether email was sent
