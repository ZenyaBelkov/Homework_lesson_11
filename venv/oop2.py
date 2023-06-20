# TASK 1
print("Task 1 \n")


class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} ({self.__store}) - {self.__price} rub."


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        return self.__products[index]

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return product
        return None

    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda x: x.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())

    def __add__(self, other):
        total_price = sum([product.get_price() for product in self.__products]) + sum([product.get_price() for product in other.__products])
        return total_price


warehouse = Warehouse()

product1 = Product("Samsung phone", "M.Video", 25000)
product2 = Product("HP laptop", "DNS", 45000)
product3 = Product("Lenovo tablet", "Eldorado", 15000)

warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

print(warehouse.get_product_by_index(1))
print(warehouse.get_product_by_name("Samsung phone"))

warehouse.sort_by_name()
for product in warehouse._Warehouse__products:
    print(product)

warehouse.sort_by_store()
for product in warehouse._Warehouse__products:
    print(product)

warehouse.sort_by_price()
for product in warehouse._Warehouse__products:
    print(product)

warehouse2 = Warehouse()

product4 = Product("Sony headphones", "Citilink", 5000)
product5 = Product("Canon camera", "Photomag", 30000)

warehouse2.add_product(product4)
warehouse2.add_product(product5)

total_price = warehouse + warehouse2
print(total_price)
print("\n")

# TASK 2
print("Task 2 \n")


class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        if self.bee_part >= self.elephant_part:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            if self.elephant_part - value >= 0 and self.bee_part + value <= 100:
                self.elephant_part -= value
                self.bee_part += value
        elif meal == "grass":
            if self.bee_part - value >= 0 and self.elephant_part + value <= 100:
                self.bee_part -= value
                self.elephant_part += value


bee_elephant = BeeElephant(40, 60)

print(bee_elephant.fly())
print(bee_elephant.trumpet())

bee_elephant.eat("nectar", 20)
print(bee_elephant.bee_part)
print(bee_elephant.elephant_part)

bee_elephant.eat("grass", 10)
print(bee_elephant.bee_part)
print(bee_elephant.elephant_part)
print("\n")

# TASK 3
print("Task 3 \n")


class Bus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []

    def contains(self, name):
        return name in self.passengers

    def iadd(self, name):
        self.board_passenger(name)
        return self

    def isub(self, name):
        self.disembark_passenger(name)
        return self

    def board_passenger(self, name):
        if len(self.passengers) < self.max_seats:
            self.passengers.append(name)
        else:
            print("No seats available")

    def disembark_passenger(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
        else:
            print(f"{name} is not on the bus")

    def __str__(self):
        return f"Bus with {len(self.passengers)} passengers"

bus = Bus(60, 30, 100)

bus.board_passenger("Alice", "Bob", "Charlie")
print(bus.passengers)
print(bus.seat_map)

print("Alice" in bus)

bus.disembark_passenger("Bob")
print(bus.passengers)
print(bus.seat_map)

bus.increase_speed(20)
print(bus.speed)

bus.decrease_speed(30)
print(bus.speed)

bus += "Dave"
print(bus.passengers)
print(bus.seat_map)

bus -= "Charlie"
print(bus.passengers)
print(bus.seat_map)