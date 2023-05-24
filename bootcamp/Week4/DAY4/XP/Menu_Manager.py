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


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}'"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            item = MenuItem(results[0][1], results[0][2])
            return item
        else:
            return None

    @classmethod
    def all_items(cls):
        query = "SELECT * FROM menu_items"
        cursor.execute(query)
        all_items = cursor.fetchall()
        return all_items


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES ('{self.name}', {self.price})"
        cursor.execute(query)
        connection.commit()

    def delete(self):
        query = f"DELETE FROM menu_items WHERE item_name = '{self.name}'"
        cursor.execute(query)
        connection.commit()

    def update(self, new_name, new_price):
        query = f"UPDATE menu_items SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}'"
        cursor.execute(query)
        connection.commit()
