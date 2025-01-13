class Menulist:
  def __init__(self, coffeeName, water ,oatmilk, almondmilk, regmilk, coffeebeans, sugar, price ):
    self.coffeeName=coffeeName
    self.ingredients={ #use dictionary function to set every ingredient name to a variable
      "Water":water,
      "Regular Milk":regmilk,
      "Oat Milk":oatmilk,
      "Almond Milk":almondmilk,
      "Coffee Beans":coffeebeans,
      "Sugar":sugar}
    self.price=price
      
  
class CoffeeMenu: 
    def __init__(self):
      self.menu=[
        #create a list consisting of the price per unit, set every other variable to 0 to prevent it from getting subtracted from storage
        Menulist(coffeeName="medium regularmilk hot latte", water=160, regmilk=110, oatmilk=0, almondmilk=0, coffeebeans=14, sugar=2, price=4.50),
        Menulist(coffeeName="medium oatmilk hot latte", water=160, oatmilk=110, regmilk=0, almondmilk=0, coffeebeans=14, sugar=2, price=4.70),
        Menulist(coffeeName="medium almondmilk hot latte",water=160, almondmilk=110, oatmilk=0, regmilk=0, coffeebeans=14, sugar=2, price=4.70),       
        Menulist(coffeeName="medium regularmilk ice latte",water=170, regmilk=80, oatmilk=0, almondmilk=0, coffeebeans=14, sugar=2, price=4.50),
        Menulist(coffeeName="medium oatmilk ice latte",water=170, oatmilk=80, regmilk=0, almondmilk=0,coffeebeans=14, sugar=2, price=4.70),
        Menulist(coffeeName="medium almondmilk ice latte",water=170, almondmilk=80, oatmilk=0, regmilk=0,coffeebeans=14, sugar=2, price=4.70),      
        Menulist(coffeeName="large regularmilk hot latte", water=200, regmilk=150,oatmilk=0, almondmilk=0, coffeebeans=24, sugar=3, price=5.50),
        Menulist(coffeeName="large oatmilk hot latte", water=200, oatmilk=150, regmilk=0, almondmilk=0,coffeebeans=24, sugar=3, price=5.70),
        Menulist(coffeeName="large almondmilk hot latte", water=200, almondmilk=150,oatmilk=0, regmilk=0, coffeebeans=24, sugar=3, price=5.70),       
        Menulist(coffeeName="large regularmilk ice latte", water=210, regmilk=110, oatmilk=0, almondmilk=0,coffeebeans=24, sugar=3, price=5.50),
        Menulist(coffeeName="large oatmilk ice latte", water=210, oatmilk=110, regmilk=0, almondmilk=0,coffeebeans=24, sugar=3, price=5.70),
        Menulist(coffeeName="large almondmilk ice latte", water=210, almondmilk=110,oatmilk=0, regmilk=0, coffeebeans=24, sugar=3, price=5.70),        
        Menulist(coffeeName="medium hot expresso", water=50, regmilk=0, oatmilk=0, almondmilk=0, sugar=2, coffeebeans=24, price=4.70),
        Menulist(coffeeName="large hot expresso", water=50, regmilk=0, oatmilk=0, almondmilk=0, sugar=3, coffeebeans=24, price=5.70),        
        Menulist(coffeeName="medium regularmilk hot cappuccino", water=200, regmilk=50,oatmilk=0, almondmilk=0, coffeebeans=18, sugar=2, price=4.70),
        Menulist(coffeeName="medium oatmilk hot cappuccino", water=200, oatmilk=50, regmilk=0, almondmilk=0,coffeebeans=18, sugar=2, price=4.90),
        Menulist(coffeeName="medium almondmilk hot cappuccino", water=200, almondmilk=50,oatmilk=0, regmilk=0, coffeebeans=18, sugar=2, price=4.90),
        Menulist(coffeeName="medium regularmilk ice cappuccino", water=210, regmilk=50,oatmilk=0, almondmilk=0, coffeebeans=18, sugar=2, price=4.70),
        Menulist(coffeeName="medium oatmilk ice cappuccino", water=210, oatmilk=50,regmilk=0, almondmilk=0, coffeebeans=18, sugar=2, price=4.90),
        Menulist(coffeeName="medium almondmilk ice cappuccino", water=210, almondmilk=50,oatmilk=0, regmilk=0, coffeebeans=18, sugar=2, price=4.90),
        Menulist(coffeeName="large regularmilk hot cappuccino", water=250, regmilk=70, oatmilk=0, almondmilk=0,coffeebeans=24, sugar=3, price=5.70),
        Menulist(coffeeName="large oatmilk hot cappuccino", water=250, oatmilk=70, regmilk=0, almondmilk=0, coffeebeans=24, sugar=3, price=5.90),
        Menulist(coffeeName="large almondmilk hot cappuccino", water=250,  almondmilk=70,oatmilk=0, regmilk=0, coffeebeans=24, sugar=3, price=5.90),    
        Menulist(coffeeName="large regularmilk ice cappuccino", water=260, regmilk=50,oatmilk=0, almondmilk=0, coffeebeans=24, sugar=3, price=5.70),
        Menulist(coffeeName="large oatmilk ice cappuccino", water=260, oatmilk=50, regmilk=0, almondmilk=0,coffeebeans=24, sugar=3, price=5.90),
        Menulist(coffeeName="large almondmilk ice cappuccino", water=260,  almondmilk=50,oatmilk=0, regmilk=0, coffeebeans=24, sugar=3, price=5.90),]

   #Create a menu system for every item set with its price
    def coffee(self):
      given_option=""
      for item in self.menu:
        given_option += f"☕{item.coffeeName} ${item.price:.2f}☕ \n"
      return given_option
    
    #Create a function to check if the user choice exists in the BakeryItem, if yes, return item, if not return None 
    def find_coffee(self,orderName):
      for item in self.menu:
          if item.coffeeName.lower() == orderName.lower():
            return item
      return None
