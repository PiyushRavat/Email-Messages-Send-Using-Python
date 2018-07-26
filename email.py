import smtplib

host = "smtp.gmail.com"
port = 587				
username = "youremailaddress@gmail.com"
password = "yourpassword"
from_email = username
to_list = ["anotheremailaddress@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hii These email send using PYTHON")
email_conn.quit()
