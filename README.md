# SMTP 250 OK Not Inbox Guarantee

This example demonstrates sending an email using Python's smtplib. It highlights that a successful SMTP transaction, where the recipient server accepts the email (visible as '250 OK' responses in debug output), does not guarantee delivery to the recipient's inbox. Emails can still be filtered or rejected by the recipient's system after initial acceptance.

## Language

`python`

## How to Run

1. Set environment variables for your SMTP server details and recipient:
   `export SMTP_SERVER='smtp.gmail.com'`
   `export SMTP_PORT='587'`
   `export SMTP_USERNAME='your_email@example.com'`
   `export SMTP_PASSWORD='your_app_password'`
   `export TO_EMAIL='recipient@example.com'`
2. Run the script: `python main.py`
3. Observe the SMTP debug output for '250 OK' responses, indicating server acceptance.

## Original Article

This example accompanies the Turkish article: [SMTP 250 OK Yanıtına Rağmen E-postalar Neden Geri Dönüyor? Detaylı Bir İnceleme](https://fatihsoysal.com/blog/smtp-250-ok-yanitina-ragmen-e-postalar-neden-geri-donuyor-detayli-bir-inceleme/).

## License

MIT — see [LICENSE](LICENSE).
