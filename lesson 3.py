class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

# Создание 5 объектов класса Human
humans = [
    Human("Nick"),
    Human("Kate"),
    Human("Alex"),
    Human("John"),
    Human("Emma")
]

# Создание объекта класса Auto
car = Auto("Mercedes")

# Посадка всех людей в машину
for human in humans:
    car.add_passenger(human)

# Вывод имен пассажиров
car.print_passengers_names()




