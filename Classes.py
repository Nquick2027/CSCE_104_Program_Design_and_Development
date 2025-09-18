class Chair:
    def __init__(self, cs, ty, pr, nl, hc, ha, br):
        self.colors = cs                # List of strings
        self.type = ty                  # String (armchair, swivel, camping, etc...)
        self.price = pr                 # Decimal number (float)
        self.num_legs = nl              # Whole number (int)
        self.has_casters = hc           # Boolean
        self.height_adjustable = ha     # Boolean
        self.brand = br                 # String
    
my_chair =Chair(['black', 'blue'], 'rolling', 200.00, 5, True, True, 'Acme')
armchair = Chair(['garnet'], 'armchair', 400.00, 0, False, False,'La-Z-Boy')

if armchair.price > my_chair.price:
    print('Armchair is nicer!')
else:
    print('Classroom chair is nicer!')

armchair.colors = ['garnet', 'black']
armchair.brand = armchair.brand + ' by Sealy'




class Laptop:
    # Constructor
    def __init__(self, sw, rm, pr, br, ml, st,cr):
        # properties
        self.screen_width = sw
        self.ram = rm
        self.price = pr
        self.brand = br
        self.model = ml
        self.storage = st
        self.color = cr
    
teacher_laptop = Laptop(17.0, '16GB', 700.50, 'Dell', 'Inspiron', '1TB', 'silver')
my_laptop = Laptop(15.0, '16GB', 500.00, 'Lenovo', 'Yoga7', '12GB', 'Silver')

laptop_stock = []
laptop_stock.append(teacher_laptop)
laptop_stock.append(my_laptop)
print(len(laptop_stock))