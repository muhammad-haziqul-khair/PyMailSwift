import smtplib
import pandas as pd

def main():
    def send_email(recipient_email,subj,message):
        try:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            sender_email = ""        # enter sender email
            sender_password = ""     # enter the app password of sender email. For creating app password, watch video:  https://youtu.be/T0Op3Qzz6Ms?si=CXPtpRVapH-hr7so
            s.login(sender_email, sender_password)
            msg = f"Subject: {subj}\n\n{message}"
            s.sendmail(sender_email, recipient_email, msg)
            s.quit()
            return "successfull"
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {e}")
            return "failed"
        

    def send_single_email_to_single_user():
        recipient_email = input("Enter the Reciever's Email")
        subj = input("Enter subject for Email: ")
        print("For Modifying Message of Email, Update message.txt file")
        input("Press 'ENTER', if updated")
        # reading the message file
        with open("message.txt", "r") as message_file:
            message = message_file.read()
        send_email(recipient_email,subj,message)
        print(f"Email sent to {recipient_email}")

    def send_email_to_multiple_user():
        subj = input("Enter subject for Email: ")
        print("For Updating Reciever's Email list, Update recipient.xlsx file")
        input("Press 'ENTER', if updated")
        recipient_file = "recipient.xlsx"
        recipient_df = pd.read_excel(recipient_file)
        print("For Modifying Message of Email, Update message.txt file")
        input("Press 'ENTER', if updated")
        # reading the message file
        with open("message.txt", "r") as message_file:
            message = message_file.read()

        # Iterate through the DataFrame and send emails
        for index, row in recipient_df.iterrows():
            recipient_email = row['Email']  # Assuming 'Email' is the column containing email addresses
            result = send_email(recipient_email,subj,message)
            print(f"Email sent to {recipient_email}: {result}")


    def send_bulk_email_to_single_user():
        recipient_email = input("Enter the Reciever's Email")
        a = True
        while a:
            try:
                num_of_emails = int(input("Enter number of Emails to send: "))
                a = False
            except Exception as e:
                print("Error Occured",e)
        subj = input("Enter subject for Email: ")    
        print("For Modifying Message of Email, Update message.txt file")
        input("Press 'ENTER', if updated")
        # reading the message file
        with open("message.txt", "r") as message_file:
            message = message_file.read()
        for x in range(num_of_emails):
            result = send_email(recipient_email,subj,message)
            print(f"Email sent to {recipient_email}: {result}")


    print("Welcome to Email Sender!")
    print("""For sending Single Email, Type 1
        For sending Email to Multiple Users, Type 2 
        For sending Bulk Email to Single User, Type 3""")
    choice = input("Enter your command: ")
    while not(choice == "1" or choice == "2" or choice == "3"):
        print("Invalid Input! ")
        choice = input("Enter your command again: ")
    def conditions():
        if choice == "1":
            print("Email Sender!")
            send_single_email_to_single_user()
        elif choice == "2":
            print("Bulk Email Sender!")
            send_email_to_multiple_user()
        elif choice == "3":
            print("Send Multiple Email to Single User!")
            send_bulk_email_to_single_user()

    conditions()
main()

def conclusion():
    repeat = input('Want to continue, Type "y" or "n": ').lower()
    while repeat == "y":
        main()
        repeat = input('Want to continue, Type "y" or "n": ').lower()
    print("Thank for using Email Sender")
conclusion()

        






