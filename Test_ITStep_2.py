import pickle
import json
class Car:
    def __init__(self, model, graduation_year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.graduation_year = graduation_year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def info(self):
        print("Info for car:")
        print(f"\tModel: {self.model}")
        print(f"\tGraduation year: {self.graduation_year}")
        print(f"\tManufacturer: {self.manufacturer}")
        print(f"\tEngine capacity: {self.engine_capacity}")
        print(f"\tColor: {self.color}")
        print(f"\tPrice: {self.price}")

    def update_price(self, new_price):
        while True:
            if new_price <= 0:
                print("Pleas check your enter price!")
                new_price = float(input("Enter new price for car: "))
            else:
                self.price = new_price
                print(f"New price car: {new_price}")
                break
    def __str__(self):
        return f"{self.model} {self.graduation_year} {self.manufacturer} {self.engine_capacity} {self.color} {self.price}"
    def dump_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def load_pickle(self, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def to_dict(self):
        return {"model": self.model,
        "graduation_year": self.graduation_year,
        "manufacturer": self.manufacturer,
        "engine_capacity": self.engine_capacity,
        "color": self.color,
        "price": self.price}

    def dump_json(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def from_dict(cls, data):
        return cls(data["model"], data["graduation_year"], data["manufacturer"], data["engine_capacity"], data["color"], data["price"])

    def load_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return self.from_dict(data)



car = Car("Toyota", 2022, "Toyota", 2060, "red", 1450000)

car.dump_pickle("Cars.pkl")
car_load_pickle = car.load_pickle("Cars.pkl")
print(f"Data from PICKLE: {car_load_pickle}")

car.dump_json("Cars.json")
car_load_json = car.load_json("Cars.json")
print(f"Data from JSON: {car_load_json}")




