#importing the emails for a seperate file
with open('emails.txt') as file:
    emails = (file.read())


seperate_emails = str(emails).split(",")
#print(seperate_emails)

non_duplicate_emails = []

for email in seperate_emails:
    if email not in non_duplicate_emails:
        non_duplicate_emails.append(email)

non_duplicate_emails_string = ''
for email in non_duplicate_emails:
    non_duplicate_emails_string += email + ', '

#exporting the emails to a seperate file
with open('duplicate-free-email-list.txt', 'w') as file:
    file.write(non_duplicate_emails_string)
