import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_security_alert(alert_type, log_details):
    # --- Put your details here ---
    sender_email = ""  
    sender_password = "" 
    receiver_email = "" 
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"🚨 SERVER ALERT: {alert_type}"
    
    body = f"The monitoring system detected the following event:\n\n{log_details}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"[*] Alert successfully sent for: {alert_type}")
    except Exception as e:
        print(f"[!] Failed to send email. Error: {e}")
    finally:
        server.quit()

# This bottom part is just for testing!
if __name__ == "__main__":
    test_log = "Failed password for root from 192.168.1.100 port 22 ssh2"
    send_security_alert("Test Alert", test_log)