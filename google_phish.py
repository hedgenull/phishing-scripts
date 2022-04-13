name = input("Enter target's first name: ")
email = input("Enter target's email address: ")
invite_name = input("Enter fake name for email invite: ")
invite_email = input("Enter fake email for email invite: ")
chat_name = input("Enter fake chat name: ")
fake_link = input(
    "Enter malicious URL to go to (format: http(s)://example.com/): ")

with open("google_invite.html", "r") as template:
    content = template.read()
    content = content.replace("${name}", name).replace(
        "${email}", email).replace("${invite_name}", invite_name).replace(
            "${invite_email}",
            invite_email).replace("${chat_name}",
                                  chat_name).replace("${fake_link}", fake_link)

with open(f"{name.lower().replace(' ', '_')}_google_invite.html", "w") as f:
    f.write(content)
    print("Template saved to file: {}. Have fun phishing!".format(f.name))
