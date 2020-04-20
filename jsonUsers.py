import json

class Users:
    def __init__(self,filename):
        with open(filename) as json_file:
            self.data = json.load(json_file)
        self.iid=[]
        self.firstname=[]
        self.lastname=[]

    def getIid(self):
        for element in self.data:
            self.iid.append(element["id"])
        return self.iid
    def getFirstName(self):
        for element in self.data:
            self.firstname.append(element["firstName"])
        return self.firstname
    def getLastName(self):
        for element in self.data:
            self.lastname.append(element["lastName"])
        return self.lastname
