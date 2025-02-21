class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

car1 = Car("Chevrolet", "Malibu", 2019)
car2 = Car("Nissan", "Altima", 2021)


car1.display_info()
car2.display_info()
