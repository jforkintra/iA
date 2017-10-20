import sys
from filereader import File


class Solver:
    file_name=None
    file = None
    solver_type= None


    def __init__(self, arguments):
        self.checkArgs(arguments)
        self.importFile(self.file_name)

    def solverType(self, argument):
        """Registers the type of solver invoqued"""
        if argument == "-i":
            self.solver_type = "informed"
        elif argument == "-u":
            self.solver_type = "uninformed"
        else:
            print("Problem with solver type, unknown type ", argument, " exiting")
            exit(-6)

    def checkArgs(self, arguments):
        if len(sys.argv) is not 3:
            print("Problem with number of arguments, exiting")
            exit(-7)
        else:
            self.solverType(arguments[1])
            self.file_name=arguments[2]

    def importFile(self, argument):
        self.file=File(argument)

if __name__ == '__main__':
    solve= Solver(sys.argv)
    print("ola")


