class bankAccount:
    def __init__(self, int_rate=0.03, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrew(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging $5.00 fee")
            self.balance -= 5
        return self
    def account_information(self):
        print(f"Balance: ${self.balance}")
        return self
    def interest(self):
        self.balance *= 1 + self.int_rate
        return self
melissa= bankAccount(0.08, 1000)
melissa.deposit(500).deposit(90).deposit(5).withdrew(752).interest().account_information()

richard= bankAccount(0.05, 10)
richard.deposit(500).deposit(200).withdrew(88).withdrew(286).withdrew(80).withdrew(100).interest().account_information()
