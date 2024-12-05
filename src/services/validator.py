from email_validator import validate_email, EmailNotValidError
from flask import jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()


class Validator:
    @staticmethod
    def email_validation(email_request):
        try:
            # Check that the email address is valid
            emailinfo = validate_email(email_request, check_deliverability=True)

            # Get the normalized form of the email address
            normalized_email = emailinfo.normalized

            # print(f'{normalized_email}')

            return jsonify({"email": normalized_email}), 200

        except EmailNotValidError as e:
            # Handle invalid email input with a specific error message
            # print(str(e))
            return jsonify({"error": "Invalid email", "message": str(e)}), 400
    
    @staticmethod
    def send_verification_email(user_email, code):
        """Send a verification email with the code."""
        sender_email = os.getenv('SENDER_EMAIL')
        smtp_user = os.getenv('SMTP_USER')
        receiver_email = user_email
        password = os.getenv('SMTP_PASSWORD')  # Use an app password for Gmail or another service

        subject = "Email Verification"
        body = f"Your verification code is: {code}\nThis code will expire in 15 minutes."

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish the server connection (e.g., for Gmail)
            server = smtplib.SMTP('live.smtp.mailtrap.io', 587)
            server.starttls()
            server.login(smtp_user, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Verification email sent successfully!")
            return jsonify({"message": "Check your email for the verification code."}), 200
        except Exception as e:
            print(f"Error sending email: {e}")
            return jsonify({"error": f"Error sending email: {e}"}), 500

    @staticmethod
    def send_forgot_password_email(user_email, url_link):
        # Implement the logic to send the forgot password email
        """Send a verification email with the code."""
        sender_email = os.getenv('SENDER_EMAIL')
        smtp_user = os.getenv('SMTP_USER')
        receiver_email = user_email
        password = os.getenv('SMTP_PASSWORD')  # Use an app password for Gmail or another service

        subject = "Email Forgot Password"
        body = f"Please click the following link to reset your password: {url_link}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))


        try:
            # Establish the server connection (e.g., for Gmail)
            server = smtplib.SMTP('live.smtp.mailtrap.io', 587)
            server.starttls()
            server.login(smtp_user, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Forgot password email sent successfully!")
            return jsonify({"message": "Check your email for the forgot password link."}), 200
        except Exception as e:
            print(f"Error sending email: {e}")
            return jsonify({"error": f"Error sending email: {e}"}), 500