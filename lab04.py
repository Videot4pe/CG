# -*- coding: utf-8 -*-
from Tkinter import *
from math import *
пimport numpy as np
import time
import matplotlib.pyplot as plt
import numpy

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

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
        self.buttonColor = Button(self.frame1, text="Цвет")
        self.buttonColorBackground   = Button(self.frame1, text="Цвет фона")
        #self.buttonPrintLine  = Button(self.frame1, text="Нарисовать линию")
        self.buttonPrintCircle  = Button(self.frame1, text="Нарисовать круг")
        self.buttonPrintCircleSpectre  = Button(self.frame1, text="Спектр кругов")
        self.buttonPrintEllipse  = Button(self.frame1, text="Нарисовать эллипс")
        self.buttonPrintEllipseSpectre  = Button(self.frame1, text="Спектр эллипсов")
        self.buttonReset  = Button(self.frame1, text="Очистить")
        self.buttonCompare  = Button(self.frame1, text="Сравнить")
        #self.consoleXY     = Entry(self.frame1, font="Arial 30", text="Xn Yn")
        self.consoleI     = Entry(self.frame1, font="Arial 30", text="Xc Yc")
        self.consoleR     = Entry(self.frame1, font="Arial 30", text="Radius")
        #self.consoleA     = Entry(self.frame1, font="Arial 30", text="Angle")
        
        self.label1 = Label(self.frame1, font="Arial 10", text="Начало: ")
        #self.label2 = Label(self.frame1, font="Arial 10", text="Конец: ")
        self.label3 = Label(self.frame1, font="Arial 10", text="Радиус: ")
        #self.label4 = Label(self.frame1, font="Arial 10", text="Угол: ")
        
        
        self.l = Listbox(self.frame1, width=50)
        self.l.insert(END,  *('алгоритм Брезенхема', 'алгоритм средней точки', 'каноническое уравнение', 'параметрическое уравнение'))
        for i in range(0, self.l.size()):
            if self.l.get(i)[0] == '-':
                self.l.itemconfig(i, foreground='gray', \
                                  selectforeground='gray', \
                                  selectbackground=self.l.itemcget(i, 'background'))
        self.l.grid(row = 8, column = 1)
        self.l.bind("<<ListboxSelect>>", self.get)
        
        self.frame.grid(row = 0, column = 0)
        self.frame1.grid(row=0, column=1)
        self.canv.grid(row=0, column=0)
        
        self.buttonColor.grid(row = 5, column = 0)
        self.buttonColorBackground.grid(row=5, column=1)
        self.buttonCompare.grid(row=4, column=1)
        self.buttonReset.grid(row=4, column=0)
        #self.buttonPrintLine.grid(row=2, column=0)
        self.buttonPrintCircle.grid(row=2, column=0)
        self.buttonPrintCircleSpectre.grid(row=2, column=1)
        self.buttonPrintEllipse.grid(row=3, column=0)
        self.buttonPrintEllipseSpectre.grid(row=3, column=1)
        
        #self.consoleXY.grid(row=0, column=1)
        self.consoleI.grid(row=0, column=1)
        self.consoleR.grid(row=1, column=1)
        #self.consoleA.grid(row=4, column=1)
        
        self.label1.grid(row=0, column=0)
        #self.label2.grid(row=1, column=0)
    self.label3.grid(row=1, column=0)
    #self.label4.grid(row=4, column=0)

def get(self, event):
    self.menu = event.widget.curselection()[0]
    
    def setDot(self, Dot):
        self.Dot = Dot
    
    def getColor(self):
        color = askcolor()
        self.color = color
    #print(color)
    
    def getColorBackground(self):
        color = askcolor()
        self.Dot.changeColor(color[1])
    
    def setCommand(self, button, command):
        button["command"] = command
    
    def printCircle(self):
        dataI = self.consoleI.get()
        dataI = dataI.split()
        dataR = self.consoleR.get()
        dataR = dataR.split()
        self.Dot.dr(float(dataI[0]), float(dataI[1]), float(dataR[0]), self.color, self.menu)
    
    def printCircleSpectre(self):
        dataR = self.consoleR.get()
        dataR = dataR.split()
        self.Dot.drs(float(dataR[0]), self.color, self.menu)
    
    def printEllipse(self):
        dataI = self.consoleI.get()
        dataI = dataI.split()
        dataR = self.consoleR.get()
        dataR = dataR.split()
        self.Dot.dre(float(dataI[0]), float(dataI[1]), float(dataR[0]), float(dataR[1]), self.color, self.menu)
    
    def printEllipseSpectre(self):
        dataR = self.consoleR.get()
        dataR = dataR.split()
        self.Dot.dres(float(dataR[0]), float(dataR[1]), self.color, self.menu)
    
    def compare(self):
        self.Dot.compare()



class Dot():
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(width=600, height=600)
        self.master.create_image((600/2, 600/2), image=self.img, state="normal")
        
        self.xCentral = 300
        self.yCentral = 300
        self.color = ['#000000']
    
    def changeColor(self, color):
        for y in range(self.img.height()):
            for x in range(self.img.width()):
                self.img.put(color, (x, y))

    def circle_canon(self, cx, cy, r, color):
        r = int(r)
        for x in range(0, r + 1, 1):
            y = round(sqrt(r ** 2 - x ** 2))
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            
            for y in range(0, r + 1, 1):
                x = round(sqrt(r ** 2 - y ** 2))
                
                self.img.put(color, (int(cx+x), int(cy+y)))
                self.img.put(color, (int(cx+x), int(cy-y)))
                self.img.put(color, (int(cx-x), int(cy+y)))
                self.img.put(color, (int(cx-x), int(cy-y)))


    def circle_param(self, cx, cy, r, color):
        l = round(pi * r / 2)  # длина четврети окружности
        for i in range(0, l + 1, 1):
            x = round(r * cos(i / r))
            y = round(r * sin(i / r))
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
    
    
    def circle_brez(self, cx, cy, r, color):
        x = 0   # задание начальных значений
        y = r
        d = 2 - 2 * r   # значение D(x,y)  при (0,R)
        while y >= 0:
            # высвечивание текущего пиксела
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            
            if d < 0:  # пиксель лежит внутри окружности
                buf = 2 * d + 2 * y - 1
                x += 1
                
                if buf <= 0:  # горизонтальный шаг
                    d = d + 2 * x + 1
                else:  # диагональный шаг
                    y -= 1
                    d = d + 2 * x - 2 * y + 2
                
                continue
            
            if d > 0:  # пиксель лежит вне окружности
                buf = 2 * d - 2 * x - 1
                y -= 1
                
                if buf > 0:  # вертикальный шаг
                    d = d - 2 * y + 1
                else:  # диагональный шаг
                    x += 1
                    d = d + 2 * x - 2 * y + 2
                
                continue
            
            if d == 0.0:  # пиксель лежит на окружности
                x += 1   # диагональный шаг
                y -= 1
                d = d + 2 * x - 2 * y + 2


    def circle_middle(self, cx, cy, r, color):
        x = 0  # начальные значения
        y = r
        p = 5 / 4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2
        while True:
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            self.img.put(color, (int(cx+x), int(cy+y)))
            
            self.img.put(color, (int(cx - y), int(cy + x)))
            self.img.put(color, (int(cx + y), int(cy - x)))
            self.img.put(color, (int(cx - y), int(cy - x)))
            self.img.put(color, (int(cx + y), int(cy + x)))
            
            x += 1
            
            if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
                p += 2 * x + 1
            else:   # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
                p += 2 * x - 2 * y + 5
                y -= 1
            
            if x > y:
                break


    def ellipse_canon(self, cx, cy, a, b, color):
        a = int(a)
        b = int(b)
        for x in range(0, a + 1, 1):
            y = round(b * sqrt(1.0 - x ** 2 / a / a))
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            
            for y in range(0, b + 1, 1):
                x = round(a * sqrt(1.0 - y ** 2 / b / b))
                self.img.put(color, (int(cx+x), int(cy+y)))
                self.img.put(color, (int(cx+x), int(cy-y)))
                self.img.put(color, (int(cx-x), int(cy+y)))
                self.img.put(color, (int(cx-x), int(cy-y)))




    def ellipse_param(self, cx, cy, a, b, color):
        m = max(a, b)
        l = round(pi * m / 2)
        for i in range(0, l + 1, 1):
            x = round(a * cos(i / m))
            y = round(b * sin(i / m))
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))


    def ellipse_brez(self, cx, cy, a, b, color):
        x = 0
        y = b
        a = a ** 2
        d = round(b * b / 2 - a * b * 2 + a / 2)
        b = b ** 2
        while y >= 0:
            self.img.put(color, (int(cx+x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            if d < 0:  # пиксель внутри
                buf = 2 * d + 2 * a * y - a
                x += 1
                if buf <= 0:  # гор. шаг
                    d = d + 2 * b * x + b
                else:  # диаг. шаг
                    y -= 1
                    d = d + 2 * b * x - 2 * a * y + a + b
                
                continue
            
            if d > 0:  # вне
                buf = 2 * d - 2 * b * x - b
                y -= 1
                
                if buf > 0:  # верт. шаг
                    d = d - 2 * y * a + a
                else:  # диаг. шаг
                    x += 1
                    d = d + 2 * x * b - 2 * y * a + a + b
                
                continue
            
            if d == 0.0:  # на окружности
                x += 1  # диаг. шаг
                y -= 1
                d = d + 2 * x * b - 2 * y * a + a + b


    def ellipse_middle(self, cx, cy, a, b, color):
        x = 0
        y = b
        p = b * b - a * a * b + 0.25 * a * a   # p при tg<1
        while 2 * (b ** 2) * x < 2 * a * a * y:  # tg < 1
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            self.img.put(color, (int(cx+x), int(cy+y)))
            
            x += 1
            
            if p < 0:  # с.т. внутри, ближе верх. пиксел, гор. шаг
                p += 2 * b * b * x + b * b
            else:   # вне, ближе диаг. пиксел, диаг. шаг
                y -= 1
                p += 2 * b * b * x - 2 * a * a * y + b * b
        
        p = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b #tg>1 в точке (х + 0.5, y - 1)
            
        while y >= 0:
            self.img.put(color, (int(cx-x), int(cy+y)))
            self.img.put(color, (int(cx+x), int(cy-y)))
            self.img.put(color, (int(cx-x), int(cy-y)))
            self.img.put(color, (int(cx+x), int(cy+y)))
            
            y -= 1
            
            if p > 0:
                p -= 2 * a * a * y + a * a
            else:
                x += 1
                p += 2 * b * b * x - 2 * a * a * y + a * a


    def drawEllipse(self, master, x, y, r1, r2, color, menu):
        if menu == 0:
            self.ellipse_brez(x, y, r1, r2, color)
            if menu == 1:
                self.ellipse_middle(x, y, r1, r2, color)
        if menu == 2:
            self.ellipse_canon(x, y, r1, r2, color)
            if menu == 3:
                self.ellipse_param(x, y, r1, r2, color)


    def dr(self, x1, y1, r, color, menu):
        self.drawCircle(self.master, x1, y1, r, color[1], menu)
        
    def drawEllipseSpectre(self, master, n1, n2, color, menu):
        x = 300
        y = 300
        for i in range (8):
            r1 = (n1/n2)*10*i+n1
            r2 = 10*i+n2
            
            if menu == 0:
                self.ellipse_brez(x, y, r1, r2, color)
            if menu == 1:
                self.ellipse_middle(x, y, r1, r2, color)
            if menu == 2:
                self.ellipse_canon(x, y, r1, r2, color)
            if menu == 3:
                self.ellipse_param(x, y, r1, r2, color)

    def dres(self, r1, r2, color, menu):
        self.drawEllipseSpectre(self.master, r1, r2, color[1], menu)
        
    def drawCircle(self, master, x, y, r, color, menu):
        if menu == 0:
            self.circle_brez(x, y, r, color)
        if menu == 1:
            self.circle_middle(x, y, r, color)
        if menu == 2:
            self.circle_canon(x, y, r, color)
        if menu == 3:
            self.circle_param(x, y, r, color)


    def dre(self, x1, y1, r1, r2, color, menu):
        self.drawEllipse(self.master, x1, y1, r1, r2, color[1], menu)
        
    def drawCircleSpectre(self, master, r1, color, menu):
        x = 300
        y = 300
        for i in range (10):
            r = 10*i+r1
            
            if menu == 0:
                self.circle_brez(x, y, r, color)
            if menu == 1:
                self.circle_middle(x, y, r, color)
            if menu == 2:
                self.circle_canon(x, y, r, color)
            if menu == 3:
                self.circle_param(x, y, r, color)

    def drs(self, r, color, menu):
        self.drawCircleSpectre(self.master, r, color[1], menu)
        
        
    def reset(self):
        self.master.delete("all")
        self.img = PhotoImage(width=600, height=600)
        self.master.create_image((600/2, 600/2), image=self.img, state="normal")
    
    def compare(self):
        print('Сравнение алгоритмов')
        x = 300
        y = 300
        Test1 = [[],[],[],[]]
        Test2 = [[],[],[],[]]
        color = '#000000'
        
        T = [0, 0, 0, 0]
        for i in range(4):
            Test1[i].append(T.copy())
            Test2[i].append(T.copy())
        
        R = [10, 50, 100, 150]
        Re = [20, 100, 200, 300]
        #for i in range(4):
        #   x_arr = Test[i]
        #  Test[i] = numpy.linspace(x_arr[0], x_arr[len(x_arr)-1], 10)
        #print(Test)
        C = ['алгоритм Брезенхема', 'алгоритм средней точки', 'каноническое уравнение', 'параметрическое уравнение']
        
        for i in range(4):
            r = R[i]
            t = time.clock()
            self.circle_brez(x, y, r, color)
            Test1[i][0] = time.clock() - t
            
            t = time.clock()
            self.circle_middle(x, y, r, color)
            Test1[i][1] = time.clock() - t
            
            t = time.clock()
            self.circle_canon(x, y, r, color)
            Test1[i][2] = time.clock() - t
            
            t = time.clock()
            self.circle_param(x, y, r, color)
            Test1[i][3] = time.clock() - t
        
        for i in range(4):
            r1 = Re[i]
            r2 = R[i]
            t = time.clock()
            self.ellipse_brez(x, y, r1, r2, color)
            Test2[i][0] = time.clock() - t
            
            t = time.clock()
            self.ellipse_middle(x, y, r1, r2, color)
            Test2[i][1] = time.clock() - t
            
            t = time.clock()
            self.ellipse_canon(x, y, r1, r2, color)
            Test2[i][2] = time.clock() - t
            
            t = time.clock()
            self.ellipse_param(x, y, r1, r2, color)
            Test2[i][3] = time.clock() - t
        
        plt.figure("Среднеквадратичное приближение")
        
        
        #plt.scatter(x_arr, y_arr, color='r', s=10, alpha=.5, label="Фактический результат")
        
        plt.grid(True)
        plt.xlabel(u'R')
        plt.ylabel(u'Time')
        plt.legend()
        
        
        for i in range(4):
            s = C[i] + ': ' + '{:.5f}'.format(T[i]) + ' сек.'
            plt.plot(R[i], Test1[i], label = C[i])
            
            print(s)
        
            plt.show()


def main():
    root = Tk()
    
    app = Application(root)
    dot = Dot(app.canv)
    app.setDot(dot)
    app.setCommand(app.buttonColor, app.getColor)
    app.setCommand(app.buttonColorBackground, app.getColorBackground)
    #app.setCommand(app.buttonPrintLine, app.printLine)
    app.setCommand(app.buttonPrintCircle, app.printCircle)
    app.setCommand(app.buttonPrintCircleSpectre, app.printCircleSpectre)
    app.setCommand(app.buttonPrintEllipse, app.printEllipse)
    app.setCommand(app.buttonPrintEllipseSpectre, app.printEllipseSpectre)
    app.setCommand(app.buttonReset, dot.reset)
    app.setCommand(app.buttonCompare, dot.compare)
    root.mainloop()

if __name__ == "__main__":
    main()

