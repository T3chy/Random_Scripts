import wordoftheday
from tkinter import *
words = wordoftheday.gettop3()
window = Tk()
window.title("The Top Three Words Used in Headlines!")
window.geometry('475x150')
first = Label(window, text="1st: " + words[0][0] + " with " + str(words[0][1]) + " uses", font=("Arial Bold",24))
second = Label(window, text="2nd: " + words[1][0] + " with " + str(words[1][1]) + " uses", font=("Arial Bold",24))
third = Label(window, text="3rd: " + words[2][0] + " with " + str(words[2][1]) + " uses", font=("Arial Bold",24))
first.grid(column=0,row=0)
second.grid(column=0,row=1)
third.grid(column=0,row=2)
window.attributes("-topmost", True)
window.mainloop()
