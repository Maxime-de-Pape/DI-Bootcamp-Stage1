import psycopg2 as ps


def connect_sql():
    HOSTNAME = 'db.fzlwltihnzomlghwgbnl.supabase.co'
    USERNAME = 'postgres'
    PASSWORD = 'HqeQhH+7%.wX_4e'
    DATABASE = 'postgres'
    connection = ps.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    return (cursor, connection)


def add_item_to_menu(name, price):
    query = f"INSERT INTO menu_items (item_name, item_price) VALUES ('{name}', {price})"
    cursor.execute(query)
    connection.commit()


def remove_item_from_menu(name, price):
    cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{name}' AND item_price = {price};")
    if len(cursor.fetchall()) == 0:
        print("No items found")
    else:
        query = f"DELETE FROM menu_items WHERE item_name = '{name}' AND item_price = {price};"
        cursor.execute(query)
        connection.commit()
        print("Item removed successfully")


def update_item_from_menu():
    old_name = input("Name of the old item to update? ")
    old_price = input("Price of the old item to update? ")
    new_name = input("New name: ")
    new_price = input("New price: ")
    cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{old_name}' AND item_price = {old_price};")
    if len(cursor.fetchall()) == 0:
        print("No items found")
    else:
        query = f"UPDATE menu_items " \
                f"SET item_name = '{new_name}', item_price = {new_price} " \
                f"WHERE item_name = '{old_name}' and item_price = {old_price}"
        cursor.execute(query)
        connection.commit()
        print("Item updated successfully")


def show_restaurant_menu():
    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()
    for item in items:
        print(f"{item[1]}: {item[2]}")


(cursor, connection) = connect_sql()


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES('{self.name}', '{self.price}');"
        cursor.execute(query)
        connection.commit()

    def delete(self):
        cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price};")
        if len(cursor.fetchall()) == 0:
            print("No items found")
        else:
            query = f"DELETE FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price};"
            cursor.execute(query)
            connection.commit()
            print("Item removed successfully")

    def update(self, new_name, new_price, old_name, old_price):
        cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{old_name}' AND item_price = {old_price};")
        if len(cursor.fetchall()) == 0:
            print("No items found")
        else:
            query = f"UPDATE menu_items " \
                    f"SET item_name = '{new_name}', item_price = {new_price} " \
                    f"WHERE item_name = '{old_name}' and item_price = {old_price}"
            self.name = new_name
            self.price = new_price
            cursor.execute(query)
            connection.commit()
            print("Item updated successfully")


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}' LIMIT 1"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return results[0]
        else:
            return None

    @classmethod
    def all_items(cls):
        cursor.execute("SELECT * FROM menu_items")
        return cursor.fetchall()


def show_user_menu():
    while True:
        ans = input('''--------------
View an Item (V)
Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S)
Exit (E)
--------------\n''')
        if ans.lower() in ['a', 'v', 'd', 'u', 's', 'e']:
            return ans.lower()
        else:
            print('Wrong input\n')


def view_item():
    item = input('Input name: ')
    res = MenuManager.get_by_name(item)
    print(res[1], res[2])


def add_item_to_menu():
    item = MenuItem(input('Input name: '), int(input('Input price: ')))
    item.save()
    print('Item was added successfully')


def remove_item_from_menu():
    name = input('Input name: ')
    if MenuManager.get_by_name(name):
        item = MenuItem(name)
        item.delete()
        print('Item was deleted successfully')
    else:
        print('No such item')


def update_item_from_menu():
    name = input('Input name: ')
    new_name, new_price = input('Input new name: '), int(input('Input new price: '))
    if MenuManager.get_by_name(name):
        item = MenuItem(name)
        item.update(new_name, new_price, name, item.price)
        print('Item was updated successfully')
    else:
        print('No such item')


def show_restaurant_menu():
    res = MenuManager.all_items()
    for i in res:
        print(i[1], i[2])


def main():
    choice = {
        'v': view_item,
        'a': add_item_to_menu,
        'd': remove_item_from_menu,
        'u': update_item_from_menu,
        's': show_restaurant_menu
    }
    while True:
        res = show_user_menu()
        if res == 'e':
            show_restaurant_menu()
            break
        else:
            choice[res]()


main()
