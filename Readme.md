# Email Login Checker

This Python script checks if email accounts in a provided list can be successfully logged in. 
It also filters successful logins for specific keywords and saves them to separate files.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/email-login-checker.git
   cd email-login-checker

2. install dependencies.
pip install smtplib

3. Configure Script:
Open the script (email_login_checker.py) and modify the following:

SMTP server details in the check_email_login function based on your email provider 
(e.g., mail.btinternet.com for BT Internet).
Input file name (logins.txt) and output folder name (output).

4. Usage
Run the script with the following command:
python email_login_checker.py

Results will be saved in the 'output' folder.

Input File Format
The input file (logins.txt) should contain email and password pairs separated by commas, 
one pair per line.

Example:
user1@example.com,password123
user2@example.com,securepass

Output
Successful logins are saved in output/all_logins.txt.
Separate files are created for specific keywords (clearpay, amazon, etc.) in the 'output' folder.
Disclaimer
This script should only be used with proper authorization. Unauthorized access to email accounts is against ethical guidelines.

Feel free to contribute or report issues!
