import json

class Tasks:
    def __init__(self):
        self.assigneeid=""
        self.description=""
        self.duedate=0
        self.iid=""
        self.startdate=0
        self.statusid=""
        self.initials="" 
        self.statusnumber=0

    def getAssigneeId(self):
        return self.assigneeid
    
    def setAssigneeId(self,assigneeid):
        self.assigneeid=assigneeid
        
    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description=description
        
    def getDueDate(self):
        return self.duedate

    def setDueDate(self,duedate):
        self.duedate=duedate

    def getIid(self):
        return self.iid

    def setIid(self,iid):
        self.iid=iid

    def getStartDate(self):
        return self.startdate

    def setStartDate(self,startdate):
        self.startdate=startdate

    def getStatusId(self):
        return self.statusid
    
    def setStatusId(self,statusid):
        self.statusid=statusid

    def getInitials(self):
        return self.initials
    
    def setInitials(self,initials):
        self.initials=initials

    def getStatusNumber(self):
        return self.statusnumber
    
    def setStatusNumber(self,statusnumber):
        self.statusnumber=statusnumber
