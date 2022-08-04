from tkinter import *

window = Tk()
window.geometry("800x600")

comments=1

comment = Text(window,
width=60, height=1)
comment.grid(row=0, column=0)

def clear():
    global comments
    comments=comments+1
    comment.delete(1.0, END)
    print(comments)

def post():
    global comments
    mylabel = Label(window, text='',
    font=('arial',10),
    relief=RAISED,
    bd=10)
    mylabel.config(text=comment.get(1.0, END))
    mylabel.grid(row=comments*10, column=0)
    clear()

postbutton = Button(window, text="post")
postbutton.config(command=post)
postbutton.grid(row=10, column=10)



window.mainloop()