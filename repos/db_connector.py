from repos.orders import Orders
from repos.products import Products

products_instance = Products()
orders_instance = Orders()

create_table_products = products_instance.create_table_products()
insert_to_table_products = products_instance.insert_all('iPhone', 1200, 'iPad', 850, 'Watch', 450, 'AirPods', 300,
                                                        'Case', 75)
create_table_orders = orders_instance.create_table_orders()
insert_to_table_orders = orders_instance.insert_all(1, 2, 2, 3, 3, 1, 4, 4, 5, 10)

order_details = orders_instance.get_order_details()

for row in order_details:
    print(row)
