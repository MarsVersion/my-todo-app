FILEPATH = "todos.txt"

def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of to-do items."""
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist


def write_todos(todos_arg, filepath = FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
