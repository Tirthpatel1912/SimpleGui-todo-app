file = open("../file_exc2/members.txt", 'a+')
new_mem = input("Add a new member: ")
file.write(new_mem+"\n")
file.seek(0, 0)
print("Our members of company: ")
str1 = file.read()
print(str1)