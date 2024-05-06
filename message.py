from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Hello user")
root.iconbitmap("images\instrument_string_bass_guitar_electric_rock_music_icon_262845.ico")

root.filename=filedialog.askopenfilename(initialdir="images/three.jpg", title="select A file", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*") ))


my_label=Label(root, text=root.filename)
my_label.pack()
root.mainloop()