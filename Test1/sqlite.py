import sqlite3

class SQLite:
    def __init__(self, database_file):
        #ИНИЦИАЛИЗАЦИЯ БД
        self.connection=sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def add_user(self, id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users`(`id`, `name`) VALUES (?,?)", (id))