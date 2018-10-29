import turtle
import Tkinter as tk
import ttk

class Fractal:
    def __init__(self, master):
        self.canvas = tk.Canvas(master=master, width=1024, height=640)
        self.canvas.grid(row=3, column=0, columnspan=16)

        self.t = turtle.RawTurtle(self.canvas)

        ttk.Label(master=master, text="Polygon:").grid(row=0, column=0)
        ttk.Label(master=master, text="Level:").grid(row=1, column=0)

        self.ePol = ttk.Entry(master=master)
        self.ePol.insert(0, "3")
        self.ePol.grid(row=0, column=1)
        self.eLevel = ttk.Entry(master=master)
        self.eLevel.insert(0, "3")
        self.eLevel.grid(row=1, column=1)

        b = ttk.Button(master=master, text="submit", command=  self.draw)
        b.grid(row=2, column=1)


    def koch(self, t, order, size, polygon):
        """
        Make turtle t draw a Koch fractal of 'order' and 'size'.
        Leave the turtle facing the same direction.
        """
        
        angle_sum = (polygon - 2) * 180
        angle = float(angle_sum) / float(polygon)    
        if order <= 0 or polygon < 2:                  # The base case is just a straight line
            t.forward(size)
        else:
            self.koch(t, order-1, float(size/3), polygon)   # go 1/n of the way
            t.left(angle)
            self.koch(t, order-1, float(size/3), polygon)
            for i in range(polygon-2):
                t.right(180.0 - angle)
                self.koch(t, order-1, float(size/3), polygon)
            t.left(angle)
            self.koch(t, order-1, float(size/3), polygon)

    def draw(self):
        self.t.reset()
        self.t.color("red")
        self.t.ht()
        self.t.speed(0)
        #self.t._delay(0)
        self.t.tracer(2, 0)
        self.t.clear()
        self.t.penup()
        self.t.goto(-400, -180)
        self.t.pendown()

        #self.koch(self.t, self.level, 800, self.pol)
        self.pol = self.ePol.get()
        self.level = self.eLevel.get()

        if(len(self.level)==0):
            level="0"
        if(len(self.pol)==0):
            pol="0"
        
        self.koch(self.t, int(self.level), 800, int(self.pol))
        self.t._update()


    def left_pressed(self, event):
        self.pol = self.ePol.get()
        self.ePol.delete(0, tk.END)
        self.ePol.insert(0, int(self.pol)-1)
        self.draw()
    
    def right_pressed(self, event):
        self.pol = self.ePol.get()
        self.ePol.delete(0, tk.END)
        self.ePol.insert(0, int(self.pol)+1)
        self.draw()

    def up_pressed(self, event):
        self.level = self.eLevel.get()
        self.eLevel.delete(0, tk.END)
        self.eLevel.insert(0, int(self.level)+1)
        self.draw()

    def down_pressed(self, event):
        self.level = self.eLevel.get()
        self.eLevel.delete(0, tk.END)
        self.eLevel.insert(0, int(self.level)-1)
        self.draw()


root = tk.Tk()
#wn = turtle.Screen()
root.title("Fractal Recursion")
root.geometry("1024x768")
root.configure(background='black')
myFractal = Fractal(root)
root.bind('<Left>', myFractal.left_pressed)
root.bind('<Right>', myFractal.right_pressed)
root.bind('<Up>', myFractal.up_pressed)
root.bind('<Down>', myFractal.down_pressed)

root.mainloop()