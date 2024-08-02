"""
Created By : Manu Tyagi
Date Created : 2024-07-28

Day 19 of 20 Apps in 60 Days

*NEW* ----
    Web App Using streamlit
    Lines should be not more than 79-Characters

To Execute Run in Terminal:
    >> streamlit run Day_19_Web_todo.py

Location

https://mtpyweb.streamlit.app
"""
# import streamlit
import streamlit as lit
import app1_function_module as mod1


# Read To-Do List In ---
read_todos = list_todos = mod1.func_get_todos()


def func_add_todo():
    input_todo = lit.session_state['new_todo_key'] + "\n"
    # print(todo)
    read_todos.append(input_todo)
    mod1.func_wrt_todos(read_todos)


lit.title("My ToDo App: MT")
lit.subheader("This is my todo web app")
lit.write("This app is to increase your productivity")

# lit.checkbox("Buy Grocery")
# lit.checkbox("Take out trash")

for item_index, item_todo in enumerate(list_todos):
    item_check = lit.checkbox(item_todo, key=item_todo)
    if item_check:
        list_todos.pop(item_index)
        mod1.func_wrt_todos(list_todos)
        del lit.session_state[item_todo]
        # lit.experimental_rerun() # Not Supported in 1.37
        lit.rerun()


lit.text_input(label="Enter a ToDo Item:",
               placeholder="<<Add New todo here>>",
               on_change=func_add_todo,
               key='new_todo_key')

print("Hello")

# lit.session_state

# end of code ---