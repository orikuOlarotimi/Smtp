import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587  # Use port 587 for TLS encryption
# Replace 'user@example.com' and 'password' with your Private Email credentials
username = "adegbamiyestephen2018@gmail.com"
password = "P4wVxFWmTO8hGn9S"
sender_email="noreply@50chats.com"
receiver_email = "fredrickbrudge001@gmail.com"


msg = MIMEMultipart("alternative")
msg["From"] = sender_email
msg["To"] = receiver_email # Replace with recipient email
msg["Subject"] = "template234"

html_content = """\
<html>
  <body>
    <span style="font-size: 18px; font-style: normal; font-weight: 500; margin-bottom: 30px;">
      Adegbamiye Stephen Has Invited you to take ownership of his app
    </span>

    <p style=>
        <button type="button" style="height: 50px; width: 200px; border-radius: 8px; color: white; cursor: pointer; border-width: 0px; background-color: blue;" class="ownershiptemplate-button button">
      Button
    </button>
    </p>

  </div>
    </body>
</html>
"""


part1 = MIMEText(html_content, "html")
msg.attach(part1)

try:
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption for secure communication
    # Log in to the SMTP server
    server.login(username, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    # Close the connection to the SMTP server
    server.quit()

    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")
