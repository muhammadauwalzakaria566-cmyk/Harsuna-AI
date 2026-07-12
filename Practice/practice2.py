class artist:
    def __init__ (self, song, perform, stage):
        self.song = song
        self.perform = perform
        self.stage = stage
    def summary(self):
        print("The" + self.song + "He" + self.perform + "on" + self.stage + "go viral")
artist1 = artist(" vibes ", " sing ", " allow him to ")
artist2 = artist(" If not ", " is not ", " going to")
artist1.summary()
artist2.summary()
