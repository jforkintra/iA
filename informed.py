from filereader import File
from node import Node
import queue


class Informed:

    modulesOnEarth = None
    modulesOnOrbit = {}
    goalOnOrbit = None
    launches = None


    def __init__(self, onEarthIn, launchesIn):
        self.modulesOnEarth = onEarthIn
        self.goalOnOrbit = onEarthIn
        self.launches = launchesIn








if __name__ == '__main__':
    file = File("mir.txt")