import re
import pyperclip

# Program that checks password validation

print("\n")
print("<<<<<<<<Note for User>>>>>>>>>")
note = ('''Your password must be 8 character long and
make sure it contains:
- Uppercase character
- Lowercase character 
- atleast a digit
''')
print(note)

# User password
userpass = input("Enter your password to test its strength: ")

matchformat = {}
def check(pattern):
    """The function checks for pattern in user input and returns a bool"""
    res = re.compile(pattern).search(userpass.strip());
    if res is not None:
        return True
    else:
        return False

# Conditions that must be met for a strong password
criteria = ['\d+', '[a-z]+', '[A-Z]+']

for i in range(3):
    if i == 0:
        matchformat['digit'] = check(criteria[i])
    elif i == 1:
        matchformat['lowercase'] = check(criteria[i])
    elif i == 2:
        matchformat['uppercase'] = check(criteria[i])
        
if matchformat['digit'] + matchformat['lowercase'] + matchformat['uppercase'] < 3:
    print("\n**Password not strong**".upper())
    print("Pleae try a stronger password")
else:
    print("\n***Your password is strong and secure***")
    copy = input("Do you want to copy the password? Y or N: ")
    if copy == 'Y' or copy == 'y':
        pyperclip.copy(userpass)
        print("\nPassword copied, you can paste it where you need to\n")    
    
print("Password Details:")
for k, v in matchformat.items():
    if v == False:
        v = "No "+k+" found"
    print(f"{k} - {v}") 