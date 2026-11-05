class BankAccount:

    def __init__(self,balance,min_balance):
        self._balance=balance
        self._min_balance=min_balance

    @property
    def balance(self):
        return self._balance

    @property
    def min_balance(self):
        return self._min_balance

    def deposit_money(self,deposit):
        if deposit<0:
            raise ValueError("Ammount to deposit can not be less than zero")
        self._balance+=deposit
        return self._balance

    def withdraw_money(self,withdraw):
        if withdraw<0:
            raise ValueError("Ammount to withdraw can not be less than zero")
        if self._balance-withdraw>=self._min_balance:
            self._balance-=withdraw
            print(f"Your withdrawal was successfull, your new balance is $ {self._balance}")
        else:
            raise ValueError(f"You can't withdraw $ {withdraw}, because you won't meet the minimun required balance")

    
class SavingsAccount(BankAccount):
    pass

try:
    my_savings=SavingsAccount(100,25)
    my_savings.withdraw_money(120)
except ValueError as e:
    print(e)

try:
    my_other_savings=SavingsAccount(200,25)
    my_other_savings.withdraw_money(120)
    my_other_savings.withdraw_money(120)
except ValueError as e:
    print(e)

try:
    bank_account=BankAccount(100,25)
    print(bank_account.deposit_money(-50))
except ValueError as e:
    print(e)

bank_account.balance=1000000
