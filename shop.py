class ShopInfo:
  def __init__(self):
    self.storage={#use dictionary function to set each ingredient with a maximum value
      "Water": 100000000,
      "Oat Milk": 700,
      "Regular Milk": 800,
      "Almond Milk": 700,
      "Sugar": 100,
      "Coffee Beans": 100,
      "Plain Bagel": 4,
      "Strawberry Cake": 3,
      "Sesameseed Bagel": 4,
      "Honey Bun":2,
      "Cinnamon Roll": 2,
      "Croissant": 4
  }

  def storagereport(self): #report backs the updated storage material left in the shop
    print (f"Water: {self.storage['Water']}ml")
    print (f"Oat Milk: {self.storage['Oat Milk']}ml")
    print (f"Coffee Beans: {self.storage['Coffee Beans']}g")
    print (f"Regular Milk: {self.storage['Regular Milk']}ml")
    print (f"Almond Milk: {self.storage['Almond Milk']}ml")
    print (f"Sugar: {self.storage['Sugar']}g")
    print (f"Plain Bagel: {self.storage['Plain Bagel']}")
    print (f"Strawberry Cake: {self.storage['Strawberry Cake']}")
    print (f"Sesameseed Bagel: {self.storage['Sesameseed Bagel']}")
    print (f"Honey Bun: {self.storage['Honey Bun']}")
    print (f"Cinnamon Roll: {self.storage['Cinnamon Roll']}")
    print (f"Croissant: {self.storage['Croissant']}")

  def resource_check(self, ingredients): 
        #checks if we have enough of the material in the shop. 
        #If the quantity used for user choice item is larger than storage item then, it output that we ran out of the item
        for item, quantity in ingredients.items():
            if quantity > self.storage.get(item, 0):
                print(f"Sorry, we have run out of {item}. Please choose something else.")
                return False
        return True
#if we have enough material, the amount of material that was used for this order is subtracted from self storage

  def coffee_return(self, coffee_order): 
        for item, quantity in coffee_order.ingredients.items():
            self.storage[item] -= quantity
        print(f"Here is your {coffee_order.coffeeName}. Enjoy!")

  def food_return(self, food_order):
        for item, quantity in food_order.ingredients.items():
            self.storage[item] -= quantity
        print(f"Here is your {food_order.food}. Enjoy!")
           
    
