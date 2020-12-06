from random import randint


class Packet():
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.payload = "Message"
        self.header = ""

    def __str__(self):
        return 'Source: ' + str(self.source) + ", " +'Destination: ' + str(self.destination) \
                + '\n'

    def randomDigits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    #going to have a function that creates the path that the packet will travel here

