from tkinter import *
import tkinter.font
from math import sqrt


class Paint:
    def __init__(self):
        self.window = Tk()
        self.drawField = Canvas(self.window, width=1200, height=600)
        self.menu = Menu(self.window)
        self.buildMenu()
        self.buildWindow()
        self.currDrawTool = 'arc'
        self.leftMouse = 'up'
        self.x1Pos, self.y1Pos = None, None

    def run(self):
        self.window.mainloop()

    def buildWindow(self):
        self.window.title('Paint')
        self.window.geometry('1200x600+400+100')
        self.window.resizable(0, 0)
        self.window.config(menu=self.menu)
        self.drawField.pack()
        self.drawField.bind("<Motion>", self.drawPencil)
        self.drawField.bind("<ButtonPress-1>", self.catchMouseDown)
        self.drawField.bind("<ButtonRelease-1>", self.catchMouseUp)

    def buildMenu(self):
        menu_list = Menu(self.menu, tearoff=1)
        menu_list.add_command(label='Pencil', command=(lambda: self.__setattr__('currDrawTool', 'pencil')))
        menu_list.add_command(label='Line', command=(lambda: self.__setattr__('currDrawTool', 'line')))
        menu_list.add_command(label='Oval', command=(lambda: self.__setattr__('currDrawTool', 'oval')))
        menu_list.add_command(label='Circle', command=(lambda: self.__setattr__('currDrawTool', 'circle')))
        menu_list.add_command(label='Arc', command=(lambda: self.__setattr__('currDrawTool', 'arc')))
        menu_list.add_command(label='Rectangle', command=(lambda: self.__setattr__('currDrawTool', 'rect')))
        menu_list.add_separator()
        menu_list.add_command(label='Quit', command=self.window.quit)
        self.menu.add_cascade(label='Tools', menu=menu_list)

    def catchMouseUp(self, event=None):
        print('up', event.x, event.y)
        self.leftMouse = 'up'

        if self.currDrawTool == 'line':
            self.drawLine(event)
        elif self.currDrawTool == 'rect':
            self.drawRectangle(event)
        elif self.currDrawTool == 'arc':
            self.drawArc(event)
        elif self.currDrawTool == 'oval':
            self.drawOval(event)
        elif self.currDrawTool == 'circle':
            self.drawCircle(event)

    def catchMouseDown(self, event=None):
        print('down', event.x, event.y)
        self.leftMouse = 'down'
        self.x1Pos = event.x
        self.y1Pos = event.y

    def drawPencil(self, event=None):
        if self.currDrawTool == 'pencil' and self.leftMouse == 'down':
            self.drawField.create_line(self.x1Pos, self.y1Pos, event.x, event.y)
            self.x1Pos = event.x
            self.y1Pos = event.y

    def drawLine(self, event=None):
        self.drawField.create_line(self.x1Pos, self.y1Pos, event.x, event.y)

    def drawRectangle(self, event=None):
        self.drawField.create_rectangle(self.x1Pos, self.y1Pos, event.x, event.y)

    def drawArc(self, event=None):
        self.drawField.create_arc(self.x1Pos, self.y1Pos, event.x, event.y, start=0, extent=150, style=ARC)

    def drawOval(self, event=None):
        self.drawField.create_oval(self.x1Pos, self.y1Pos, event.x, event.y)

    def drawCircle(self, event=None):
        r = sqrt((event.y - self.y1Pos) ** 2 + (event.x - self.x1Pos) ** 2)
        self.drawField.create_oval(self.x1Pos - r, self.y1Pos - r, self.x1Pos + r, self.y1Pos + r)


Paint().run()
