# smtp-250-ok-not-inbox-guarantee
This example demonstrates sending an email using Python's smtplib. It highlights that a successful SMTP transaction, where the recipient server accepts the email (visible as '250 OK' responses in debug output), does not guarantee delivery to the recipient's inbox. Emails can still be filtered or rejected by the recipient's system after initial acce
