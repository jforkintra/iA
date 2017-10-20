import datetime


class File:

    filename = None
    file = None
    lines = None
    vertices = {}
    vertices_list =[]
    edges = {}
    launchs = []

    def __init__(self, filename=None):
        """Receives the filename and analyzes the entire file, parsing the information
        into the appriate structures"""
        self.filename = filename
        if self.filename is not None:
            self.fileReader()
            self.scanFile()
            self.orderLauches()
        else:
            print("A filename is needed")

    def fileOpener(self):
        """Opens the file with proper exception handling"""
        if self.filename is not None:
            try:
                self.file = open(self.filename)
            except Exception:
                print("File not valid at fileOpener, exiting")
                exit(-8)
            else:
                print("File opened")
        return

    def fileReader(self):
        """Reads the file and processes it's content"""
        try:
            self.fileOpener()
            self.lines = self.file.readlines()
        except Exception:
            print("error at fileReader(), exiting")
            exit(-9)
        else:
            print("Lines aquired")

    def vertAcq(self, line):
        """Acquires the vertices information"""
        #temp = line.split(" ", 1)
        temp = line.split()
        if temp[0] not in self.vertices.keys():
            try:
                self.vertices[temp[0]] = float(temp[1])
                self.vertices_list.append(temp[0])
            except ValueError:
                print("Value is not a float at vertAcq()")

    # Editei isto. se a key já estiver no dict, adicionas o outro cenas a essa key.
    # pode haver mais que uma cena p cada key
    # ou se calhar isto já faz e sou conas -> não fazia, tks
    def edgeAcq(self,line):
        temp = line.split("\n", 1)
        #temp = temp[0].split(" ", 2)
        temp = temp[0].split()
        if temp[1] not in self.edges.keys():
            self.edges[temp[1]] = [temp[2]]
        else:
            self.edges[temp[1]].append(temp[2])
        if temp[2] not in self.edges.keys():
            self.edges[temp[2]] = [temp[1]]
        else:
            self.edges[temp[2]].append(temp[1])

    def launchAcq(self, line):
        """Acquires the launchs information"""
        temp_date = {}
        temp = line.split("\n", 1)
        temp = temp[0].split()
        #temp = temp[0].split(" ", 4)

        temp_date["day"] = int(temp[1][0:2])
        temp_date["month"] = int(temp[1][2:4])
        temp_date["year"] = int(temp[1][4:])
        unix_timestamp= datetime.datetime(temp_date["year"], temp_date["month"], temp_date["day"])

        temp_launch=[unix_timestamp, temp_date, float(temp[2]), float(temp[3]), float(temp[4])]
        self.launchs.append(temp_launch)

    def scanFile(self):
        """Rules for parsing the different kinds of line inputs"""
        for line in self.lines:
            if line[0] == "V":
                self.vertAcq(line)
            elif line[0] == "E":
                self.edgeAcq(line)
            elif line[0] == "L":
                self.launchAcq(line)
            else:
                pass

    def orderLauches(self):
        """Orders the launchs by descending date. Makes it easy to pop lauches from the
        structure"""
        self.launchs = sorted(self.launchs, key = lambda launch: launch[0], reverse=True)


if __name__ == '__main__':
    file = File("mir.txt")
    print((file.vertices_list))