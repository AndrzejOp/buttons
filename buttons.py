from tkinter import *

count = 0
def click ():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file="Zrzut ekranu 2023-11-29 234243.png")

button = Button(window,
                text = "Increment",
                command= click,
                font = ("Comic Sans",30),
                fg = "green",
                bg = "black",
                activebackground= "black",
                activeforeground= "green",
                state= ACTIVE,
                image= photo,
                compound= BOTTOM)



button.pack()

window.mainloop()