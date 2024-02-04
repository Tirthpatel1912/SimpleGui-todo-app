import functions
import time

while True:
    print("Present time: ",time.strftime("%b %d,%H:%M:%S"))
    user_choice = input("Type add,edit,Show,exit and complete: ")
    user_choice = user_choice.strip()

    if user_choice.startswith("add") or user_choice.startswith("new"):
        user_value = user_choice[4:]
        user_value = user_value + "\n"
        todos = functions.get_todos("todo.txt")
        todos.append(user_value)
        functions.set_todos(todos, "todo.txt")

    elif user_choice.startswith("show") or user_choice.startswith("Show"):
        todos = functions.get_todos("todo.txt")

        # todos = [item.strip("\n") for item in todos]
        for index,item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")

    elif user_choice.startswith("exit") or user_choice.startswith("Exit"):
        print("Bye!")
        break

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])
            index = number - 1
            todos = functions.get_todos("todo.txt")
            print("Your todo list: ", todos)
            complete_todo = todos[index].strip("\n")
            todos.pop(index)
            print(f"Todo {complete_todo} completed")
            functions.set_todos(todos, "todo.txt")
        except IndexError:
            print("oops!There is no such element present at this index")
            continue

    elif user_choice.startswith("edit"):
        try:
            todo_position = int(user_choice[5:])
            index = todo_position - 1
            todos = functions.get_todos("todo.txt")
            print("Your todo list: ", todos)
            todo_elem = input("Enter your new todo:")
            todos[index] = todo_elem + "\n"
            print("Your todo list: ", todos)
            functions.set_todos(todos, "todo.txt")
        except IndexError:
            print("Enter valid value.")
            continue

    else:
        print("Enter valid choice!")



