from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.geometry("250x200")
root.title("Rock Paper Scissors")
root.iconbitmap('images/rock.ico')

computer_options = [1, 2, 3]
player_choice = IntVar()
computer_choice = random.choice(computer_options)

Radiobutton(root, text="Rock", variable=player_choice, value=1).pack()
Radiobutton(root, text="Paper", variable=player_choice, value=2).pack()
Radiobutton(root, text="Scissors", variable=player_choice, value=3).pack()

#myButton = Button(root, text="Submit!", command=lambda: clicked(player_choice.get()))
#myButton.pack()

myButton = Button(root, text="Submit!", command=lambda: solve())
myButton.pack()


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

def solve():
    if player_choice == 1:
        if computer_choice == 1:
            print("The computer also chose rock, boring.")
        elif computer_choice == 2:
            print("The computer chose paper, get wrecked scrub!")
        elif computer_choice == 3:
            print("The computer chose scissors, you win!")
    elif player_choice == 2:
        if computer_choice == 1:
            print("The computer chose rock, you win!.")
        elif computer_choice == 2:
            print("The computer also chose paper, how lame.")
        elif computer_choice == 3:
            print("The computer chose scissors, you got mashed!")
    elif player_choice == 3:
        if computer_choice == 1:
            print("The computer chose rock, stop wasting your time!")
        elif computer_choice == 2:
            print("The computer chose paper, you win!")
        elif computer_choice == 3:
            print("The computer also chose scissors, dumb.")
    else: print("The game was confused, try again.")

mainloop()