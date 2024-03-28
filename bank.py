# создать класс Accunt, которы полностью будет имитировать
# банковский счет. Класс должен включать атрибуты для хранения  идентификатора
# владельца, балагса счета  для депазита  (пополнения  и снятия средств .
# если на счету достаточно средств)

class Accout():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"удачно пополнили cчет. Счет: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"удачно сняли со счета {money}")
            print(f"Текущий баланс: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс: {self.balance} ")

man = Accout(123123123, 600)

man.all_balance()
man.withdraw(300)
man.withdraw(400)
man.deposit(1200)
man.all_balance()
