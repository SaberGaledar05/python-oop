class Person:
    def __init__(self , first_name= 'unknown', last_name= 'unknown', account_balance= 0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = account_balance

    def account_top_up(self):
        top_up = int(input(f'Top up your account {self.first_name} {self.last_name}: '))
        if top_up > 0:
            self.account_balance += top_up
            return (f'your account has been topped up. '
                    f'Your current account balance : {self.account_balance} $ ')
        else:
            return "Value Error"

    def account_withdraw (self):
        withdraw = int(input(f'Enter your withdraw amount {self.first_name} {self.last_name}: '))
        if withdraw > 0 and withdraw <= self.account_balance:
            self.account_balance -= withdraw
            return (f'Your withdraw amount : {withdraw} $ '
                    f'Your current account balance : {self.account_balance} $ ')
        elif withdraw < 0:
            return "Value Error"
        elif withdraw > self.account_balance:
            return "Insufficient funds"

    def balance(self):
        return f'Your current account balance : {self.account_balance} $ '

    def account_info(self):
        return f'name: {self.first_name}, family: {self.last_name}, balance: {self.account_balance} $ '


