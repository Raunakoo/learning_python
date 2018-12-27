class Character():
    def __init__(self,name):
        self.name = name

    def running(self):     
        print("{} is running".format(self.name))

John = Character("John")
John.running()

Mary = Character("Mary")
Mary.running()

class Person():
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def info(self):
        print("i am {} and my score {}".format(self.name, self.score))


class Mary(Person):
    def __init__(self,name,score):
        self.name = name
        self.score = score

mary = Mary("Mary", 4555)
mary.info()