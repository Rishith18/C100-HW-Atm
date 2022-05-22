class Atm():
    def __init__(self, cardNum, pinNum, balance):
        self.cardNum = cardNum
        self.pinNum = pinNum
        self.balance = balance

    def CashWithdrawl(self):
        print("Withdrew Cash")
    
    def BalanceEnquiry(self, balance):
        print("Your balance is",self.balance,"dollars")

bob_acc = Atm(123467, 123456, 12567)

bob_acc.CashWithdrawl()
bob_acc.BalanceEnquiry(bob_acc)

