# PyMailSwift
# Overview
This is a simple Python script for sending emails to single or multiple recipients. It provides options to send a single email, email to multiple users, or bulk emails to a single user.

# Features
__Single Email__: Send a single email to a specified recipient with a customizable subject and message.
__Multiple Users__: Send emails to multiple recipients by reading email addresses from an Excel file.
__Bulk Email__: Send a specified number of identical emails to a single recipient.
# Usage
* Run the script by executing the main() function.
* Choose the type of email you want to send:
  * Type 1 for a single email.
  * Type 2 for emails to multiple users.
  * Type 3 for bulk emails to a single user.
* Follow the prompts to enter the required information, such as recipient email addresses, subject, and message.
* For bulk emails, specify the number of emails to send.
The script will use the Gmail SMTP server to send the emails.
# Files
__message.txt:__ Modify this file to customize the message content of the emails.
__recipient.xlsx:__ For sending emails to multiple users, update this Excel file with recipient email addresses.
# Dependencies
__smtplib:__ Python standard library for sending emails using the Simple Mail Transfer Protocol (SMTP).
__pandas:__ Python library for data manipulation and analysis (used for reading Excel files).
# Notes
* Ensure that the __message.txt__ and __recipient.xlsx__ files are appropriately updated before sending emails.
# Conclusion
The script provides a basic and straightforward way to send emails using Python. Feel free to use and modify it according to your needs.

# Author
Muhammad Haziqul Khair
