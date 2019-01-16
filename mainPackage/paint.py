from tkinter import *
import tkinter.font


class Paint:
    def __init__(self):
        # class variables
        self.window = Tk()
        self.drawField = Canvas(self.window,width=400,height=400)
        self.buildWindow()
        self.xPos, self.yPos = None, None
        self.currDrawTool = 'pencil'
        self.leftMouse = 'up'
        self.x1Pos, self.x1Pos, self.x1Pos, self.x1Pos = None, None, None, None,

    def run(self):
        self.window.mainloop()

    def buildWindow(self):
        self.window.title('Paint')
        self.window.geometry('400x400+400+100')
        self.window.resizable(0, 0)
        self.drawField.pack()
        self.drawField.bind("<Motion>", self.motion)
        self.drawField.bind("<ButtonPress-1>", self.catchMouseDown)
        self.drawField.bind("<ButtonRelease-1>", self.catchMouseUp)

    def motion(self, event=None):
        print('motion', event.x, event.y)
        pass
        # TODO motion

    def catchMouseUp(self, event=None):
        print('up', event.x, event.y)
        pass
        # TODO cmu

    def catchMouseDown(self, event=None):
        print('down', event.x, event.y)
        pass

    def drawPencil(self):
        pass
        # TODO draw pencil

    def drawLine(self):
        pass
        # TODO draw line

    def drawRectangle(self):
        pass
        # TODO draw rect

    def drawArc(self):
        pass
        # TODO draw arc

    def drawCircle(self):
        pass
        # TODO draw Circle


Paint().run()
