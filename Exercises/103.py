import re

email_text = """
Hello Team,

Please find the details below:
john.doe@example.com
- Contact: john.doe@example.com
- Support: support@company.org
- Sales: sales@business.com

Feel free to reach out for any queries.

Best regards,
Jane Doe
jane.doe@personalmail.net\..co.com.net.
"""

# Extract unique emails from the text
matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email_text)
emails = set(matches)
print(f"We have found {len(emails)} unique emails:")
print(emails)

# Save emails to file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")
print("Emails have been saved to 'emails.txt'.")

# Ask user for an additional email
new_email = input("Enter an additional email address: ").strip()
if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", new_email):
    print("Invalid email format. Email was not added.")
elif new_email in emails:
    print("This email is already in the set.")
else:
    emails.add(new_email)
    with open("emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")
    print("The new email is added and saved!")
