from repos.base_repository import BaseRepository


class Orders(BaseRepository):

    def __init__(self):
        super().__init__()
        self.table_name = 'orders'

    def create_table_orders(self):
        self.cursor.execute(f"CREATE TABLE {self.table_name} (id SERIAL PRIMARY KEY, product_id int, quantity int);")

    def insert_all(self, product_id1: int, quantity1: int, product_id2: int, quantity2: int, product_id3: int,
                   quantity3: int, product_id4: int, quantity4: int, product_id5: int, quantity5: int):
        self.cursor.execute(
            f"insert into {self.table_name} (product_id, quantity) values ('{product_id1}', '{quantity1}'), "
            f"('{product_id2}', '{quantity2}'),  ('{product_id3}', '{quantity3}'), ('{product_id4}', '{quantity4}'), "
            f"('{product_id5}', '{quantity5}');")

    def get_order_details(self):
        self.cursor.execute("""
        SELECT
            p.name,
            p.price,
            o.quantity,
            (p.price * o.quantity) AS total_price
        FROM
            products AS p
        JOIN
            orders AS o
        ON
            p.id = o.product_id;
        """)
        return self.cursor.fetchall()
