# -*- coding: utf-8 -*-
from Tkinter import *
from math import *
from tkColorChooser import askcolor
import numpy as np
import time

class Application():
    
    def __init__(self, master):
        self.command = None
        self.commandData = None
        
        self.menu = -1
        self.color = "black"
        self.backgroundColor = "white"
        self.frame = Frame(master, background="white")
        self.frame1 = Frame(master, width=50, height=400, background="white")
        
        self.canv = Canvas(self.frame, width=600, height=600, background="white")
        
        self.buttonColor = Button(self.frame1, text="Цвет линии")
        self.buttonColorBackground   = Button(self.frame1, text="Цвет фона")
        self.buttonPrintLine  = Button(self.frame1, text="Нарисовать линию")
        self.buttonReset  = Button(self.frame1, text="Очистить")
        self.buttonPrintCircle  = Button(self.frame1, text="Нарисовать солнце")
        #self.buttonFill  = Button(self.frame1, text="Закрасить")
        
        self.consoleXY     = Entry(self.frame1, font="Arial 30", text="Xn Yn")
        self.consoleI     = Entry(self.frame1, font="Arial 30", text="Xc Yc")
        self.consoleR     = Entry(self.frame1, font="Arial 30", text="Radius")
        self.consoleA     = Entry(self.frame1, font="Arial 30", text="Angle")

        
        self.label1 = Label(self.frame1, font="Arial 10", text="Начало: ")
        self.label2 = Label(self.frame1, font="Arial 10", text="Конец: ")
        self.label3 = Label(self.frame1, font="Arial 10", text="Радиус: ")
        self.label4 = Label(self.frame1, font="Arial 10", text="Угол: ")
        
        
        self.l = Listbox(self.frame1)
        self.l.insert(END,  *('Брезенхем целочисленный', 'Брезенхем вещественный', 'Брезенхем с устранением ступенчатости', 'ЦДА', 'Стандартный'))
        for i in range(0, self.l.size()):
            if self.l.get(i)[0] == '-':
                self.l.itemconfig(i, foreground='gray', \
                             selectforeground='gray', \
                             selectbackground=self.l.itemcget(i, 'background'))
        self.l.grid(row = 5, column = 2)
        self.l.bind("<<ListboxSelect>>", self.get)
        
        self.frame.grid(row = 0, column = 1)
        self.frame1.grid(row=0, column=0)
        self.canv.grid(row=0, column=0)

        self.buttonColor.grid(row = 5, column = 0)
        self.buttonColorBackground.grid(row=5, column=1)
        self.buttonReset.grid(row=4, column=0)
        self.buttonPrintLine.grid(row=1, column=2)
        self.buttonPrintCircle.grid(row=3, column=2)
        
        self.consoleXY.grid(row=0, column=1)
        self.consoleI.grid(row=1, column=1)
        self.consoleR.grid(row=2, column=1)
        self.consoleA.grid(row=3, column=1)
        
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.label4.grid(row=3, column=0)

    def get(self, event):
        self.menu = event.widget.curselection()[0]
    
    def setDot(self, Dot):
        self.Dot = Dot
    
    def getColor(self):
        color = askcolor()
        self.color = color
    
    def getColorBackground(self):
        color = askcolor()
        self.Dot.changeColor(color[1])
    
    def setCommand(self, button, command):
        button["command"] = command
    
    def printLine(self):
        dataXY = self.consoleXY.get()
        dataXY = dataXY.split()
        dataI = self.consoleI.get()
        dataI = dataI.split()
        self.Dot.draw(float(dataXY[0]), float(dataXY[1]), float(dataI[0]), float(dataI[1]), self.color, self.menu)
    
    def printCircle(self):
        dataXY = self.consoleXY.get()
        dataXY = dataXY.split()
        dataI = self.consoleI.get()
        dataI = dataI.split()
        dataR = self.consoleR.get()
        dataR = dataR.split()
        dataA = self.consoleA.get()
        dataA = dataA.split()
        self.Dot.dr(float(dataR[0]), float(dataA[0]), self.color, self.menu)



class Dot():
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(width=600, height=600)
        self.master.create_image((600/2, 600/2), image=self.img, state="normal")

        self.xCentral = 300
        self.yCentral = 300
    
    def changeColor(self, color):
        for y in range(self.img.height()):
            for x in range(self.img.width()):
                self.img.put(color, (x, y))

    def draw(self, x1, y1, x2, y2, color, menu):
        if menu == 0:
            self.intBrLine(self.master, x1, y1, x2, y2, color[1])

        elif menu n== 1:
            self.floatBrLine(self.master, x1, y1, x2, y2, color[1])

        elif menu == 2:
            self.smoothBrLine(self.master, x1, y1, x2, y2, color[1])

        elif menu == 3:
            self.ddaLine(self.master, x1, y1, x2, y2, color[1])

        elif menu == 4:
            self.standartLine(self.master, x1, y1, x2, y2, color[1])

    def dr(self, r, a, color, menu):
        self.drawSun(self.master, 300, 300, r, a, color, menu)

    def drawSun(self, master, x1, y1, r, a, color, menu):
        bx = x1
        by = y1
        start = time.clock()
        end = time.clock()
        for i in np.arange(0, 360, a):
            ex = cos(radians(i)) * r + bx
            ey = sin(radians(i)) * r + by
            
            if menu == 3:
                start = time.clock()
                self.ddaLine(self.master, bx, by, ex, ey, color[1])
                end = time.clock()
            if menu == 1:
                start = time.clock()
                self.floatBrLine(self.master, bx, by, ex, ey, color[1])
                end = time.clock()
            if menu == 0:
                start = time.clock()
                self.intBrLine(self.master, bx, by, ex, ey, color[1])
                end = time.clock()
            if menu == 2:
                start = time.clock()
                self.smoothBrLine(self.master, bx, by, ex, ey, color[1])
                end = time.clock()
            if menu == 4:
                start = time.clock()
                self.standartLine(self.master, bx, by, ex, ey, color[1])
                end = time.clock()
        print(end-start)

    def standartLine(self, master, x1, y1, x2, y2, color):
        master.create_line(x1, y1, x2, y2, fill=color)
    
    def ddaLine(self, master, x1, y1, x2, y2, color):
        p1 = [x1, y1]
        p2 = [x2, y2]

        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]

        length = max(abs(delta_x), abs(delta_y))

        if round(length, 0) == 0:
            self.img.put(color, (int(p1[0]), int(p1[1])))
        
        dx = delta_x/length
        dy = delta_y/length
        
        x = round(p1[0], 0)
        y = round(p1[1], 0)
        
        points = []
        
        while length > 0:
            self.img.put(color, (int(round(x, 0)), int(round(y))))
            x += dx
            y += dy
            length -= 1
            
    def intBrLine(self, master, x1, y1, x2, y2, color):
        p1 = [x1, y1]
        p2 = [x2, y2]
        if p1 == p2:
            self.img.put(color, (int(p1[0]), int(p1[1])))
            return
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        x = p1[0]
        y = p1[1]

        change = False
        
        if dy > dx:
            temp = dx
            dx = dy
            dy = temp
            change = True

        e = 2 * dy - dx
        i = 1
        while i <= dx:
            self.img.put(color, (int(x), int(y)))
            if e >= 0:
                if change == 0:
                    y += sy
                else:
                    x += sx
                e -= 2 * dx
            
            if e < 0:
                if change == 0:
                    x += sx
                else:
                    y += sy
                e += (2 * dy)
            i += 1
    
    def floatBrLine(self, master, x1, y1, x2, y2, color):
        p1 = [x1, y1]
        p2 = [x2, y2]
        if p1 == p2:
            self.img.put(color, (int(p1[0]), int(p1[1])))
            return

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        x = p1[0]
        y = p1[1]

        change = False
        
        if dy > dx:
            dx, dy = dy, dx
            change = True

        h = dy / dx
        
        e = h - 0.5
        i = 1
        while i <= dx:
            self.img.put(color, (int(x), int(y)))
            if e >= 0:
                if change is False:
                    y += sy
                else:
                    x += sx
                e -= 1
            
            if e < 0:
                if change is False:
                    x += sx
                else:
                    y += sy
                e += h
            i+=1

    def smoothBrLine(self, master, x1, y1, x2, y2, color):
        p1 = [x1, y1]
        p2 = [x2, y2]

        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]

        max_intens = 4

        if round(max(abs(delta_x), abs(delta_y)), 0) == 0:
            self.img.put(color, (int(p1[0]), int(p1[1])))

        sx, sy = self.sign(delta_x), self.sign(delta_y)
        delta_x, delta_y = abs(delta_x), abs(delta_y)

        x, y = p1
        change = False

        if delta_y > delta_x:
            delta_x, delta_y = delta_y, delta_x
            change = True

        h = max_intens*delta_y/delta_x
        w = max_intens - h
        e = max_intens/2

        points = []
        i = 1
        while i <= delta_x:
            new = self.change_lightness(color, int(e), max_intens)
            self.img.put(new, (int(x), int(y)))
            if e <= w:
                if change:
                    y += sy
                else:
                    x += sx
                e += h
            else:
                x += sx
                y += sy
                e -= w
            i = i + 1
    
    def change_lightness(self, color, lvl, max_levels):
        rrggbb = color[1:3], color[3:5], color[5:7]
        rrggbb = [int(i, 16) for i in rrggbb]
        step = int(255/max_levels-1)
        for i in range(3):
            rrggbb[i] += lvl*step
            if rrggbb[i] > 255: rrggbb[i] = 255
            rrggbb[i] = hex(rrggbb[i])[2:]
        return "#" + "".join([str(i) if len(i)==2 else "0"+str(i) for i in rrggbb])
    
    def sign(self, x):
        if x == 0:
            return 0
        else:
            return x/abs(x)

    def reset(self):
        self.master.delete("all")
        self.img = PhotoImage(width=600, height=600)
        self.master.create_image((600/2, 600/2), image=self.img, state="normal")


def main():
    root = Tk()
    
    app = Application(root)
    dot = Dot(app.canv)
    app.setDot(dot)
    app.setCommand(app.buttonColor, app.getColor)
    app.setCommand(app.buttonColorBackground, app.getColorBackground)
    app.setCommand(app.buttonPrintLine, app.printLine)
    app.setCommand(app.buttonPrintCircle, app.printCircle)
    app.setCommand(app.buttonReset, dot.reset)
    root.mainloop()

if __name__ == "__main__":
    main()

