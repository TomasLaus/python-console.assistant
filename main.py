"""
    Project with Python and MySql
        - Open the assistant
        - Login or register
        - Register: will create a new user in the database
        - Login: will identify the user and we will be able to: 
            - Create a note, show our notes or delete them
"""

from users import actions

print("""
    Options available:
        - Register (register)
        - Login (login)

""")

DoThis = actions.Actions()

action = input("What do you want to do?         ")

if action == "register":
    DoThis.register()

elif action == "login":
    DoThis.login()
