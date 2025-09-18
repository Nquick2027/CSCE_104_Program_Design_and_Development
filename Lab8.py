class Car:
    def __init__(self, mk, md, yr, cl):
        self.make = mk
        self.model = md
        self.year = yr
        self.color = cl

myCar = Car('Jeep', 'Commander', '2008', 'White')
friendsCar = Car('Mustang', 'GT', 'Unknown', 'Dark Blue')

class House:
    def __init__(self, st, rm, bd, bt, yd, pr):
        self.numStories = st
        self.totalRooms = rm
        self.numBedrooms = bd
        self.numBathrooms = bt
        self.yardSqft = yd
        self.price = pr

randomHouse = House(3, 12, 5, 3, 38, 750000)
otherHouse = House(1, 11, 4, 3, 'Unknown', 'Unknown')

class Person:
    def __init__(self, gd, ag, et, ht, wt, ct):
        self.gender = gd
        self.age = ag
        self.ethnicity = et
        self.height = ht
        self.weight = wt
        self.country = ct

male = Person('Male', 37, 'Black/African American', '6\'2\"', 270, 'United States')
female = Person('Female', 19, 'Hispanic/Latino', '5\'5\"', 'Unknown', 'Chile')