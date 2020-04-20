from tkinter import *
from jsonCombine import *

class Gantt:
    def __init__(self):
        self.master=Tk()
        self.info=Combine()#contains the info of all the tasks
        self.timeline_start=-1
        self.timeline_end=-1
        self.w=Canvas(self.master, width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())
        self.w.pack()
        self.globalwidth=-1
        self.globalheight=-1
        self.rectlist=[]
        
    '''setter of the timeline's start and end date'''
    def setTimeline(self):
        for t in self.info.getInfo():
            if self.timeline_start == -1:
                self.timeline_start=t.getStartDate()
                self.timeline_end=t.getDueDate()
            if self.timeline_start > t.getStartDate():
                self.timeline_start=t.getStartDate()
            if self.timeline_end < t.getDueDate():
                self.timeline_end=t.getDueDate()

    '''setter of the globalwidth and the globalheight'''       
    def setglobalVariables(self):
        self.globalwidth=int(self.master.winfo_screenwidth()/(self.timeline_end-self.timeline_start+2))
        self.globalheight=int(self.master.winfo_screenheight()/((len(self.info.getInfo())*2)+3))

    '''method for printing the dates at the top of the page'''
    def printDates(self):
        previousdates=[]
        for t in self.info.getInfo(): # instead of date[0] -> t.start_date
            if t.getStartDate() not in previousdates:
                self.w.create_text(self.globalwidth*(t.getStartDate()-self.timeline_start+1), self.globalheight, text=t.getStartDate())
                previousdates.append(t.getStartDate())
            if t.getDueDate() not in previousdates:  
                self.w.create_text(self.globalwidth*(t.getDueDate()-self.timeline_start+1), self.globalheight, text=t.getDueDate())
                previousdates.append(t.getDueDate())

    '''mothod for drawing the rectangle for the overlapping area'''
    def drawOverlap(self):
        overlap_start=self.info.getInfo()[0].getStartDate()
        overlap_end=self.info.getInfo()[0].getDueDate()
        for t in self.info.getInfo():
            if t.getStartDate()>overlap_start:
                overlap_start=t.getStartDate()
            if t.getDueDate()<overlap_end:
                overlap_end=t.getDueDate()
        if (overlap_start<overlap_end):
            self.w.create_rectangle(self.globalwidth*(overlap_start-self.timeline_start+1), 2*self.globalheight-(self.globalheight/5), self.globalwidth*(overlap_end-self.timeline_start+1),self.globalheight*(2*len(self.info.getInfo())+1)+(self.globalheight/5), fill="#DCDCDC", outline="")
    
    '''method for drawing the rectangles of each task '''
    def drawRectangles(self):
        height=self.globalheight*2
        for t in self.info.getInfo():
            colour=""
            if t.getStatusNumber()==1: # e.g. t.status_id == 1
                colour="#FF6347"
            elif t.getStatusNumber()==2:
                colour="#A9A9A9"
            elif t.getStatusNumber()==3:
                colour="#8B008B"
            else:
                colour="#9ACD32"
            self.rectlist.append(self.w.create_rectangle(self.globalwidth*(t.getStartDate()-self.timeline_start+1), height, self.globalwidth*(t.getDueDate()-self.timeline_start+1), height+self.globalheight, fill=colour, outline=""))
            self.w.create_text(self.globalwidth*(t.getDueDate()-self.timeline_start+1)-self.globalwidth/2, height+self.globalheight/2, text=t.getInitials(),fill="white")
            self.w.create_text(self.globalwidth*(t.getStartDate()-self.timeline_start+1)+(self.globalwidth/10)*len(t.getDescription()), height+self.globalheight/2, text=t.getDescription(),fill="white")
            height=height+2*self.globalheight

    '''method for checking mouse clicks'''
    def mouseHandling(self):
        def on_click (shape):
            def on_click (e):
                for shape1 in self.rectlist:
                    self.w.itemconfig(shape1, outline="")
                self.w.itemconfig(shape, outline="black")
            return on_click

        for shape in self.rectlist:
            self.w.tag_bind(shape, '<Button-1>', on_click(shape))

          
