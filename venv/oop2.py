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

product1 = Product("Samsung phone", "5 element", 2500)
product2 = Product("HP laptop", "DNS", 4500)
product3 = Product("Lenovo tablet", "MTS", 1500)

warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

print("Product by index: ", warehouse.get_product_by_index(1))
print("Product by name: ", warehouse.get_product_by_name("Samsung phone"), "\n")

print("Sort by name:")
warehouse.sort_by_name()
for product in warehouse._Warehouse__products:
    print(product)

print("Sort by store:")
warehouse.sort_by_store()
for product in warehouse._Warehouse__products:
    print(product)

print("Sort by price:")
warehouse.sort_by_price()
for product in warehouse._Warehouse__products:
    print(product)

warehouse2 = Warehouse()

product4 = Product("Sony headphones", "Citilink", 500)
product5 = Product("Canon camera", "Photomag", 3000)

warehouse2.add_product(product4)
warehouse2.add_product(product5)

print("Total price:")
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
        self.free_seats = max_seats
        self.seats = {i: None for i in range(1, max_seats+1)}

    def add_passenger(self, *names):
        if len(names) > self.free_seats:
            print("Not enough seats")
            return
        for name in names:
            for seat, occupant in self.seats.items():
                if occupant is None:
                    self.seats[seat] = name
                    self.free_seats -= 1
                    self.passengers.append(name)
                    break

    def remove_passenger(self, *names):
        for name in names:
            for i, occupant in enumerate(self.seats):
                if occupant == name:
                    self.seats[i] = None
                    self.free_seats += 1
                    self.passengers.remove(name)
                    break

    def increase_speed(self, value):
        if self.speed + value > self.max_speed:
            print("Can't exceed maximum speed")
            return
        self.speed += value

    def decrease_speed(self, value):
        if self.speed - value < 0:
            print("Can't go below 0 speed")
            return
        self.speed -= value

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.add_passenger(name)
        return self

    def __isub__(self, name):
        self.remove_passenger(name)
        return self


bus = Bus(50, 30, 80)
print(bus.speed)  # 50
bus.increase_speed(20)
print(bus.speed)  # 70
bus.increase_speed(15)  # Can't exceed maximum speed
print(bus.speed)  # 70
bus.decrease_speed(30)
print(bus.speed)  # 40

print(bus.free_seats)  # 30
bus.add_passenger("John", "Jane", "Jack")
print(bus.free_seats)  # 27
print(bus.passengers)  # ['John', 'Jane', 'Jack']
print(bus.seats)  # {1: 'John', 2: 'Jane', 3: 'Jack', ...}
bus.add_passenger("Mary", "Mark", "Mike")  # Not enough seats
bus.remove_passenger("Jane", "Mike")
print(bus.free_seats)  # 29
print(bus.passengers)  # ['John', 'Jack', 'Mary', 'Mark']
print(bus.seats)  # {1: 'John', 2: None, 3: 'Jack', ...}

print("John" in bus)  # True
print("Jane" in bus)  # False

bus += "Peter"
print(bus.passengers)  # ['John', 'Jack', 'Mary', 'Mark', 'Peter']
bus -= "Mark"
print(bus.passengers)  # ['John', 'Jack', 'Mary', 'Peter']
