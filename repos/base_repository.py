import psycopg2


class BaseRepository:
    def __init__(self):
        self.__connection = psycopg2.connect(user='postgres', password='123', host='127.0.0.1', port='5432',
                                             database='store')
        self.cursor = self.__connection.cursor()
        self.__connection.set_session(autocommit=True)
        self.table_name = ''

    def __del__(self):
        if self.__connection:
            if self.cursor:
                self.cursor.close()
            self.__connection.close()

    def get_all(self):
        self.cursor.execute(f"select * from {self.table_name}")
        return self.cursor.fetchall()
