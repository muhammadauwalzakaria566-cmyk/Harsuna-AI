class wallet:
    def __init__(self, transfer, send, bonus):
        self.transfer= transfer
        self.send=send
        self.bonus=bonus
    def summary(self):
        print("you have " + self.transfer + " Transfer" + self.send + " send " + str (self.bonus))
wallet1 = wallet(" succefully"," tap the botton below ", 3000)
wallet2 = wallet (" not yet"," the money ",  1000 )

wallet1.summary()
wallet2.summary()