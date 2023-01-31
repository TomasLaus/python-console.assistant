import users.user as UserModel
import notes.actions

class Actions: 

    def register(self):
        print("\nOk. Let's register your account into the system")

        name = input("Enter your name: ")
        lastname = input("Enter your last name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = UserModel.User(name, lastname, email, password)
        regUser = user.reg()

        if regUser[0] >= 1:
            print(f" Perfect! {regUser[1].name} you have registered with this email:  {regUser[1].email}  ")
        else :
            print(f"An error occurred with your registration")

    def login(self):
        print("\nOk. Enter your credentials")


        try:
            email = input("\nEnter your email: ")
            password = input("\nEnter your password: ")

            user = UserModel.User('', '', email, password)

            login = user.identify()

            if email == login[3]:
                print(f"\nWelcome {login[1]}, you have been authenticated")
                self.nextActions(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print('Incorrect Login')

    def nextActions(self, user):
        print("""
        
            Available options:
                - Create note (create)
                - Show your notes (show)
                - Delete a note (delete)
                - Exit (exit)

        """)

        action =  input("What do you want to do?  \n")
        doThis = notes.actions.Actions()


        if action == 'create':
            doThis.create(user)
            self.nextActions(user)

        elif action == 'show':
            doThis.show(user)
            self.nextActions(user)
        
        elif action == 'delete':
            doThis.delete(user)
            self.nextActions(user)
        
        elif action == 'exit':
            print(f"Ok {user[1]}, see you later!")
            exit()

