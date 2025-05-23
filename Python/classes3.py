
interest_rate = 0.05 # global variables

class BankAccount():
    def __init__(self):
        self.__balance = 2000 # private variable
    
    def show_balance(self):
        return f"Balance: {self.__balance}"
    
    def calculate_interest(self):
        return int((self.__balance * interest_rate) + self.__balance)

account = BankAccount()
print(f"actual account balance - {account.show_balance()}")
# print(account.__balance)
print(f"balance after crediting interest - {account.calculate_interest()}")