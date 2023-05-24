import psycopg2 as ps

def connect_sql():
    HOSTNAME = 'db.fzlwltihnzomlghwgbnl.supabase.co'
    USERNAME = 'postgres'
    PASSWORD = 'HqeQhH+7%.wX_4e'
    DATABASE = 'postgres'
    connection = ps.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    return (cursor, connection)

(cursor, connection) = connect_sql()


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES ('{self.name}', {self.price})"
        return manage_connection(query)

    def delete(self):
        query = f"DELETE FROM menu_items WHERE item_name = '{self.name}'"
        manage_connection(query)

    def update(self, new_name, new_price):
        query = f"""UPDATE menu_items
        SET item_name = '{new_name}', item_price = {new_price}
        WHERE item_name = '{self.name}'"""
        manage_connection(query)


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}' LIMIT 1"
        res = manage_connection(query)
        if res:
            return res[0]
        else:
            return None

    @classmethod
    def all_items(cls):
        query = f"SELECT * FROM menu_items"
        res = manage_connection(query)
        return res


def add_item_to_menu(name, price):
    item = MenuItem(name, price)
    item.save()
    return item


def remove_item_from_menu(name, price):
    item = MenuItem(name, price)
    item.delete()
    return item


def update_item_from_menu():
    old_name = input("Name of the old item to update? ")
    old_price = input("Price of the old item to update? ")
    new_name = input("New name: ")
    new_price = input("New price: ")
    item = MenuItem(new_name, new_price)
    item.update(new_name, new_price)
    return item


def show_restaurant_menu():
    items = MenuManager.all_items()
    for i in items:
        print(f"{i[1]}: {i[2]}")
