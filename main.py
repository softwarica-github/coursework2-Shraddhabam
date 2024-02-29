
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import subprocess
 
# Your actual credentials and sensitive data should be stored securely
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587
SENDER_EMAIL = "sarushahi547@gmail.com"  # Your email address
SENDER_PASSWORD = "shahisaru13@!!"  # Your email password

 
# Function to generate a random username
def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
 
# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=12))
 

 
# Email sending function
# Modified Email sending function to show a popup on success
def send_email(root, receiver_email, username, password):
    try:
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = receiver_email
        message["Subject"] = "Generated Username and Password"
        body = f"Username: {username}\nPassword: {password}"
        message.attach(MIMEText(body, "plain"))
 
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
        server.quit()

        # Show popup message indicating success
        messagebox.showinfo("Success", "Email sent successfully!", parent=root)
    except Exception as e:
        # Show popup message indicating failure
        messagebox.showerror("Error", "Failed to send email.", parent=root)
        print(e)
 
 
# GUI setup
# GUI setup
def generate_and_send_email():
    receiver_email = email_entry.get()
    username = generate_username()
    password = generate_password()

   
    # Send email with the generated username and password and show success popup
    send_email(root, receiver_email, username, password)
 
 
root = tk.Tk()
root.title("Generate Username and Password")
 
email_label = tk.Label(root, text="Enter your Gmail address:")
email_label.pack()
 
email_entry = tk.Entry(root)
email_entry.pack()
 
generate_button = tk.Button(root, text="Generate and Send Email", command=generate_and_send_email)
generate_button.pack()
 
root.mainloop()