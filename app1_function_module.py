FILEPATH = 'app1_todos.txt'
def func_get_todos(file_path_name=FILEPATH):
    """
    This Function is for Reading a Text File: app1_todos.txt
    :return:
    """
    # with open("files/app1_todos.txt", "r") as file_todo:
    with open(file_path_name, "r") as file_todo:
        list_todo_local = file_todo.readlines()
    return list_todo_local


def func_wrt_todos(list_todo_arg, file_path_name_local = FILEPATH):
    """
    This Function is to Write to Text File: app1_todos.txt
    :param list_todo_arg:
    :return:
    """
    # with open('files/app1_todos.txt', 'w') as file_todo:
    with open(file_path_name_local, 'w') as file_todo:
        file_todo.writelines(list_todo_arg)
    return "True"  #list_todo


if __name__ == "__main__":
    print("Good Hello")
    print(func_get_todos())

# end of code ---