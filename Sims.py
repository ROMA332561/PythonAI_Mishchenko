import random


class Human:
    def __int__(self, name = "Human", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.glaness = 50
        self.satiety = 50

    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shoping(self, manage):
        pass
    def chill(self):
        pass
    def clan_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
    class Auto:
        def __int__(self, brnd_list):
            self.brand = random.choice(list(brnd_list))
            self.fuel= brnd_list[self.brand]["fuel"]
            self.strenght = brnd_list[self.brand]["strength"]
            self.consumption = brnd_list[self.brand]["consumption"]

    brands_of_car = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
                     "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
                     "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
                     "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},}
    class House:
        def __int__(self):
            self.mess = 0
            self.food = 0
            job_list = {
                "Java developer":
                    {"salary": 50, "gladness_less": 10},
                "Python developer":
                    {"salary": 40, "gladness_less": 3},
                "C++ developer":
                    {"salary": 45, "gladness_less": 25},
                "Rust developer": {"salary": 70, "gladness_less": 1},
            }
class Job:
    def __int__(self,  job_list):
        self.job = random.choice(list(job_list))
        self.