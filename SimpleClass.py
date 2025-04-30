class Classey:
    varia = 2

    def method(self):
        print(self.varia)

object_one = Classey()
object_Two = Classey()

object_one.varia= 3
object_Two.varia = 5

print(object_Two.varia)
print(object_one.varia)

class Transport:
    def __init__(self, air, water):
        self.air = air
        self.air = water


obj_Transport = Transport("beluga",  "tugBoat")
object2 = Transport("jet", "boat")

print(obj_Transport.air, obj_Transport.water)
print(object2.air, object2.water)

class ShoppingCart:
    def __init__(self):
        self.item = [];
        pass.item = []
    
     def add_item(self, item_name, qty):

        
        