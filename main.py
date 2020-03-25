from firstFrame import *
from secondFrame import main2
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

window = tk.ThemedTk()
window.get_themes()
window.set_theme("equilux")

width_value = window.winfo_screenwidth()
height_value = window.winfo_screenwidth()

window.configure(background="gray27")
window.geometry("%dx%d+0+0" % (width_value, height_value))

f1 = ttk.Frame(window)
main(f1)
f2 = ttk.Frame(window, height=666, width=1200)
main2(f2)
f2.pack_propagate(False)


def swap(frame):
    frame.tkraise()


for frameS in (f1, f2):
    frameS.grid(row=0, column=0)

pda1 = ttk.Button(f1, text='To Stats & Leagues manager', command=lambda: swap(f2))
pda1.pack(side=RIGHT)

pda2 = ttk.Button(f2, text='       To scoreboard      ', command=lambda: swap(f1))
pda2.pack(side=LEFT)

f1.tkraise()
window.mainloop()
