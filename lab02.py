# -*- coding: utf-8 -*-
from Tkinter import *
from math import *

class Application():
    
    def __init__(self, master):
        self.command = None
        self.commandData = None
        
        self.frame = Frame(master, background="white")
        self.frame1 = Frame(master, width=50, height=400, background="red")
        #self.frame2 = Frame(master, background="white")
        
        
        self.canv = Canvas(self.frame, width=600, height=600, background="white")
        
        self.buttonDot   = Button(self.frame1, text="Добавить")
        self.buttonDel   = Button(self.frame1, text="Удалить")
        self.buttonChange   = Button(self.frame1, text="Изменить")
        self.buttonCount  = Button(self.frame1, text="Нарисовать")
        self.buttonReset  = Button(self.frame1, text="Очистить")
        self.buttonPrint  = Button(self.frame1, text="Точки")
        self.buttonFill  = Button(self.frame1, text="Закрасить")
        
        self.consoleXY     = Entry(self.frame1, font="Arial 30", text="Array Xc Yc")
        self.consoleI     = Entry(self.frame1, font="Arial 30", text="a, i")
        self.consoleAXY     = Entry(self.frame1, font="Arial 30", text="Array Number Xc Yc")
        
        self.label  = Label(self.frame, text="0 . 0")
        self.label1 = Label(self.frame1, font="Arial 10", text="Point coordinates: ")
        self.label2 = Label(self.frame1, font="Arial 10", text="Dot number: ")
        self.label3 = Label(self.frame1, font="Arial 10", text="Dot number and coordinates: ")
        
        self.frame.grid(row = 0, column = 1)
        self.frame1.grid(row=0, column=0)
        self.canv.grid(row=0, column=0)
        
        self.buttonDot.grid(row=0, column=1)
        self.buttonDel.grid(row=1, column=1)
        self.buttonChange.grid(row=2, column=1)
        self.buttonReset.grid(row=3, column=0)
        self.buttonCount.grid(row=4, column=1)
        self.buttonPrint.grid(row=4, column=2)
        self.buttonFill.grid(row=4, column=3)
        
        self.consoleXY.grid(row=0, column=0)
        self.consoleI.grid(row=1, column=0)
        self.consoleAXY.grid(row=2, column=0)
        
        
        #self.label.grid(row=5, column=0 )
        #self.label1.grid(row=0, column=1)
        #self.label2.grid(row=1, column=1)
    
    
    
    def getMousePos(self, event):
        self.label["text"] = "{} . {}".format((event.x-300), (300-event.y))
    
    def setCommand(self, button, command):
        button["command"] = command
    
    def setDot(self, Dot):
        self.Dot = Dot
    
    def getCommandCount(self):
        self.Dot.count()
    
    def getCommandPrint(self):
        self.Dot.printD()
    
    def getCommandDot(self):
        dataXY = self.consoleXY.get()
        dataXY = dataXY.split()
        self.Dot.dot(float(dataXY[0]), float(dataXY[1]), float(dataXY[2]))
    
    def getCommandDel(self):
        dataI = self.consoleI.get()
        self.Dot.ddel(int(dataI[0]), int(dataI[2]))

    def getCommandChange(self):
        dataAXY = self.consoleAXY.get()
        dataAXY = dataAXY.split()
        self.Dot.change(int(dataAXY[0]), int(dataAXY[1]), float(dataAXY[2]), float(dataAXY[3]))

    def getCommandFill(self):
        self.Dot.fill()



class Dot():
    def __init__(self, master):
        self.master = master
        self.dots1 = []
        self.dots2 = []
        self.dotsResult1 = []
        self.dotsResult2 = []
        self.sum = 0

        self.xCentral = 300
        self.yCentral = 300
        self.k = 1
        
        #self.setCoordinats()
        self.drawDot(self.master)
    
    
    #def setCoordinats(self):
    #xc = self.xCentral
    #yc = self.yCentral
    
    
    
    def dot(self, a, x, y):
        
        #y = -y
        
        dot = [x, y]
        if (a == 1):
            self.dots1.append(dot)
        else:
            self.dots2.append(dot)

        self.scaling()
        self.drawDot(self.master)

    def printD(self):
        self.master.delete("all")
        
        i = 0
        
        print("1 Bunch")
        for dot in self.dots1:
            i+=1
            s = str(i) + ") " + str(dot[0]) + " " + str(dot[1])
            print(s)
        print("2 Bunch")
        i = 0
        for dot in self.dots2:
            i+=1
            s = str(i) + ") " + str(dot[0]) + " " + str(dot[1])
            print(s)
        self.drawDot(self.master)
    
    def ddel(self, a, i):
        self.master.delete("all")
        
        if (a == 1):
            self.dots1.pop(i)
        else:
            self.dots2.pop(i)
        self.dotsResult1 = []
        self.dotsResult2 = []
        self.count()
        self.drawDot(self.master)
    
    def reset(self):
        self.dots1 = []
        self.dots2 = []
        self.dotsResult1 = []
        self.dotsResult2 = []
        self.sum = 0
        
        self.xCentral = 300
        self.yCentral = 300
        self.k = 1
        self.drawDot(self.master)
    
    def drawDot(self, master):
        k = self.k
        self.master.delete("all")
        master.create_line([self.xCentral,-600,self.xCentral,450], fill="grey", width=1)
        master.create_line([-600,self.yCentral,600,self.yCentral], fill="grey", width=1)
        
        i = 1
        for dot in self.dots1:
            x = dot[0]*k + self.xCentral
            y = self.yCentral - dot[1]*k
            master.create_oval(x-3,y-3,x+3,y+3, fill="blue", width=1)
            s = str(dot[0]) + ' ' + str(dot[1])
            master.create_text(x, y+8, text = s, fill="black", font=("Helvectica", "8"))
            i = i + 1
        for dot in self.dots2:
            x = dot[0]*k + self.xCentral
            y = self.yCentral - dot[1]*k
            master.create_oval(x-3,y-3,x+3,y+3, fill="green", width=1)
            s = str(dot[0]) + ' ' + str(dot[1])
            master.create_text(x, y+8, text = s, fill="black", font=("Helvectica", "8"))
            i = i + 1

    def scaling(self):
        dx = 1
        dy = 1
        for dot in self.dots1:
            x = dot[0]
            y = dot[1]
            if (abs(x) > dx):
                dx = abs(x)
            if (abs(y) > dy):
                dy = abs(y)
        for dot in self.dots2:
            x = dot[0]
            y = dot[1]
            if (abs(x) > dx):
                dx = abs(x)
            if (abs(y) > dy):
                dy = abs(y)
        if (dx > dy):
            self.k = int(300/(dx+1))
        else:
            self.k = int(300/(dy+1))

    def checkForScale(self, xc1, xc2, yc1, yc2, r1, r2):
        dx = 1
        dy = 1
        if (abs(xc1) > dx):
            dx = abs(xc1+2*r1)
        if (abs(yc1) > dy):
            dy = abs(yc1+2*r1)
        if (abs(xc2) > dx):
            dx = abs(xc2+2*r2)
        if (abs(yc2) > dy):
            dy = abs(yc2+2*r2)

        if (dx > dy):
            self.k = int(300/(dx+1))
        else:
            self.k = int(300/(dy+1))

    def count(self):
        if (len(self.dots1) > 2 and len(self.dots2)) > 2:
            for i1 in range(0, len(self.dots1), 1):
                for i2 in range(i1, len(self.dots1), 1):
                    for i3 in range(i2, len(self.dots1), 1):
                        if (self.checkTriangle(self.dots1[i1][0], self.dots1[i1][1], self.dots1[i2][0], self.dots1[i2][1], self.dots1[i3][0], self.dots1[i3][1]) == 1):
                            for j1 in range(0, len(self.dots2), 1):
                                for j2 in range(j1, len(self.dots2), 1):
                                    for j3 in range(j2, len(self.dots2), 1):
                                        if (self.checkTriangle(self.dots2[j1][0], self.dots2[j1][1], self.dots2[j2][0], self.dots2[j2][1], self.dots2[j3][0], self.dots2[j3][1]) == 1):
                                            if (self.checkCircles(i1, i2, i3, j1, j2, j3) == 1):
                                                if (self.checkForAll(i1, i2, i3, j1, j2, j3) > self.sum):
                                                    self.sum = self.checkForAll(i1, i2, i3, j1, j2, j3)
                                                    dot1 = [self.dots1[i1][0], self.dots1[i1][1]]
                                                    dot2 = [self.dots1[i2][0], self.dots1[i2][1]]
                                                    dot3 = [self.dots1[i3][0], self.dots1[i3][1]]
                                                    dot4 = [self.dots2[j1][0], self.dots2[j1][1]]
                                                    dot5 = [self.dots2[j2][0], self.dots2[j2][1]]
                                                    dot6 = [self.dots2[j3][0], self.dots2[j3][1]]
                                                    self.dotsResult1 = []
                                                    self.dotsResult2 = []
                                                    self.dotsResult1.append(dot1)
                                                    self.dotsResult1.append(dot2)
                                                    self.dotsResult1.append(dot3)
                                                    self.dotsResult2.append(dot4)
                                                    self.dotsResult2.append(dot5)
                                                    self.dotsResult2.append(dot6)
                                                    print("Current sum = ")
                                                    print(self.sum)
    
        self.drawPicture(self.master)

    def change(self, a, n, x, y):
        dot = [x, y]
        if (a == 1):
            try:
                self.dots1[n] = dot
            except IndexError:
                self.dots1.append(dot)
        elif (a == 2):
            try:
                self.dots2[n] = dot
            except IndexError:
                self.dots2.append(dot)
        self.dotsResult1 = []
        self.dotsResult2 = []
        self.scaling()
        self.drawDot(self.master)

    def fill(self):
        self.fillThis(self.master)

    def fillThis(self, master):
        try:
            x1 = self.dotsResult1[0][0]
            x2 = self.dotsResult1[1][0]
            x3 = self.dotsResult1[2][0]
            y1 = self.dotsResult1[0][1]
            y2 = self.dotsResult1[1][1]
            y3 = self.dotsResult1[2][1]
            
            A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
            B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
            C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
            D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
            xc1 = -(B/(2*A))
            yc1 = -(C/(2*A))
            r1 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
            
            x1 = self.dotsResult2[0][0]
            x2 = self.dotsResult2[1][0]
            x3 = self.dotsResult2[2][0]
            y1 = self.dotsResult2[0][1]
            y2 = self.dotsResult2[1][1]
            y3 = self.dotsResult2[2][1]
            
            A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
            B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
            C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
            D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
            xc2 = -(B/(2*A))
            yc2 = -(C/(2*A))
            r2 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
            
            self.checkForScale(xc1, xc2, yc1, yc2, r1, r2)
            self.drawDot(self.master)
            
            dx = xc2 - xc1
            dy = yc2 - yc1
            d = sqrt(dx*dx + dy*dy)
            between = r1 / (r1 + r2)
            d1 = d * between
            d2 = d - d1
            sq = fabs(d1*r1 - d2*r2)
            
            k = self.k
            
            left_x = xc1 - r1
            left_y = yc1 - r1
            right_x = xc1 + r1
            right_y = yc1 + r1
            x1 = left_x*k + self.xCentral
            y1 = self.yCentral - left_y*k
            x2 = right_x*k + self.xCentral
            y2 = self.yCentral - right_y*k
            master.create_oval(x1,y1,x2,y2, width=1, outline='blue')
            
            left_x2 = xc2 - r2
            left_y2 = yc2 - r2
            right_x2 = xc2 + r2
            right_y2 = yc2 + r2
            x3 = left_x2*k + self.xCentral
            y3 = self.yCentral - left_y2*k
            x4 = right_x2*k + self.xCentral
            y4 = self.yCentral - right_y2*k
            master.create_oval(x3,y3,x4,y4, width=1, outline='green')
            #master.create_oval((x1+d1)*k + self.xCentral + 2,self.yCentral - (yc1+d1)*k + 2,(x1+d1)*k + self.xCentral - 2,self.yCentral - (yc1+d1)*k - 2, width=10, outline='red')
            
            d = sqrt((xc2-xc1)**2 + (yc2-yc1)**2)
            
            master.create_line(xc1*k + self.xCentral, self.yCentral - yc1*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="red", width=1)
            
            r3 = r2 + r1
            dx = xc2 - xc1
            dy = yc2 - yc1
            dd = sqrt(dx * dx + dy * dy)
            a = asin(r3 / dd)
            b = atan2(dy, dx)
            
            t = b - a
            taX = xc2 + r3 * sin(t)
            taY = yc2 + r3 * -cos(t)
            
            t = b + a
            tbX = xc2 + r3 * -sin(t)
            tbY = yc2 + r3 * cos(t)
            
            ddx = xc2 - taX
            ddy = yc2 - taY
            d = sqrt(dx**2 + dy**2)
            
            dx2 = xc2 - tbX
            dy2 = yc2 - tbY
            d2 = sqrt(dx2**2 + dy2**2)
            
            ko = r1/(r1+r2)
            xmid = xc1 + (xc2-xc1)*ko
            ymid = yc1 + (yc2-yc1)*ko
            
            master.create_line((xc1 + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + ddy*(r1/(r1+r2)))*k, (taX + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (taY + ddy*(r1/(r1+r2)))*k, fill="black", width=1)
            master.create_line((xc1 + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + dy2*(r1/(r1+r2)))*k, (tbX + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (tbY + dy2*(r1/(r1+r2)))*k, fill="black", width=1)
            
            master.create_line((xc1 + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + ddy*(r1/(r1+r2)))*k, xc1*k + self.xCentral, self.yCentral - yc1*k, fill="black", width=1)
            master.create_line((xc1 + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + dy2*(r1/(r1+r2)))*k, xc1*k + self.xCentral, self.yCentral - yc1*k, fill="black", width=1)
            
            master.create_line((taX + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (taY + ddy*(r1/(r1+r2)))*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="black", width=1)
            master.create_line((tbX + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (tbY + dy2*(r1/(r1+r2)))*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="black", width=1)

            master.create_polygon((xc1 + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + ddy*(r1/(r1+r2)))*k, xc1*k + self.xCentral, self.yCentral - yc1*k, (xc1 + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + dy2*(r1/(r1+r2)))*k, xmid*k + self.xCentral, self.yCentral - ymid*k, outline='gray', fill='blue', width=2)
            master.create_polygon((taX + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (taY + ddy*(r1/(r1+r2)))*k, xc2*k + self.xCentral, self.yCentral - yc2*k, (tbX + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (tbY + dy2*(r1/(r1+r2)))*k, xmid*k + self.xCentral, self.yCentral - ymid*k, outline='gray', fill='green', width=2)
            s = "Задание: На плоскости задано 2 множества точек. Найти пару окружностей, каждая из которых \nпроходит хотя бы через 3 различные точки одного и того же множества, \nтаких, что разность площадей четырехугольников, образованных \nцентрами окружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных, максимальна."
            master.create_text(5, 525, text = s, fill="black", anchor=SW, font=("Purisa", "12"))
            s0 = '''Ответ: Окружность 1 образована точками (''' + str(self.dotsResult1[0][0]) + "; " + str(self.dotsResult1[0][1]) + "),  (" + str(self.dotsResult1[1][0]) + "; " + str(self.dotsResult1[1][1]) + "),  (" + str(self.dotsResult1[2][0]) + "; " + str(self.dotsResult1[2][1]) + ")"
            master.create_text(5, 540, text = s0, fill="black", anchor=SW, font=("Helvectica", "12"))
            s1 = '''Окружность 2 образована точками (''' + str(self.dotsResult2[0][0]) + "; " + str(self.dotsResult2[0][1]) + "),  (" + str(self.dotsResult2[1][0]) + "; " + str(self.dotsResult2[1][1]) + "),  (" + str(self.dotsResult2[2][0]) + "; " + str(self.dotsResult2[2][1]) + ")"
            master.create_text(5, 555, text = s1, fill="black", anchor=SW, font=("Helvectica", "12"))
            s2 = '''Максимальная разность площадей четырехугольников, образованных центрами \nокружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных = ''' + str(self.sum)
            master.create_text(5, 600, text = s2, fill="black", anchor=SW, font=("Helvectica", "12"))
        except IndexError:
            s = "Задание: На плоскости задано 2 множества точек. Найти пару окружностей, каждая из которых \nпроходит хотя бы через 3 различные точки одного и того же множества, \nтаких, что разность площадей четырехугольников, образованных \n центрами окружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных, максимальна."
            master.create_text(5, 560, text = s, fill="black", anchor=SW, font=("Purisa", "12"))
            s2 = '''Ответ: Не удалось найти соответствующие всем условиям задачи окружности. \nПожалуйста, добавьте точки.'''
            master.create_text(5, 590, text = s2, fill="black", anchor=SW, font=("Helvectica", "12"))

    def drawPicture(self, master):
        try:
            x1 = self.dotsResult1[0][0]
            x2 = self.dotsResult1[1][0]
            x3 = self.dotsResult1[2][0]
            y1 = self.dotsResult1[0][1]
            y2 = self.dotsResult1[1][1]
            y3 = self.dotsResult1[2][1]
            
            A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
            B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
            C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
            D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
            xc1 = -(B/(2*A))
            yc1 = -(C/(2*A))
            r1 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
            
            x1 = self.dotsResult2[0][0]
            x2 = self.dotsResult2[1][0]
            x3 = self.dotsResult2[2][0]
            y1 = self.dotsResult2[0][1]
            y2 = self.dotsResult2[1][1]
            y3 = self.dotsResult2[2][1]
            
            A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
            B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
            C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
            D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
            xc2 = -(B/(2*A))
            yc2 = -(C/(2*A))
            r2 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
            
            self.checkForScale(xc1, xc2, yc1, yc2, r1, r2)
            self.drawDot(self.master)

            dx = xc2 - xc1
            dy = yc2 - yc1
            d = sqrt(dx*dx + dy*dy)
            between = r1 / (r1 + r2)
            d1 = d * between
            d2 = d - d1
            sq = fabs(d1*r1 - d2*r2)
            
            k = self.k
            
            left_x = xc1 - r1
            left_y = yc1 - r1
            right_x = xc1 + r1
            right_y = yc1 + r1
            x1 = left_x*k + self.xCentral
            y1 = self.yCentral - left_y*k
            x2 = right_x*k + self.xCentral
            y2 = self.yCentral - right_y*k
            master.create_oval(x1,y1,x2,y2, width=1, outline='blue')

            left_x2 = xc2 - r2
            left_y2 = yc2 - r2
            right_x2 = xc2 + r2
            right_y2 = yc2 + r2
            x3 = left_x2*k + self.xCentral
            y3 = self.yCentral - left_y2*k
            x4 = right_x2*k + self.xCentral
            y4 = self.yCentral - right_y2*k
            master.create_oval(x3,y3,x4,y4, width=1, outline='green')
            #master.create_oval((x1+d1)*k + self.xCentral + 2,self.yCentral - (yc1+d1)*k + 2,(x1+d1)*k + self.xCentral - 2,self.yCentral - (yc1+d1)*k - 2, width=10, outline='red')

            ko = r1/r2
            xmid = xc1 + (xc2-xc1)*ko
            ymid = yc1 + (yc2-yc1)*ko
            
            d = sqrt((xc2-xc1)**2 + (yc2-yc1)**2)

            master.create_line(xc1*k + self.xCentral, self.yCentral - yc1*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="red", width=1)

            r3 = r2 + r1
            dx = xc2 - xc1
            dy = yc2 - yc1
            dd = sqrt(dx * dx + dy * dy)
            a = asin(r3 / dd)
            b = atan2(dy, dx)
            
            t = b - a
            taX = xc2 + r3 * sin(t)
            taY = yc2 + r3 * -cos(t)
            
            t = b + a
            tbX = xc2 + r3 * -sin(t)
            tbY = yc2 + r3 * cos(t)
            
            ddx = xc2 - taX
            ddy = yc2 - taY
            d = sqrt(dx**2 + dy**2)
            
            dx2 = xc2 - tbX
            dy2 = yc2 - tbY
            d2 = sqrt(dx2**2 + dy2**2)
            
            master.create_line((xc1 + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + ddy*(r1/(r1+r2)))*k, (taX + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (taY + ddy*(r1/(r1+r2)))*k, fill="black", width=1)
            master.create_line((xc1 + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + dy2*(r1/(r1+r2)))*k, (tbX + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (tbY + dy2*(r1/(r1+r2)))*k, fill="black", width=1)
            
            master.create_line((xc1 + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + ddy*(r1/(r1+r2)))*k, xc1*k + self.xCentral, self.yCentral - yc1*k, fill="black", width=1)
            master.create_line((xc1 + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (yc1 + dy2*(r1/(r1+r2)))*k, xc1*k + self.xCentral, self.yCentral - yc1*k, fill="black", width=1)
            
            master.create_line((taX + ddx*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (taY + ddy*(r1/(r1+r2)))*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="black", width=1)
            master.create_line((tbX + dx2*(r1/(r1+r2)))*k + self.xCentral, self.yCentral - (tbY + dy2*(r1/(r1+r2)))*k, xc2*k + self.xCentral, self.yCentral - yc2*k, fill="black", width=1)

            s = "Задание: На плоскости задано 2 множества точек. Найти пару окружностей, каждая из которых \nпроходит хотя бы через 3 различные точки одного и того же множества, \nтаких, что разность площадей четырехугольников, образованных \nцентрами окружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных, максимальна."
            master.create_text(5, 525, text = s, fill="black", anchor=SW, font=("Purisa", "12"))
            s0 = '''Ответ: Окружность 1 образована точками (''' + str(self.dotsResult1[0][0]) + "; " + str(self.dotsResult1[0][1]) + "),  (" + str(self.dotsResult1[1][0]) + "; " + str(self.dotsResult1[1][1]) + "),  (" + str(self.dotsResult1[2][0]) + "; " + str(self.dotsResult1[2][1]) + ")"
            master.create_text(5, 540, text = s0, fill="black", anchor=SW, font=("Helvectica", "12"))
            s1 = '''Окружность 2 образована точками (''' + str(self.dotsResult2[0][0]) + "; " + str(self.dotsResult2[0][1]) + "),  (" + str(self.dotsResult2[1][0]) + "; " + str(self.dotsResult2[1][1]) + "),  (" + str(self.dotsResult2[2][0]) + "; " + str(self.dotsResult2[2][1]) + ")"
            master.create_text(5, 555, text = s1, fill="black", anchor=SW, font=("Helvectica", "12"))
            s2 = '''Максимальная разность площадей четырехугольников, образованных центрами \nокружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных = ''' + str(self.sum)
            master.create_text(5, 600, text = s2, fill="black", anchor=SW, font=("Helvectica", "12"))
        except IndexError:
            s = "Задание: На плоскости задано 2 множества точек. Найти пару окружностей, каждая из которых \nпроходит хотя бы через 3 различные точки одного и того же множества, \nтаких, что разность площадей четырехугольников, образованных \n центрами окружностей, точками касания внутренних общих касательных и \nточкой пересечения касательных, максимальна."
            master.create_text(5, 560, text = s, fill="black", anchor=SW, font=("Purisa", "12"))
            s2 = '''Ответ: Не удалось найти соответствующие всем условиям задачи окружности. \nПожалуйста, добавьте точки.'''
            master.create_text(5, 590, text = s2, fill="black", anchor=SW, font=("Helvectica", "12"))

    def checkForAll(self, i1, i2, i3, j1, j2, j3):
        
        x1 = self.dots1[i1][0]
        x2 = self.dots1[i2][0]
        x3 = self.dots1[i3][0]
        y1 = self.dots1[i1][1]
        y2 = self.dots1[i2][1]
        y3 = self.dots1[i3][1]
        
        A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
        B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
        C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
        D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
        xc1 = -(B/(2*A))
        yc1 = -(C/(2*A))
        r1 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
        
        x1 = self.dots2[j1][0]
        x2 = self.dots2[j2][0]
        x3 = self.dots2[j3][0]
        y1 = self.dots2[j1][1]
        y2 = self.dots2[j2][1]
        y3 = self.dots2[j3][1]
        
        A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
        B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
        C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
        D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
        xc2 = -(B/(2*A))
        yc2 = -(C/(2*A))
        r2 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
        
        
        r3 = r2 + r1
        dx = xc2 - xc1
        dy = yc2 - yc1
        dd = sqrt(dx * dx + dy * dy)
        a = asin(r3 / dd)
        b = atan2(dy, dx)
        
        t = b - a
        taX = xc2 + r3 * sin(t)
        taY = yc2 + r3 * -cos(t)
        
        t = b + a
        tbX = xc2 + r3 * -sin(t)
        tbY = yc2 + r3 * cos(t)
        
        ddx1 = taX - xc1
        ddy1 = taY - yc1
        
        dd1 = sqrt(ddx1**2 + ddy1**2)
        k1 = r1/(r1+r2)
        k2 = r2/(r1+r2)
    
        sq = fabs(dd1*k1 * r1 - dd1*k2 * r2)
        return sq

    def checkCircles(self, i1, i2, i3, j1, j2, j3):
        x1 = self.dots1[i1][0]
        x2 = self.dots1[i2][0]
        x3 = self.dots1[i3][0]
        y1 = self.dots1[i1][1]
        y2 = self.dots1[i2][1]
        y3 = self.dots1[i3][1]
        
        A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
        B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
        C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
        D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
        if (2*A == 0):
            return 0
        xc1 = -(B/(2*A))
        yc1 = -(C/(2*A))
        if (4*A**2 == 0):
            return 0
        r1 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
        
        x1 = self.dots2[j1][0]
        x2 = self.dots2[j2][0]
        x3 = self.dots2[j3][0]
        y1 = self.dots2[j1][1]
        y2 = self.dots2[j2][1]
        y3 = self.dots2[j3][1]
        
        A = x1*(y2-y3)-y1*(x2-x3) + x2*y3 - x3*y2
        B = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1)
        C = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2)
        D = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2)
        if (2*A == 0):
            return 0
        xc2 = -(B/(2*A))
        yc2 = -(C/(2*A))
        if (4*A**2 == 0):
            return 0
        r2 = sqrt((B**2 + C**2 - 4*A*D)/(4*A**2))
    
        d = sqrt((xc1-xc2)**2 + (yc1-yc2)**2)
        if d > r1+r2:
            return 1
        else:
            return 0

    def leng(self, x1, y1, x2, y2):
        return sqrt((y1 - y2)*(y1 - y2) + (x1 - x2)*(x1 - x2))

    def checkTriangle(self, x1, y1, x2, y2, x3, y3):
        ab = self.leng(x1, y1, x2, y2)
        bc = self.leng(x2, y2, x3, y3)
        ac = self.leng(x1, y1, x3, y3)
        return (((ab + bc - ac) > 0) and ((ab + ac - bc) > 0) and ((bc + ac - ab) > 0))

#print(str(self.k))

def main():
    root = Tk()
    
    app = Application(root)
    dot = Dot(app.canv)
    app.canv.bind("<Motion>", app.getMousePos)
    app.setDot(dot)
    app.setCommand(app.buttonDot, app.getCommandDot)
    app.setCommand(app.buttonDel, app.getCommandDel)
    app.setCommand(app.buttonCount, app.getCommandCount)
    app.setCommand(app.buttonPrint, app.getCommandPrint)
    app.setCommand(app.buttonReset, dot.reset)
    app.setCommand(app.buttonChange, app.getCommandChange)
    app.setCommand(app.buttonFill, app.getCommandFill)
    root.mainloop()

if __name__ == "__main__":
    main()

