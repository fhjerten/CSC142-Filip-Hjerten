class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, mpg):
        self._name = name  # private name of vehicle
        self._fuel_capacity = fuel_capacity  # how much fuel it holds
        self._cost_per_gallon = cost_per_gallon  # price of fuel
        self._mpg = mpg  # miles per gallon

    @property
    def name(self):
        return self._name  # return vehicle name

    @property
    def range(self):
        return self._fuel_capacity * self._mpg  # distance on full tank

    @property
    def cost_per_mile(self):
        return self._cost_per_gallon / self._mpg  # cost per mile


# create different vehicles
car = Vehicle("Car", 12, 3.5, 25)  # small tank, good mpg
bus = Vehicle("Bus", 50, 4.0, 6)  # big tank, low mpg
train = Vehicle("Train", 200, 5.0, 15)  # medium efficiency
plane = Vehicle("Plane", 5000, 6.0, 0.2)  # very large fuel, very low mpg


# put all vehicles in a list
vehicles = [car, bus, train, plane]

# sort by cost per mile (lowest first)
vehicles.sort(key=lambda v: v.cost_per_mile)
#for each vehicle (v), using it as cost_per_mile


# print table header
print("Name\tRange\tCost per Mile")  # \t made for spacing between each column


# loop through vehicles and print info
for v in vehicles:
    print(f"{v.name}\t{v.range}\t{v.cost_per_mile:.2f}")  # formatted output. 2f rounds to 2 decimaks. 




