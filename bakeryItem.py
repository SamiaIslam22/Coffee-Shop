class BakeryItem:
  def __init__(self, food, price, plainbagels, strawberrycake, sesbagel, honeybun, cinnamonroll, croissant):
    #attributes
    self.food=food
    self.price= price 
    self.ingredients={ #use dictionary function to set every ingredient name to a variable
      "Plain Bagel":plainbagels,
      "Strawberry Cake": strawberrycake,
      "Sesameseed Bagel": sesbagel,
      "Honey Bun": honeybun,
      "Cinnamon Roll": cinnamonroll,
      "Croissant": croissant
    }
    
class BakeryMenu: 
    def __init__(self):
      #create a list consisting of the price per unit, set every other variable to 0 to prevent it from getting subtracted from storage
      self.menu = [
        BakeryItem(food="Plain Bagel", price = 3.00, plainbagels=1, strawberrycake=0, sesbagel=0, honeybun=0, cinnamonroll=0, croissant=0),
        BakeryItem(food="Strawberry Cake", price = 4.00, plainbagels=0, strawberrycake=1, sesbagel=0, honeybun=0, cinnamonroll=0, croissant=0), 
        BakeryItem(food="Sesameseed Bagel", price = 3.50, plainbagels=0, strawberrycake=0, sesbagel=1, honeybun=0, cinnamonroll=0, croissant=0),
        BakeryItem(food="Honey Bun", price = 4.00, plainbagels=0, strawberrycake=0, sesbagel=0, honeybun=1, cinnamonroll=0, croissant=0),
        BakeryItem(food="Cinnamon Roll", price = 3.70, plainbagels=0, strawberrycake=0, sesbagel=0, honeybun=0, cinnamonroll=2, croissant=0),
        BakeryItem(food="Croissant", price = 3.00, plainbagels=0, strawberrycake=0, sesbagel=0, honeybun=0, cinnamonroll=0, croissant=1),
      ]

    #Create a function to check if the user choice exists in the BakeryItem, if yes, return item, if not return None 
    def find_food(self, orderName):
        for item in self.menu:
            if item.food.lower() == orderName.lower():
                return item
        return None
