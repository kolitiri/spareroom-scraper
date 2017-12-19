# Standard library imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Local imports
from config_loader import ConfigLoader


class Emailer:
    """ A class that sends an email notification """

    def __init__(self, config_file):
        # Create a new instance of the ConfigLoader class
        self.config_loader = ConfigLoader(config_file)

    def _get_item(self, config_item):
        """ Get the value of an item from the config file.
            Calls get_item of ConfigLoader class.

            Args:
                config_item: Name of the item to look up.

            Returns:
                A list of one or more values for the requested item.
        """

        config_item = self.config_loader.get_item(config_item)

        return config_item

    def send_gmail(self, content):
        """ Send an email notification through gmail.

            Reads the configuration from emailer_config.ini

            Raises:
                SMTPException, if one occured.
        """

        gmail_server = self._get_item('gmail_server')
        gmail_port = self._get_item('gmail_port')
        gmail_user = self._get_item('gmail_user')
        gmail_password = self._get_item('gmail_password')
        gmail_receiver = self._get_item('gmail_receiver')
        gmail_subject = 'Spareroom search results'

        msg = MIMEMultipart('alternative')
        msg['From'] = gmail_user
        msg['To'] = gmail_receiver
        msg['Subject'] = gmail_subject

        html_part = MIMEText(content, 'html')
        msg.attach(html_part)

        try:
            server = smtplib.SMTP_SSL(gmail_server, gmail_port)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, gmail_receiver, msg.as_string())
            server.close()
        except:  
            raise