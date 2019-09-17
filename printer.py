class Printer:
    def __init__(self, name, print_speed, price):
        self.name = name
        self.print_speed = print_speed
        self.price = price

    # def __del__(self):
    #     print("Object " + self.name + " was deleted")

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
