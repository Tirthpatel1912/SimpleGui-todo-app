password = input("Enter password :")
dict_password = {}

# Length checking of password
dict_password["length"] = False
if len(password) >= 8:
    dict_password["length"] = True

# Check any number present in password
dict_password["digitcheck"] = False
for i in password:
    if i.isdigit():
        dict_password["digitcheck"] = True

# Check capital character in password or not
dict_password["capitalcharcheck"] = False
for i in password:
    if i.isupper():
        dict_password["capitalcharcheck"] = True

# Final Result for password
if all(dict_password.values()):
    print("Strong password")
else:
    print("Weak password")




