name = input("Enter target name: ")
fake_name = input("Enter fake name: ")
fake_message = input("Enter fake message: ")
fake_amount = input("Enter fake amount: ")
fake_order_number = input("Enter fake order number: ")
fake_code = input("Enter fake code: ")
fake_link = input(
    "Enter malicious URL to go to (format: http(s)://example.com/): ")

with open("amazon_card.html", "r") as template:
    content = template.read()
    content = content.replace(
        "${name}", name).replace("${fake_message}", fake_message).replace(
            "${fake_amount}",
            fake_amount).replace("${fake_code}", fake_code).replace(
                "${fake_number}",
                fake_order_number).replace("${fake_link}", fake_link).replace("${fake_name}", fake_name)

with open(f"{name.lower().replace(' ', '_')}_amazon_card.html", "w") as f:
    f.write(content)
    print("Template saved to file: {}. Have fun phishing!".format(f.name))
