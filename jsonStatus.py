import json

class Status:
    def __init__(self,filename):
        with open(filename) as json_file:
            self.data = json.load(json_file)
        self.statusid=[]
        self.statusname=[]

    def getStatusId(self):
        for element in self.data:
            self.statusid.append(element["id"])
        return self.statusid
    def getStatusName(self):
        for element in self.data:
            self.statusname.append(element["name"])
        return self.statusname

