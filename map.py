import tkinter as tk
from tkinter import *


#window
window= tk.Tk()
window.geometry("600x600")
window.title("google map viewer")
window.resizable(False,False)

gmap_widget =TkinterMapView(window,width=600,height=400)
gmap_widget.pack(fill='both')
gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
gmap_widget.set_address("sinagpore",market=True)

window.mainloop()
