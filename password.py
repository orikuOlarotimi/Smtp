import smtplib
import random
from flask import Flask, request, json, render_template, jsonify, redirect, url_for
import mongoengine as db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

database_name = "API"
DB_URI = URI
db.connect(host=DB_URI)


class UserDetails(db.Document):
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()

    def to_json(self):
        return {'username': self.username,
                'email': self.email,
                'password': self.password
                }


@app.route("/mongo", methods=["POST"])
def mongo():
    user1 = UserDetails(username="akak", email="ririri@gmail.com", password="sksksksk")
    user1.save()
    user2 = UserDetails(username="hahha", email="ajajaah@gmail.com", password="wuwuwuuw")
    user2.save()
    user3 = UserDetails(username="rotisko",email="orikuolarotimi12345@gmail.com", password="timi1ka")
    user3.save()
    return "successful"


@app.route("/")
def home():
    return render_template("diddy.html")


@app.route("/forgot_password", methods=["POST"])
def password():
    email = request.form.get('email')
    user = UserDetails.objects(email=email).first()

    if user:
        verification_code = random.randint(100000, 999999)
        smtp_server = server
        smtp_port = 587
        username = username
        password = password
        sender_email = email
        receiver_email = email

        msg = MIMEMultipart("alternative")
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "template234"

        html = f"""\
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Forgotten password</title>
                                </head>
                                <body>
                                 <h1>Password Reset Code</h1>
                                <p>Your code is: <strong>{verification_code}</strong></p>
                                </body>
                                </html>
                            """
        htmlPart = MIMEText(html, 'html')
        msg.attach(htmlPart)

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

            return render_template("confirm.html", email=email, verification_code=verification_code)
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")


    else:
        # Email does not exist
        return jsonify({"message": "Email not found"}), 404


@app.route("/confirm_verification", methods=["POST"])
def confirm_code():
    email = request.form.get('email')
    verification_code = request.form.get('verification_code')
    veri_code = request.form.get("veri_code")

    if verification_code != veri_code:
        return {"message": "code incorrect please try again"}
    else:
        return render_template("password.html", email=email)


@app.route("/change_password", methods=['POST'])
def change_password():
    email = request.form.get('email')
    new_password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    if new_password != confirm_password:
        return {"message": "password not same"}
    else:
        user = UserDetails.objects(email=email).first()
        if user:
            user.password = new_password
            user.save()
            return {"message": "Password updated successfully"}
        else:
            return {"message": "User not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
