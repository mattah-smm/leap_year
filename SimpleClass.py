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
        self.water = water


obj_transport = Transport("beluga",  "tugBoat")
object2_transport= Transport("jet", "boat")

print(obj_transport.air, obj_transport.water)
print(object2_transport.air, object2_transport.water)


class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.item.append(item)
    def remove_item(self, item_name):
        for item in self.items:
            if item(0) == item_name:
                self.item.remove(item)
                break

    def calculate_total(self):
        total =0
        for item in self.item:
            total +=item[1]
        return total
cart = ShoppingCart()


#adding items to the list
cart.add_item("kiwi", 100)
cart.add_item("pens", 10)
cart.add_item("apples", 20)

print ("Current Items in Cart")
for item in cart.item:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity: ", total_qty)