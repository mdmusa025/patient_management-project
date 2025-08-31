import re
username=input("enter the username:")
pwd=input("enter the password:")
pwd_len=len(pwd)
is_valid=False

while True:
    if pwd_len < 7 or pwd_len >20:
        break
    elif not re.search('[A-Z]',pwd):
        break
    elif not re.search('[a-z]',pwd):
        break
    elif not re.search('[0-9]',pwd):
        break
    elif not re.search('[$#@!]',pwd):
        break
    elif  re.search('\s',pwd):
        break
    else:
        is_valid =True
        break
if is_valid:
    print(f" Username: {username}")
    print(f"password:{pwd}")
    print("password is valid")
else:
    print(f" Username: {username}")
    print(f"password:{pwd}")

    print("password is invalid")
   