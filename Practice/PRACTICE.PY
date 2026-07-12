class creator:
    def __init__(self, name, platform, subscribers):
      self.name = name
      self.platform = platform
      self.subscribers = subscribers
    def summary(self):
        print(" my name " + self.name + " and I create on " + self.platform +  "with " + str(self.subscribers) +  "subscribers")
creator1 = creator("Auwal",  "Youtube",  2000)
creator2 = creator("musa",  "youtube",  10000)

creator1.summary()
creator2.summary()