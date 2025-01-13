from CoffeeMenuItem import CoffeeMenu 
from bakeryItem import BakeryMenu
from shop import ShopInfo
from moneyMachine import MoneyMachine
from time import sleep

#import the classes from the files
#use python time module to use sleep() function to delay the shop start
def main():
  print('''                             ______________________
                            (___________           |
                              [XXXXX]   |          |
                         __  /~~~~~~~\  |          |
       CT               /  \|@@@@@@@@@\ |          |
         )              \   |@@@@@@@@@@||          |
        (                   \@@@@@@@@@@||  ______  |
       __)__                 \@@@@@@@@/ | |on|off| |
    C\|     \               __\@@@@@@/__|  ~~~~~~  |
      \     /              (____________|__________|
       \___/               |_______________________|''')

#credit to ccw@aloha.com

#set each class to a variable
  coffeemenu = CoffeeMenu()
  money= MoneyMachine()
  shop= ShopInfo()
  bakerymenu=BakeryMenu()

  print("Hello! Welcome to the Coffee Shop!!")
  while True:
    #Provide options for the user to choose from
    option=input(" 1.Bakery Menu \n 2.Coffee Menu \n 3.Shop Report \n 4.Exit the shop \nPlease type the option number.\n")
    
    if option == "1":
      print("Today on the Menu: \n ˏ⸉ˋ‿̩͙‿̩̩̥͙̽‿̩͙ 𝐵𝒶𝓀𝑒𝓇𝓎 𝑀𝑒𝓃𝓊 ‿̩̥̩‿̩̩̥͙̽‿̩͙ˊ⸊ˎ")
      print (" Plain Bagel ($3.00 \n Strawberry Cake ($4.00) \n Sesameseed Bagel ($3.50) \n Honey Bun ($4.00) \n Cinnamon Roll ($3.70) \n Crossiant ($3.00)")
      user_input=input(f"What would you like?\n(type 'Exit' to exit):").strip().title() #strip() removes any leading and trailing whitespaces 
      #title() converts the first letter of the input into a capital lett
      
      if user_input=="Exit":
        print("Have a nice day! ")
        break #Exit, ends the function

      selected_food=bakerymenu.find_food(user_input) #sends the function to bakeryItem.py file and checks if the food exists
      if selected_food is None:
        print("Please choose a valid food menu option.")
        continue #restarts back the function
      print (f"The selected food is: {selected_food.food} ${selected_food.price:.2f}")#sets the decimal point to 2 places

      if shop.resource_check(selected_food.ingredients): #checks if we have enough resource in shop.py file to supply the food
        payment=input("How would you like to pay, card or cash?").strip().lower() #lower() makes the string lowercased
        if payment=="cash":
          cashpay = money.insert_cash(selected_food.price)#The function continues in moneyMachine.py where it checks if the cash inserted enough or not
          if cashpay:
            print('Thank you! Please wait for your food')
            shop.food_return(selected_food)
            sleep(4) #delays the restart of option
        elif payment=="card":
          cardpay=money.add_card(selected_food.price)
          #The function continues in moneyMachine.py where it checks if the card number is valid or not, and if it has enough balance for payment
          if cardpay:
            print('Thank you! Please wait for your food')
            shop.food_return(selected_food)
            sleep(4)
        else: 
          print("invalid input")

    elif option=="2":
      print("Today on the Menu: \n*̩̩̥͙　-•̩̩͙-ˏˋ⋆𝒞𝑜𝒻𝒻𝑒𝑒 𝑀𝑒𝓃𝓊⋆ˊˎ-•̩̩͙-　*̩̩̥͙")
      print(coffeemenu.coffee()) #prints the menu from CoffeeMenuItem.py file
      user_input = input("Enter the name of the coffee you'd like to order \n(type 'Exit' to exit): ").strip().title().lower()
      
      if user_input=="Exit":
        break

      selected_coffee=coffeemenu.find_coffee(user_input) #checks if the choosen menu item exists or not
      if selected_coffee is None:
        print ("Please choose a coffee option from the given menu. ")
        continue
      print(f"The selected coffee is: {selected_coffee.coffeeName} ${selected_coffee.price:.2f}")
      if shop.resource_check(selected_coffee.ingredients): #checks if there is enough resources in shop.py file for the order to take place
        payment=input("How would you like to pay, card or cash? \n").strip().lower()
      
      if payment=="cash":
          cashpay = money.insert_cash(selected_coffee.price)
          if cashpay :
            print('Thank you! Please wait for your coffee ')
            shop.coffee_return(selected_coffee)
            sleep(4)
      elif payment=="card":
          cardpay=money.add_card(selected_coffee.price)
          if cardpay:
            print('Thank you! Please wait for your coffee')
            shop.coffee_return(selected_coffee)
            sleep(4)
      else: 
          print("invalid input")


    elif option == "3":
      shop.storagereport() #prints the updated storage report from shop.py file
      money.profit_report() #prints the updated profit report from moneyMachine.py

    elif option=="4":
      print("Thank you for visiting the Coffee Shop! Have a great day!")
      break

    else:
         print("Invalid option. Please choose from the available options.")

if __name__ == "__main__":
    main()
