import random
from tkinter import *

p = 0
score = 0

def Rock():
    global p, score
    p = 1
    listbox.insert(END, f"{len(listbox.get(0, END)) // 2+1}]Your choice: Rock")

    c = random.randint(1, 3)
    if c == 1:
        listbox.insert(END, "Computer's choice: Rock")
        listbox.insert(END, "TIE")
    elif c == 3:
        listbox.insert(END, "Computer's choice: Scissor")
        listbox.insert(END, "You win")
        score += 1
    elif c == 2:
        listbox.insert(END, "Computer's choice: Paper")
        listbox.insert(END, "Computer wins")
    else:
        listbox.insert(END, "INVALID NUMBER")

    entry2.delete(0, END)
    entry2.insert(0, f"{score} out of {len(listbox.get(0, END)) // 2}")

def Paper():
    global p, score
    p = 2
    listbox.insert(END, f"{len(listbox.get(0, END)) // 2+1}]Your choice: Paper")

    c = random.randint(1, 3)
    if c == 1:
        listbox.insert(END, "Computer's choice: Rock")
        listbox.insert(END, "You win")
        score += 1
    elif c == 3:
        listbox.insert(END, "Computer's choice: Scissor")
        listbox.insert(END, "Computer wins")
    elif c == 2:
        listbox.insert(END, "Computer's choice: Paper")
        listbox.insert(END, "TIE")
    else:
        listbox.insert(END, "INVALID NUMBER")

    entry2.delete(0, END)
    entry2.insert(0, f"{score} out of {len(listbox.get(0, END)) // 2}")

def Scissor():
    global p, score
    p = 3
    listbox.insert(END, f"{len(listbox.get(0, END)) // 2+1}]Your choice: Scissor")

    c = random.randint(1, 3)
    if c == 1:
        listbox.insert(END, "Computer's choice: Rock")
        listbox.insert(END, "Computer wins")
    elif c == 3:
        listbox.insert(END, "Computer's choice: Scissor")
        listbox.insert(END, "TIE")
    elif c == 2:
        listbox.insert(END,"Computer's choice: Paper")
        listbox.insert(END, "You win")
        score += 1
    else:
        listbox.insert(END, "INVALID NUMBER")

    entry2.delete(0, END)
    entry2.insert(0, f"{score} out of {len(listbox.get(0, END)) // 2}")

def playagain():
    global score
    score = 0
    listbox.delete(0, END)
    entry2.delete(0, END)

window = Tk()
window.geometry("800x800")
window.config(background="light blue")

label = Label(window, text="ROCK PAPER SCISSORS", font="bold 20")
label.place(x=250, y=100)

label1 = Label(window, text="Choose any one button:")
label1.place(x=100, y=200)

rock = Button(window, text="ROCK", command=Rock)
rock.place(x=100, y=300)

paper = Button(window, text="PAPER", command=Paper)
paper.place(x=100, y=400)

scissor = Button(window, text="SCISSOR", command=Scissor)
scissor.place(x=100, y=500)


scrollbar = Scrollbar(window)
scrollbar.place(x=700, y=400, height=200)


listbox = Listbox(window, yscrollcommand=scrollbar.set)
listbox.place(x=300, y=400, width=400)


scrollbar.config(command=listbox.yview)

score_label = Label(window, text="Your score:")
score_label.place(x=100, y=600)

entry2 = Entry(window)
entry2.place(x=400, y=600)

play_again_button = Button(window, text="PLAY AGAIN", command=playagain)
play_again_button.place(x=100, y=700)

window.mainloop()
