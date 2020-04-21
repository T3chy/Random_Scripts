import wordoftheday
from tkinter import *
number_of_words = 10
words = wordoftheday.gettopx(number_of_words)
window = Tk()
window.title("The Top Three Words Used in Headlines!")
window.geometry('475x'+str(45*number_of_words + 10))
rankings = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
for i in range(number_of_words):
    ranked = Label(window, text=rankings[i] + ": " + words[i][0] + " with " + str(words[i][1]) + " uses", font=("Arial Bold",24))
    ranked.grid(column=0,row=i)
window.attributes("-topmost", True)
window.mainloop()
