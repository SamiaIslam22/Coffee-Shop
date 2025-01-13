class MoneyMachine:
    currency = "$"
#set currency to $
    def __init__(self):
        self.profit = 0.0
#start of profit with 0.0 at the beginning of the shop and add on every time an item is purchased
    def profit_report(self):
        print(f"Money: {self.currency}{self.profit}")

    def insert_cash(self, amount): #Cash option
        cash_input = float(input(f"Insert {self.currency}{amount:.2f} in cash: ")) #asks to insert money 
        if cash_input >= amount:#checks if the input money is larger than or equal to the price of the item.
            #if larger, give back change by subtracting the price from the input money
            change = cash_input - amount
            self.profit += amount #add the profit made to self.profit
            print(f"Thank you! Here's your change: {self.currency}{change:.2f}") #give back change
            return True
        else:
            print("Insufficient cash. Please insert the correct amount.")
            return False

    def add_card(self, amount): #Card option
      while True:
        try:
          card_number = int(input("Enter your card number: ")) #use error handling to make sure only integers are used as input
        except ValueError:
          print("Invalid card number.")
          continue
        try: 
          card_balance = float(input("Enter your card balance: ")) #use error handling to make sure only float are used as input
        except ValueError:
          print("Invalid card balance")
          continue
        if card_balance >= amount:#checks if the input money is larger than or equal to the price of the item.
          
            self.profit += amount#add the profit made to self.profit
            remaining_balance = card_balance - amount  #if larger, give back change by subtracting the price from the input money
            print(f"Payment successful. Remaining card balance: {self.currency}{remaining_balance:.2f}")#give back change
            return True
        else:
            print("Insufficient card balance. Please use a different payment method.")
            return False
