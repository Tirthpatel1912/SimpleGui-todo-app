import json
import time

with open("datafile.json", "r") as file:
    data = file.read()
data1 = json.loads(data)

today = time.strftime("%b %d,%H:%M")
print("Welcome to today's quiz")
print(f"Date {today}")

score = 0
for question in data1:
    print(question["question"])
    for index,option in enumerate(question["options"]):
        print(f"{index+1}-{option}")
    user_input = int(input("Enter your choice: "))
    if user_input == question["answer"]:
        print("woo! right answer")
        score += 1
    else:
        print("Oops! Wrong answer but you will do it")
    question["userchoics"] = user_input


# Result
lengthoflist = len(data1)
print("Your score:",f"{score}"+"/"+f"{lengthoflist}")

