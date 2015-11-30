class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def pay(self, amount):
        self.balance-=amount

    def receive(self, amount):
        self.balance+=amount

    def print_balance(self):
        print('Balance of: '+str(self.name)+' is: '+str(self.balance))
        print( )

    def transfer(self, other, amount):
        self.pay(amount)
        other.receive(amount)


hal=BankAccount('Lakatos Nintendo', 100)
hal.pay(220)
feri=BankAccount('Kalanyos Rolex ', 700000000)
feri.transfer(hal, 200000)

feri.print_balance()
hal.print_balance()
