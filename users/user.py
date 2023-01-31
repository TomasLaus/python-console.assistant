import datetime
import hashlib
import users.conection as conection

connect = conection.connect()
database = connect[0]
cursor = connect[1]

class User: 

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def reg(self):
        date = datetime.datetime.now()

        # Hash password

        hashpass = hashlib.sha256()
        hashpass.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.lastname, self.email, hashpass.hexdigest(), date)

        try:

            cursor.execute(sql, user)
            database.commit()
            result =  [cursor.rowcount, self]
        except:
            result = [0, self]

        return result




    def identify(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # Hash password
        hashpass = hashlib.sha256()
        hashpass.update(self.password.encode('utf8'))

        user = (self.email, hashpass.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result