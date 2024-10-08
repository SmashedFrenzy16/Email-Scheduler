import smtplib
import schedule
import time

r_email = input("Enter in the recipient's email address: ")
    
# Email credentials
email = input("Enter in your email address: ")
email_pass = input("Enter in your email password: ")

# Email server
smtp = input("Enter in your email SMTP server: ")
port = input("Enter in your email SMTP port: ")

# Email message

message = input("Enter in your email message: ")

def send_email():
    
    server = smtplib.SMTP(smtp, port)

    server.starttls()

    server.login(email, email_pass)

    server.sendmail(email, r_email, message)

    server.quit()

# Email scheduled at a certain time every day
schedule.every().day.at("08:00").do(send_email) # Change time on this line

while True:
    schedule.run_pending()
    time.sleep(1)
