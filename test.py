import unittest
from unittest.mock import patch
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk
from main import generate_username, generate_password, send_email, generate_and_send_email

class TestEmailSending(unittest.TestCase):
    def test_generate_username(self):
        username = generate_username()
        self.assertEqual(len(username), 8)

    def test_generate_password(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    @patch('your_script_name.smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        root = Tk()
        receiver_email = 'test@example.com'
        username = 'test_username'
        password = 'test_password'

        send_email(root, receiver_email, username, password)

        mock_smtp.return_value.starttls.assert_called()
        mock_smtp.return_value.login.assert_called_with('220384@softwarica.edu.np', 'Sarkar1011')
        mock_smtp.return_value.sendmail.assert_called_with('220384@softwarica.edu.np', 'test@example.com', 
                                                            MIMEMultipart().as_string())
        mock_smtp.return_value.quit.assert_called()

    @patch('your_script_name.messagebox')
    def test_send_email_failure(self, mock_messagebox):
        root = Tk()
        receiver_email = 'sarushahi547@gmail.com'
        username = 'test_username'
        password = 'test_password'

        # Mocking exception to simulate failure in sending email
        with patch('your_script_name.smtplib.SMTP') as mock_smtp:
            mock_smtp.return_value.login.side_effect = Exception('Failed to login')

            send_email(root, receiver_email, username, password)

        mock_messagebox.showerror.assert_called_with('Error', 'Failed to send email.', parent=root)

if __name__ == '__main__':
    unittest.main()
