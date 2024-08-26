import tkinter as tk

def draw_pikachu(canvas):
    # Body
    canvas.create_oval(50, 100, 250, 300, fill='yellow', outline='black')
    
    # Ears
    canvas.create_polygon(70, 50, 90, 150, 110, 50, fill='yellow', outline='black')
    canvas.create_polygon(190, 50, 210, 150, 230, 50, fill='yellow', outline='black')
    canvas.create_polygon(75, 50, 85, 75, 100, 50, fill='black', outline='black')
    canvas.create_polygon(195, 50, 205, 75, 220, 50, fill='black', outline='black')
    
    # Eyes
    canvas.create_oval(110, 150, 130, 170, fill='white', outline='black')
    canvas.create_oval(170, 150, 190, 170, fill='white', outline='black')
    canvas.create_oval(120, 160, 125, 165, fill='black')
    canvas.create_oval(180, 160, 185, 165, fill='black')
    
    # Cheeks
    canvas.create_oval(85, 200, 105, 220, fill='red', outline='black')
    canvas.create_oval(195, 200, 215, 220, fill='red', outline='black')
    
    # Nose
    canvas.create_oval(145, 180, 155, 190, fill='black')
    
    # Mouth
    canvas.create_arc(130, 200, 170, 220, start=0, extent=-180, fill='black')
    
    # Arms
    canvas.create_oval(30, 220, 70, 260, fill='yellow', outline='black')
    canvas.create_oval(230, 220, 270, 260, fill='yellow', outline='black')
    
    # Legs
    canvas.create_oval(110, 280, 140, 320, fill='yellow', outline='black')
    canvas.create_oval(160, 280, 190, 320, fill='yellow', outline='black')
    
    # Tail
    canvas.create_polygon(250, 100, 300, 80, 270, 130, 310, 150, 270, 170, 250, 120, fill='yellow', outline='black')
    canvas.create_polygon(300, 80, 310, 90, 270, 130, fill='black', outline='black')

def main():
    window = tk.Tk()
    window.title("Pikachu Drawing")

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    draw_pikachu(canvas)

    window.mainloop()

if __name__ == "__main__":
    main()
