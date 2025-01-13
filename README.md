This coffee shop has a coffee menu section and a bakery menu section. Based on the user's preference, they can purchase from whichever menu. 

The program starts with a welcome print and ASCII art which goes credited to ccw@aloha.com, followingly, the function asks for an option among the four given options. The options are, "1. Bakery Menu \n 2.Coffee Menu \n 3. Shop Report \n 4. Exit the shop \nPlease type the option number.\n"

Based on the option, the function will move to different files to gather the resources and place the order. If "Exit" is used in the middle of ordering from a menu, the program will end until started over again. 

If the user chooses option 1, the program then checks if the food item exits in the bakeryItem.py file, if yes, it checks if there is enough of that item in storage. If the food item does not exist, the program asks for a valid food choice from the menu. If there is not enough of that food item left in storage, the program asks the user to choose something else from the menu. 


Afterward, the payment process begins where the user is asked if they would like to pay in cash or card. If cash, insert more or equal amount of price, else the program will print an insufficient amount entered. If more than the necessary amount of cash is paid, the program gives back change. If the user chooses a card, enter a valid number for the card. We used error handling for card numbers. If characters other than integers are inputted, the program asks for a valid number. Then, the program asks to put in a balance. Similar to cash, if the input is more or equal amount of the price, the program gives back change, else, the program will print an insufficient amount entered.

If the user chooses option 2, the program checks if the coffee item exists in the CoffeeMenuItem.py file. A similar process starts as option 1.

Option 3 prints the updated storage report from the ShopInfo.py file and the profit report from the moneyMachine.py file.

Option 4 exits the function. 
