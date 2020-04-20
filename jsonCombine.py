import json
from jsonTasks import *
from jsonStatus import *
from jsonUsers import *

class Combine:
    def __init__(self):
        self.infolist=[]
        with open('tasks.json') as json_file:
            data = json.load(json_file)

            status=Status('status.json')
            statusidlist=status.getStatusId()
            users=Users('users.json')
            usersid=users.getIid()
            usersfirstname=users.getFirstName()
            userslastname=users.getLastName()
            
            for element in data:
                obj=Tasks()
                obj.setAssigneeId(element["assigneeId"])
                obj.setDescription(element["description"])
                obj.setDueDate(int(element["dueDate"][-2:]))
                obj.setIid(element["id"])
                obj.setStartDate(int(element["startDate"][-2:]))
                obj.setStatusId(element["statusId"])
                count=1
                for statuselement in statusidlist:
                    if statuselement==obj.getStatusId():
                        obj.setStatusNumber(count)
                    count=count+1
                count=0
                for usersidelement in usersid:
                    if usersidelement==obj.getAssigneeId():
                        obj.setInitials(usersfirstname[count][0]+userslastname[count][0])
                    count=count+1
                self.infolist.append(obj)

    def getInfo(self):
        return self.infolist
        
