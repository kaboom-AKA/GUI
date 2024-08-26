import tkinter as tk
from tkinter import *

def xx():
    window =tk.Tk()

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    def draw(event):
        x = event.x
        y = event.y
        canvas.create_oval((x - brush_size / 2, y - brush_size / 2 ,x + brush_size / 2,y + brush_size / 2), fill = "black")
       
    brush_size = 10
    window.bind('<KeyPress>',lambda event:print(event))
    window.bind('<Button-1>',lambda event:print("Key pressed :" + event.char))
    window.bind('<Alt-Motion>', draw)
    window.mainloop()

def main():

    xx()


if __name__ == '__main__':
    main()