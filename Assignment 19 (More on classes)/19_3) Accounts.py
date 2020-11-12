class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)

class SavingsAccount(Account):
    INTEREST = 0.05
    BONUS = 0.1

    def update_balance(self):
        self.balance += (self.balance * self.INTEREST) + (self.balance * self.BONUS)

class DebitAccount(Account):
    INTEREST = 0.02

    def update_balance(self):
        self.balance += self.balance * self.INTEREST



###############################
# def print_accounts(accounts):
#     for account in accounts:
#         print(account)
#     print()

# def update_accounts(accounts):
#     for account in accounts:
#         account.update_balance()

# sav1 = SavingsAccount(1000)
# deb1 = DebitAccount(1000)
# sav2 = SavingsAccount(2000)
# deb2 = DebitAccount(4000)

# accounts = [sav1, deb1, sav2, deb2]
# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)