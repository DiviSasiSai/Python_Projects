# You probably have accounts on many different websites. It’s a bad habit to
# use the same password for each of them because if any of those sites has
# a security breach, the hackers will learn the password to all of your other
# accounts. It’s best to use password manager software on your computer that
# uses one master password to unlock the password manager. Then you can
# copy any account password to the clipboard and paste it into the website’s
# Password field.
# Packages
#piperclip,sys

import pyperclip
import sys

PASSWORDS = {
    "email":"Sai@14399",
    "facebook":"SaiSai@143",
    "insta":"Sasi@14399"
}

if len(sys.argv) < 2:
    print("Usage: python passwordLocker.py <account>")
    sys.exit(1)

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password of {account} copied to clipboard")
else:
    print("Account does not exist")
    sys.exit(1)