from practice1 import Person

saber = Person('Saber','Galedar')
ali = Person('Ali','safari', 250000)
print(saber.account_top_up())
print(saber.account_withdraw())
print(ali.account_top_up())
print(ali.account_withdraw())
print(saber.account_balance)
print(saber.account_info())
print(ali.account_balance)
print(ali.account_info())