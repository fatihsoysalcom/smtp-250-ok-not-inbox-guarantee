import smtplib
from email.mime.text import MIMEText
import os

# --- Configuration (replace with your actual details or environment variables) ---
# It's highly recommended to use environment variables for sensitive information.
# Example: export SMTP_SERVER="smtp.gmail.com"
# Example: export SMTP_PORT="587"
# Example: export SMTP_USERNAME="your_email@example.com"
# Example: export SMTP_PASSWORD="your_app_password"
# Example: export FROM_EMAIL="your_email@example.com"
# Example: export TO_EMAIL="recipient@example.com"

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com") # e.g., smtp.gmail.com, smtp.office365.com
SMTP_PORT = int(os.getenv("SMTP_PORT", 587)) # 587 for TLS, 465 for SSL
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

FROM_EMAIL = os.getenv("FROM_EMAIL", SMTP_USERNAME) # Often the same as username
TO_EMAIL = os.getenv("TO_EMAIL") # The recipient's email address

if not all([SMTP_USERNAME, SMTP_PASSWORD, TO_EMAIL]):
    print("Error: Please set SMTP_USERNAME, SMTP_PASSWORD, and TO_EMAIL environment variables.")
    print("Example: export SMTP_USERNAME='your_email@example.com'")
    print("Example: export SMTP_PASSWORD='your_app_password'")
    print("Example: export TO_EMAIL='recipient@example.com'")
    exit(1)

# --- Email Content ---
subject = "Test Email: SMTP 250 OK but maybe not inbox"
body = """
Merhaba,

Bu e-posta, SMTP 250 OK yanıtının e-postanın alıcının gelen kutusuna ulaştığı anlamına gelmediğini gösteren bir örnek için gönderilmiştir.
Python smtplib kütüphanesi ile gönderilmiştir.

Saygılarımla,
Örnek Uygulama
"""

msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL

try:
    print(f"Attempting to connect to SMTP server: {SMTP_SERVER}:{SMTP_PORT}")
    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.set_debuglevel(1) # Enable debug output to see SMTP conversation
        server.starttls() # Use TLS encryption
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        print(f"\nSending email from {FROM_EMAIL} to {TO_EMAIL}...")
        # The server.sendmail() call attempts to deliver the email.
        # If it completes without raising an exception, it means the recipient's
        # mail server accepted the email, typically responding with '250 OK'
        # at various stages of the SMTP conversation (visible in debug output).
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print("\nEmail sent successfully via SMTP!")
        print("--- IMPORTANT NOTE ---")
        print("The 'Email sent successfully via SMTP!' message indicates that the recipient's mail server")
        print("accepted the email (similar to an 'SMTP 250 OK' response, visible in debug output).")
        print("However, as discussed in the article, this DOES NOT guarantee that the email will reach")
        print("the recipient's inbox. It might still be filtered as spam, rejected by internal rules,")
        print("or otherwise not delivered to the final recipient's mailbox.")

except smtplib.SMTPAuthenticationError as e:
    print(f"\nSMTP Authentication Error: {e}")
    print("Please check your SMTP_USERNAME and SMTP_PASSWORD.")
    print("For Gmail, you might need to use an 'App Password' if 2FA is enabled.")
except smtplib.SMTPConnectError as e:
    print(f"\nSMTP Connection Error: {e}")
    print(f"Could not connect to {SMTP_SERVER}:{SMTP_PORT}. Check server address, port, and network.")
except smtplib.SMTPException as e:
    print(f"\nAn SMTP error occurred: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
