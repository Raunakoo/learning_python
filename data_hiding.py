class JustCounter:
    __secretcount = 0

    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)

counter = JustCounter()
counter.count()
counter.count()

print(counter._JustCounter__secretcount)
