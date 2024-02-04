def get_todos(filepath="todo.txt"):
    """ Take a filename as input and return
    list of file contents.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(todos_arg, filepath="todo.txt"):
    """ Take file name and list of content as arguments
    which were written in file that are passed by argument.
    """
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_arg)
