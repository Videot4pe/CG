from Tkinter import *
from math import sin, cos

class Application():
    def __init__(self, master):
        self.command = None
        self.commandData = None

        self.frame  = Frame(master, background="white")
        self.frame1 = Frame(master, background="white")
        self.canv   = Canvas(self.frame, width=600, height=600, background="white")
        
        self.buttonRotate = Button(self.frame1, text="Rotate", width=10)
        self.buttonMove   = Button(self.frame1, text="Move", width=10)
        self.buttonScal   = Button(self.frame1, text="Scale", width=10)
        self.buttonCenter   = Button(self.frame1, text="Center", width=10)
        self.buttonReset  = Button(self.frame1, text="Reset")
        
        self.consoleRotate = Entry(self.frame1, font="Arial 15", text="angle")
        self.consoleMove   = Entry(self.frame1, font="Arial 15", text="dx dy")
        self.consoleScal   = Entry(self.frame1, font="Arial 15", text="kx ky")
        self.consoleCenter   = Entry(self.frame1, font="Arial 15", text="xc yc")


        self.frame.grid(row = 0, column = 0)
        self.frame1.grid(row=0, column=1)
        self.canv.grid(row=0, column=0)
        
        self.buttonRotate.grid(row=2, column=1)
        self.buttonMove.grid(row = 2, column=2)
        self.buttonScal.grid(row=2, column=3)
        self.buttonCenter.grid(row=2, column=4)

        self.consoleRotate.grid(row=1, column=1)
        self.consoleMove.grid(row=1, column=2)
        self.consoleScal.grid(row=1, column=3)
        self.consoleCenter.grid(row=1, column=4)

        self.buttonReset.grid(row=3, column=1, columnspan=3)

    
    def setCommand(self, button, command):
        button["command"] = command
    
    def setSquare(self, square):
        self.square = square

    
    def getCommandMove(self):
        data = self.consoleMove.get()
        data = data.split()
        self.square.move(float(data[0]), -float(data[1]))


    def getCommandRotate(self):
        data = self.consoleRotate.get()
        data = data.split()
        self.square.rotate(float(data[0]))

    def getCommandScal(self):
        data = self.consoleScal.get()
        data = data.split()
        self.square.scaling(-float(data[0]), float(data[1]))

    def getCommandCenter(self):
        data = self.consoleCenter.get()
        data = data.split()
        self.square.center(float(data[0]), float(data[1]))



class Square():
    def __init__(self, master):
        self.master = master
        self.kx = 1
        self.ky = 1
        
        self.xm = 0
        self.ym = 0
        
        self.xc = 300 + self.xm
        self.yc = 250 + self.ym

        self.de = 100

        self.sin = 0
        self.cos = 1

        self.setCoordinats()
        self.drawSquare(self.master)

    def setCoordinats(self):
    	master = self.master
        kx = self.kx
        ky = self.ky
        xm = self.xm
        ym = self.ym
        xc = self.xc
        yc = self.yc
        s = self.sin
        c = self.cos
        de = self.de

        x1 = xc + (50-xm)*kx*c - (100-ym)*ky*s
        y1 = yc + (50-xm)*kx*s + (100-ym)*ky*c
        x2 = xc + (0-xm)*kx*c - (0-ym)*ky*s
        y2 = yc + (0-xm)*kx*s + (0-ym)*ky*c
        x3 = xc + (100-xm)*kx*c - (0-ym)*ky*s
        y3 = yc + (100-xm)*kx*s + (0-ym)*ky*c
        self.triangle  = [x1, y1, x2, y2, x3, y3]

        x1 = xc + (0-xm)*kx*c - (100-ym)*ky*s
        y1 = yc + (0-xm)*kx*s + (100-ym)*ky*c
        x2 = xc + (0-xm)*kx*c - (0-ym)*ky*s
        y2 = yc + (0-xm)*kx*s + (0-ym)*ky*c
        x3 = xc + (100-xm)*kx*c - (0-ym)*ky*s
        y3 = yc + (100-xm)*kx*s + (0-ym)*ky*c
        x4 = xc + (100-xm)*kx*c - (100-ym)*ky*s
        y4 = yc + (100-xm)*kx*s + (100-ym)*ky*c
        self.Square  = [x1, y1, x2, y2, x3, y3, x4, y4]

        x1 = xc + (0-xm)*kx*c - (0-ym)*ky*s
        y1 = yc + (0-xm)*kx*s + (0-ym)*ky*c
        x2 = xc + (10-xm)*kx*c - (2.5-ym)*ky*s
        y2 = yc + (10-xm)*kx*s + (2.5-ym)*ky*c
        x3 = xc + (20-xm)*kx*c - (4.5-ym)*ky*s
        y3 = yc + (20-xm)*kx*s + (4.5-ym)*ky*c
        x4 = xc + (30-xm)*kx*c - (6.5-ym)*ky*s
        y4 = yc + (30-xm)*kx*s + (6.5-ym)*ky*c
        x5 = xc + (40-xm)*kx*c - (7.5-ym)*ky*s
        y5 = yc + (40-xm)*kx*s + (7.5-ym)*ky*c
        x6 = xc + (50-xm)*kx*c - (8-ym)*ky*s
        y6 = yc + (50-xm)*kx*s + (8-ym)*ky*c
        x7 = xc + (60-xm)*kx*c - (7.5-ym)*ky*s
        y7 = yc + (60-xm)*kx*s + (7.5-ym)*ky*c
        x8 = xc + (70-xm)*kx*c - (6.5-ym)*ky*s
        y8 = yc + (70-xm)*kx*s + (6.5-ym)*ky*c
        x9 = xc + (80-xm)*kx*c - (4.5-ym)*ky*s
        y9 = yc + (80-xm)*kx*s + (4.5-ym)*ky*c
        x10 = xc + (90-xm)*kx*c - (2.5-ym)*ky*s
        y10 = yc + (90-xm)*kx*s + (2.5-ym)*ky*c
        x11 = xc + (100-xm)*kx*c - (0-ym)*ky*s
        y11 = yc + (100-xm)*kx*s + (0-ym)*ky*c
        self.oval1 = [x1,y1,x2,y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11]
        
        x1 = xc + (0-xm)*kx*c - (0-ym)*ky*s
        y1 = yc + (0-xm)*kx*s + (0-ym)*ky*c
        x2 = xc + (9-xm)*kx*c - (10-ym)*ky*s
        y2 = yc + (9-xm)*kx*s + (10-ym)*ky*c
        x3 = xc + (16-xm)*kx*c - (20-ym)*ky*s
        y3 = yc + (16-xm)*kx*s + (20-ym)*ky*c
        x4 = xc + (22-xm)*kx*c - (30-ym)*ky*s
        y4 = yc + (22-xm)*kx*s + (30-ym)*ky*c
        x5 = xc + (28-xm)*kx*c - (40-ym)*ky*s
        y5 = yc + (28-xm)*kx*s + (40-ym)*ky*c
        x6 = xc + (33-xm)*kx*c - (50-ym)*ky*s
        y6 = yc + (33-xm)*kx*s + (50-ym)*ky*c
        x7 = xc + (38-xm)*kx*c - (60-ym)*ky*s
        y7 = yc + (38-xm)*kx*s + (60-ym)*ky*c
        x8 = xc + (42-xm)*kx*c - (70-ym)*ky*s
        y8 = yc + (42-xm)*kx*s + (70-ym)*ky*c
        x9 = xc + (46-xm)*kx*c - (80-ym)*ky*s
        y9 = yc + (46-xm)*kx*s + (80-ym)*ky*c
        x10 = xc + (49-xm)*kx*c - (90-ym)*ky*s
        y10 = yc + (49-xm)*kx*s + (90-ym)*ky*c
        x11 = xc + (50-xm)*kx*c - (100-ym)*ky*s
        y11 = yc + (50-xm)*kx*s + (100-ym)*ky*c
        self.oval2 = [x1,y1,x2,y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11]
        
        x1 = xc + (100-xm)*kx*c - (0-ym)*ky*s
        y1 = yc + (100-xm)*kx*s + (0-ym)*ky*c
        x2 = xc + (91-xm)*kx*c - (10-ym)*ky*s
        y2 = yc + (91-xm)*kx*s + (10-ym)*ky*c
        x3 = xc + (84-xm)*kx*c - (20-ym)*ky*s
        y3 = yc + (84-xm)*kx*s + (20-ym)*ky*c
        x4 = xc + (78-xm)*kx*c - (30-ym)*ky*s
        y4 = yc + (78-xm)*kx*s + (30-ym)*ky*c
        x5 = xc + (72-xm)*kx*c - (40-ym)*ky*s
        y5 = yc + (72-xm)*kx*s + (40-ym)*ky*c
        x6 = xc + (67-xm)*kx*c - (50-ym)*ky*s
        y6 = yc + (67-xm)*kx*s + (50-ym)*ky*c
        x7 = xc + (62-xm)*kx*c - (60-ym)*ky*s
        y7 = yc + (62-xm)*kx*s + (60-ym)*ky*c
        x8 = xc + (58-xm)*kx*c - (70-ym)*ky*s
        y8 = yc + (58-xm)*kx*s + (70-ym)*ky*c
        x9 = xc + (54-xm)*kx*c - (80-ym)*ky*s
        y9 = yc + (54-xm)*kx*s + (80-ym)*ky*c
        x10 = xc + (51-xm)*kx*c - (90-ym)*ky*s
        y10 = yc + (51-xm)*kx*s + (90-ym)*ky*c
        x11 = xc + (50-xm)*kx*c - (100-ym)*ky*s
        y11 = yc + (50-xm)*kx*s + (100-ym)*ky*c
        self.oval3 = [x1,y1,x2,y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11]

        self.drawSquare(master)

    def move(self, dx, dy):
        self.xc += dx
        self.yc -= dy
        self.setCoordinats()
        self.master.delete("all")
        self.drawSquare(self.master)

    def rotate(self, angle):
        self.sin = sin(angle)
        self.cos = cos(angle)
        self.setCoordinats()
        self.master.delete("all")
        self.drawSquare(self.master)
        

    def scaling(self, kx, ky):
        self.kx = kx
        self.ky = ky
        self.setCoordinats()
        self.master.delete("all")
        self.drawSquare(self.master)
    
    def center(self, xc, yc):
        self.xc = xc
        self.yc = yc
        self.setCoordinats()
        self.master.delete("all")
        self.drawSquare(self.master)


    def drawSquare(self, master):
        master.create_polygon(self.Square, fill="", outline="black", width=2)
        master.create_polygon(self.triangle, fill="", outline="black", width=2)
        master.create_polygon(self.oval1, fill="", outline="black", width=2)
        master.create_polygon(self.oval2, fill="", outline="black", width=2)
        master.create_polygon(self.oval3, fill="", outline="black", width=2)
    
    
    def reset(self):
        self.kx = 1
        self.ky = 1
        
        self.xm = 0
        self.ym = 0
        
        self.xc = 300 + self.xm
        self.yc = 300 + self.ym
        
        self.de = 100
        
        self.sin = 0
        self.cos = 1
        
        self.setCoordinats()
        self.master.delete("all")
        self.drawSquare(self.master)
 
def main():
    root = Tk()

    app = Application(root)
    square = Square(app.canv)
    app.setSquare(square)
    app.setCommand(app.buttonMove, app.getCommandMove)
    app.setCommand(app.buttonRotate, app.getCommandRotate)
    app.setCommand(app.buttonScal, app.getCommandScal)
    app.setCommand(app.buttonCenter, app.getCommandCenter)
    app.setCommand(app.buttonReset, square.reset)

    root.mainloop()

if __name__ == "__main__":
    main()
