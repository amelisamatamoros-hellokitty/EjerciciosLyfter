class BankAccount:

    def __init__(self,balance):
        self.balance=balance

    def deposit_money(self,deposit):
        self.balance+=deposit

    def withdraw_money(self,withdraw):
        if self.balance-withdraw>self.min_balance:
            self.balance-=withdraw
            print(f"Your withdrawal was successfull, your new balance is $ {self.balance}")
        else:
            print(f"You can't withdraw $ {withdraw}, because you won't meet the minimun required balance")

    
class SavingsAccount(BankAccount):

    def __init__(self,balance,min_balance):
        super().__init__(balance)  # hereda atributo de la clase padre
        self.min_balance=min_balance #atributo de la subclase


my_savings=SavingsAccount(100,25)
my_savings.withdraw_money(120)
my_other_savings=SavingsAccount(200,25)
my_other_savings.withdraw_money(120)
my_other_savings.withdraw_money(120)