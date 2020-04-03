from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.geometry("350x350")
root.title("Rock Paper Scissors")
root.iconbitmap('images/rock.ico')

computer_options = [1, 2, 3]
player_choice = IntVar()
computer_choice = random.choice(computer_options)


#This function controls the instructions button on the home page
def myClick():
    #extremely makeshift way of getting my text to fit on screen without covering my buttons.
    myLabel = Message(root, text="                                                       Click on rock, paper, or scissors, then click 'Submit!'. Paper beats rock, rock beats scissors, and scissors beats paper. The computer will choose an option and so will you. Good luck!")
    instructionsButton['state'] = DISABLED
    myLabel.pack()

#This function controls the start game button on the home page
def startGame():
    #These are all set-up instructions, placing the new window, adjusting size, icon, and title.
    global game_img
    global close_game
    global top
    global computer_options
    global computer_choice
    global player_choice
    top = Toplevel()
    top.geometry("220x150")
    top.title("Rock Paper Scissors")
    top.iconbitmap('images/rock.ico')
    #Sets the computer_choices as a list of three options
    computer_options = [1, 2, 3]
    #The player's choice is empty, since it will be filled by a button selection
    player_choice = IntVar()
    # the computer_choice selects a random option from the list computer_options above.
    computer_choice = random.choice(computer_options)

    #These buttons are tied to the player_choice variable, and have each have a different value.
    #When one button is clicked, it stores that variable in player_choice as an integer
    Radiobutton(top, text="Rock", variable=player_choice, value=1).grid(row=1, column=1)
    Radiobutton(top, text="Paper", variable=player_choice, value=2).grid(row=1, column=2)
    Radiobutton(top, text="Scissors", variable=player_choice, value=3).grid(row=1, column=3)

    #These three buttons call the solve function, destroy just the current window, and destroy the program, respectively.
    submit = Button(top, text="Submit!", command=lambda: solve())
    submit.grid(row=2, column=1)

    menu = Button(top, text="Menu", command=top.destroy)
    menu.grid(row=2, column=2)

    close = Button(top, text="Close", command=root.destroy)
    close.grid(row=2, column=3)

    #Each message matches up with a single outcome. The messages are created here,
    #then put on screen when the player makes his/her choice.
    rt = Message(top, text="The computer also chose rock, boring.")
    rl = Message(top, text="The computer chose paper, get wrecked scrub!")
    rw = Message(top, text="The computer chose scissors, you win!")
    pw = Message(top, text="The computer chose rock, you win!")
    pt = Message(top, text="The computer also chose paper, how lame.")
    pl = Message(top, text="The computer chose scissors, you got mashed!")
    sl = Message(top, text="The computer chose rock, stop wasting your time!")
    sw = Message(top, text="The computer chose paper, you win!")
    st = Message(top, text="The computer also chose scissors, dumb.")
    ll = Message(top, text="You lose. Read the instructions next time, doo doo head.")

    #This function is called by the submit button.
    #I don't fully understand how player_choice.get works with player_choice,
    #but basically, player_choice is being set to the current value set by the player.
    #The logic then decides what message to output, referencing the above messages,
    #and using the .grid attribute to put only the appropriate one on screen.
    def solve():
        global player_choice
        player_choice.get()
        player_choice = player_choice.get()
        submit['state'] = DISABLED
        if player_choice == 1:
            if computer_choice == 1:
                rt.grid(row=3, column=2)
            elif computer_choice == 2:
                print("")
                rl.grid(row=3, column=2)
            elif computer_choice == 3:
                print("")
                rw.grid(row=3, column=2)
        elif player_choice == 2:
            if computer_choice == 1:
                pw.grid(row=3, column=2)
            elif computer_choice == 2:
                pt.grid(row=3, column=2)
            elif computer_choice == 3:
                pl.grid(row=3, column=2)
        elif player_choice == 3:
            if computer_choice == 1:
                sl.grid(row=3, column=2)
            elif computer_choice == 2:
                sw.grid(row=3, column=2)
            elif computer_choice == 3:
                st.grid(row=3, column=2)
        else: ll.grid(row=3, column=2)

#This is the image that appears above the buttons.
game_img = ImageTk.PhotoImage(Image.open("images/rock_paper_scissors.png"))

#This label puts the image on the screen.
image_label = Label(root, image=game_img)
image_label.pack()

#Physical Button that starts the game. Linked to myClick
instructionsButton = Button(root, text="Instructions", command=myClick)
instructionsButton.pack()

#Physical Button that starts the game. Linked to startGame
startButton = Button(root, text="Play Game", command=startGame)
startButton.pack()

mainloop()