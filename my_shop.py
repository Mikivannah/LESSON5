class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Not done"

    def mark_as_done(self):
        self.status = "Done"

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

# метод добавление ассортимента товара
    def add_item(self, item_name, price):
        self.items[item_name] = price

# метод удаления ассортимента товара
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

# метод изменения цены
    def get_price(self, item_name):
        return self.items.get(item_name)

# метод  обновления цены
    def update_price(self, item_name, new_price):
        self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Супермаркет", "Московская, 123")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Народный", "Плеханова 456")
store2.add_item("chips", 1.99)
store2.add_item("soda", 1.25)

store3 = Store("Светлячек", "Мира 23")
store3.add_item("hammer", 10.99)
store3.add_item("screws", 0.2)

# Тестирование методов
print(f"До добавления  - цена на яблоки в магазине1:", store1.get_price("apples"))
store1.update_price("apples", 0.6)
print("После обновления - цена на яблоки в магазине1:", store1.get_price("apples"))

print("Перед удалением - асартимент товара в  магазине2:", store2.items)
store2.remove_item("chips")
print("После обновления  - ассортимент товара в магазине2:", store2.items)