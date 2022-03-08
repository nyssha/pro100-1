class atm (object):
    def __init__(self, card_number,pin_number,cashwithdrawl,balanceenquiry):
        self.card_number=card_number
        self.pin_number=pin_number
        self.cashwithdrawl=cashwithdrawl
        self.balanceenquiry=balanceenquiry

    def card_number(self):
        print(123456)

    def pin_number(self):
        print(654321)    

    def cashwithdrawl(self):
        print(100)    

    def balanceenquiry(self):
        print(180923)    

Bank=atm(123456,654321,100,180923)
Bank.card_number
