class Car:
    species = "Porsche"
    number_of_wheels = 4
    def __init__(self, brand, year, fuel_type, max_speed):
        self.brand = brand
        self.year = year
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def show (self):
        print(f"I am {self.brand} and I am from {self.year} year")

    def jedz(self):
        print(f"Jade z predkoscia: {self.max_speed} km/h")

car1 = Car("Porsche", 2001, "benzyna", 300)
print(car1.brand)
print(car1.year)
print(car1.fuel_type)
print(car1.max_speed)
car1.show()
car1.jedz()
car1.max_speed += 35
print("Zmiana predkosci max")
car1.jedz()


print("\n\nDrugi samochod")
car2 = Car("Mercedes", 2010, "diesel", 250)
print(car2.brand)
print(car2.year)
print(car2.fuel_type)
print(car2.max_speed)
car2.show()
car2.jedz()
print("Zmiana predkosci max")
car2.max_speed += 35
car2.jedz()
