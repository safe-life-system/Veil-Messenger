import sqlite3

#Класс управления локальной БД
class DataBaseControl:
    def __init__(self, user_id, user_name, user_login, password, salt):
        self.user_id = user_id
        self.user_name = user_name
        self.user_login = user_login
        self.salt = salt
        self.password = password
    
    #Метод создания БД
    def create_db(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                user_id TEXT PRIMARY KEY,
                user_login BLOB,
                user_name TEXT,
                user_password BLOOB,
                salt BLOB);
            """)
    
    #Метод регистрации в БД
    def registration_db(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user(user_id, user_login, user_name, user_password, salt) VALUES(?, ?, ?, ?, ?);", (self.user_id, self.user_login, self.user_name, self.password, self.salt,))
            
            return True