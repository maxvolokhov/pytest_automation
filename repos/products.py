from repos.base_repository import BaseRepository


class Products(BaseRepository):

    def __init__(self):
        super().__init__()
        self.table_name = 'products'

    def create_table_products(self):
        self.cursor.execute(f"CREATE TABLE {self.table_name} (id SERIAL PRIMARY KEY, name varchar(30), price int);")

    def insert_all(self, name1: str, price1: int, name2: str, price2: int, name3: str, price3: int, name4: str,
                   price4: int, name5: str, price5: int):
        self.cursor.execute(f"insert into {self.table_name} (name, price) values ('{name1}', '{price1}'), ('{name2}',"
                            f" '{price2}'),  ('{name3}', '{price3}'), ('{name4}', '{price4}'), ('{name5}', '{price5}');"
                            f"")
