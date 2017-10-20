class State:
    onEarth = None
    onOrbit = None
    onOrbitGraph = None

    def __init__(self, onEarthIn, onOrbitIn ):
        self.OnEarth = onEarthIn
        self.OnOrbit = onOrbitIn

class Node:

    state = None
    pathCost = None
    launchNumber = None
    totalLaunches = None
    # same index corresponds to modules on that launch:
    launchesExecuted = None
    modulesOnLaunch = None

    def __init__(self, stateIn, pathCostIn, launchNumberIn, totalLaunchesIn, launchesExecutedIn, modulesOnLaunchIn):
        self.state = stateIn
        self.pathCost = pathCostIn
        self.launchNumber = launchNumberIn
        self.launchesExecuted = launchesExecutedIn
        self.modulesOnLaunch = modulesOnLaunchIn



if __name__ == '__main__':
    pass