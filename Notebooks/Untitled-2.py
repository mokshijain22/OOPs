
# name = input("Enter your name: ")

# while True:
#        print(name)
#        if input()=="         ":
#               break

# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance  

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  
class CoffeeMachine:
    def __init__(self):
        self.__coffee_beans = 10  

    def make_coffee(self):
        if self.__coffee_beans > 0:
            print("Making coffee...")
            self.__coffee_beans -= 1
            return "Coffee is ready!"
        else:
            return "No coffee beans left!"

machine = CoffeeMachine()
print(machine.make_coffee())  
print(machine.make_coffee())  
print(machine.__coffee_beans)  