from random import randint


class Packet():
    def __init__(self):
        self.source = randint(0,10)
        self.destination = randint(0,10)
        self.path = []
        self.information = self.randomDigits(10)

    def __str__(self):
        return 'Source: ' + str(self.source) + ", " +'Destination: ' + str(self.destination) \
                + '\n' + "Information: " + str(self.information)

    def randomDigits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    #going to have a function that creates the path that the packet will travel here

