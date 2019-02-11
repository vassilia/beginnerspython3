class Account:
    """" A class used to represent a type of account """

    def __init__(self, account_number, account_holder, opening_balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = opening_balance
        self.type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

acc1 = Account('123', 'John', 10.05, 'current')
acc2 = Account('345', 'John', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')

acc1.deposit(23.45)
acc1.withdraw(12.33)
print(acc1.get_balance())

