# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner          #public
#         self.__balance = balance      #private

#     def deposit(self, amount):
#         if amount > 0:
#            self.__balance += amount
#            print(f"Deposited {amount}")
#         else:
#             print("Invalid Deposit")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn {amount}")
#         else:
#             print(f"Invalid of Insufficient Balance")
    
#     def check_balance(self):
#         return self.__balance
    

# account = BankAccount("Salman", 1000)
# account.deposit(500)
# account.withdraw(300)
# print(account.check_balance())
# print(account.owner)
# print(account.__balance)