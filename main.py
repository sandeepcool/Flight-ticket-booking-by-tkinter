from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("600x600")
Label(root, text="Which country you want to travel in?", font = "lucidia 15 bold").pack()
country = ["India", "Australia", "UK", "USA", "Canada", "Newzland"]
var = StringVar()
new_var = var.set("nonewhere")
def travel():
  tmsg.showinfo("Let's travel", f"So, we are booking your flight to {var.get()}\nWe wish you a happy journey. Thanks for booking with us" )
for x in range(6):
  Radiobutton(root,text=country[x], variable=var, value=country[x]).pack()
Button(root, text="Let's travel", command=travel).pack()
root.mainloop()