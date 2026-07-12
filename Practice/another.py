class balling:
    def __init__(self, newyork, abuja, kano):
        self.newyork = newyork
        self.abuja = abuja
        self.kano = kano
    def summary(self):
        print("I" + self.newyork + str(self.abuja) + " in the" + self.kano + ", I realy miss it" )

balling1 = balling(" love ", 10, " vacation")
balling2 = balling(" visited ", 30," holidy")
balling3 = balling(" eat ", 23345, " vacation" )

balling1.summary()
balling2.summary()
balling3.summary()


