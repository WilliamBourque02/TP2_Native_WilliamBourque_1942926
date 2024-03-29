# Liste des Imports utilisés pour le projet 

from tkinter import *
from PIL import ImageTk, Image
from random import randint
import sys
import os

# CODE STARTS HERE 
# GRAPHICAL INTERFACE FOR START MENU SETTINGS

global rock1, paper1, scissor1, spock1, lizard1, rock2, paper2, scissor2, spock2, lizard2
window = Tk()
window.title("Travail Pratique 1 William Bourque")
window.config(bg='#3EDBF0')
window.geometry('1990x900')
welcome = Label(window, text="ROCK PAPER SCISSORS SPOCK LIZARD", bg='#3EDBF0', fg="black", font=("Arial Bold", 36))
welcome.grid(row=1, padx=500, pady=(250, 0))
player_name = Entry(window, width=27, borderwidth=9, bg="#FFA900",
                    justify='center', fg="black", font=("Arial Bold", 16))
player_name.grid(pady=20, ipady=15, padx=500)
player_name.insert(0, "PLAYER")


# COMMAND TO DESTROY WINDOW

def exit_game():
    window.destroy()



# COMMAND THAT SETS THE DIRECTIVES AND RESULTS OF WHEN A GAME ENDS

def end_win(ans):
    end_window = Toplevel(window)
    end_window.title("RESULT WINDOW")
    end_window.geometry('1990x900')
    end_window.config(bg='#3EDBF0')
    msg_label = Label(end_window, text="THE GAME IS OVER", bg='#3EDBF0', fg="black", font=("Arial Bold", 45))
    msg_label.grid(row=1, padx=500, pady=(250, 0))

    score_label = Label(end_window, text=player_name.get() + "'S SCORE IS :  " + ans, borderwidth=9, bg="#FFA900",
                        fg="black", font=("Arial Bold", 35))
    score_label.grid(pady=20, padx=(350, 350))

    exit_btn = Button(end_window, text="EXIT THE GAME", borderwidth=9,
                      bg="black", fg="#FFA900", font=("Arial Bold", 18), command=exit_game)

    exit_btn.grid(row=5)



# THOSE PARAMETERS DEFINE THE COMMNANDS THAT ARE THE MOST IMPORTANT FOR THE GOOD WORKING OF THE CODE

def start():
    global rock1, paper1, scissor1, spock1, lizard1, rock2, paper2, scissor2, spock2, lizard2
    start_window = Toplevel(window)
    start_window.title("ROCK PAPER SCISSORS SPOCK LIZARD")
    start_window.geometry('1990x1080')
    start_window.config(bg='#FF6464')

    rock1 = ImageTk.PhotoImage(Image.open("r1.jpg"))
    paper1 = ImageTk.PhotoImage(Image.open("h1.jpg"))
    scissor1 = ImageTk.PhotoImage(Image.open("sc1.jpg"))
    spock1 = ImageTk.PhotoImage(Image.open("sp1.jpg"))
    lizard1 = ImageTk.PhotoImage(Image.open("l1.jpg"))

    rock2 = ImageTk.PhotoImage(Image.open("r2.jpg"))
    paper2 = ImageTk.PhotoImage(Image.open("h2.jpg"))
    scissor2 = ImageTk.PhotoImage(Image.open("sc2.jpg"))
    spock2 = ImageTk.PhotoImage(Image.open("sp2.jpg"))
    lizard2 = ImageTk.PhotoImage(Image.open("l2.jpg"))

    def msg_update1(msg):
        message['text'] = msg
    
    def msg_update2(msg2):
        message2['text'] = msg2

    def computer_update():
        final = int(computer_score['text'])
    
        final += 1
        computer_score['text'] = str(final)
        if final == 3 or player_score + computer_score == 5:
            ans = player_score['text']
            start_window.destroy()
            end_win(ans)

    def player_update():
        final = int(player_score['text'])
        final += 1
        player_score['text'] = str(final)

        if player_score + computer_score == 5 or final == 3:
            start_window.destroy()
            ans = player_score['text']
            end_win(ans)

    options = ["rock", "paper", "scissors", "spock", "lizard"]






    # PARAMETERS THAT ARE CHECKED TO SEE IF A GAME HAS BEEN WINNED AND THE REASONS OF THAT WIN

    def winner_check(p, c):
        if p == c:
            msg_update1("TIE !")
            msg_update2("TRY AGAIN NOW TO CONTINUE...")

        elif p == "rock":
            if c == "lizard":
                msg_update1("PLAYER WINS !")
                msg_update2("ROCK CRUSHES LIZARD")
                player_update()
            elif c == "scissors":
                msg_update1("PLAYER WINS !")
                msg_update2("ROCK CRUSHES SCISSORS")
                player_update()
            elif c == "paper":
                msg_update2("PAPER COVERS ROCK")
                msg_update1("CPU WINS !")
                computer_update()
            elif c == "spock":
                msg_update2("SPOCK VAPORIZES ROCK")
                msg_update1("CPU WINS !")
                computer_update()
            else:
                msg_update1("CPU WINS !")
                computer_update()

        elif p == "paper":
            if c == "rock":
                msg_update1("PLAYER WINS !")
                msg_update2("PAPER COVERS ROCK")
                player_update()
            elif c == "spock":
                msg_update1("PLAYER WINS !")
                msg_update2("PAPER DISPROVES SPOCK")
                player_update()
            elif c == "scissors":
                msg_update2("SCISSORS CUTS PAPER")
                msg_update1("CPU WINS !")
                computer_update()
            elif c == "lizard":
                msg_update2("LIZARD EATS PAPER")
                msg_update1("CPU WINS !")
                computer_update()
            else:
                msg_update1("CPU WINS !")
                computer_update()

        elif p == "scissors":
            if c == "paper":
                msg_update1("PLAYER WINS !")
                msg_update2("SCISSORS CUTS PAPER")
                player_update()
            elif c == "lizard":
                msg_update1("PLAYER WINS !")
                msg_update2("SCISSORS DECAPITATES LIZARD")
                player_update()
            elif c == "spock":
                msg_update2("SPOCK SMASHES SCISSORS")
                msg_update1("CPU WINS !")
                computer_update()
            elif c == "rock":
                msg_update2("ROCK CRUSHES SCISSORS")
                msg_update1("CPU WINS !")
                computer_update()
            else:
                msg_update1("CPU WINS !")
                computer_update()

        elif p == "spock":
            if c == "scissors":
                msg_update1("PLAYER WINS !")
                msg_update2("SPOCK SMASHES SCISSORS")
                player_update()
            elif c == "rock":
                msg_update1("PLAYER WINS !")
                msg_update2("SPOCK VAPORIZES SCISSORS")
                player_update()
            elif c == "lizard":
                msg_update2("LIZARD POISONS SPOCK")
                msg_update1("CPU WINS !")
                computer_update()
            elif c == "paper":
                msg_update2("PAPER DISPROVES SPOCK")
                msg_update1("CPU WINS !")
                computer_update()
            else:
                msg_update1("CPU WINS !")
                computer_update()

        elif p == "lizard":
            if c == "spock":
                msg_update1("PLAYER WINS !")
                msg_update2("LIZARD POISONS SPOCK")
                player_update()
            elif c == "paper":
                msg_update1("PLAYER WINS !")
                msg_update2("LIZARD EATS PAPER")
                player_update()
            elif c == "scissors":
                msg_update2("SCISSORS DECAPITATES LIZARD")
                msg_update1("CPU WINS !")
                computer_update()
            elif c == "paper":
                msg_update2("LIZARD EATS PAPER")
                msg_update1("CPU WINS !")
                computer_update()
            else:
                msg_update1("CPU WINS !")
                computer_update()
        else:
            pass

    def update_choice(msg):
        computer_choice = options[randint(0, 4)]
        if computer_choice == "rock":
            computer_label.configure(image=rock2)
        elif computer_choice == "paper":
            computer_label.configure(image=paper2)
        elif computer_choice == "scissors":
            computer_label.configure(image=scissor2)
        elif computer_choice == "spock":
            computer_label.configure(image=spock2)
        else:
            computer_label.configure(image=lizard2)
        if msg == "rock":
            player_label.configure(image=rock1)
        elif msg == "paper":
            player_label.configure(image=paper1)
        elif msg == "scissors":
            player_label.configure(image=scissor1)
        elif msg == "spock":
            player_label.configure(image=spock1)
        else:
            player_label.configure(image=lizard1)

        winner_check(msg, computer_choice)




    # GRAPHICAL DEFINITION OF THE BUTTONS

    rock1_btn = Button(start_window, image=rock1, width=125, borderwidth=5, bg='#DA0037',
                       height=125, command=lambda: update_choice("rock"))
    rock1_btn.grid(row=2, column=0, padx=(70, 0), pady=(50, 0))
    rock2_btn = Button(start_window, image=rock2, width=125, borderwidth=5, bg='#150E56', height=125, )
    rock2_btn.grid(row=2, column=10, pady=(50, 0))
    paper1_btn = Button(start_window, image=paper1, width=125, borderwidth=5, bg='#DA0037',
                        height=125, command=lambda: update_choice("paper"))
    paper1_btn.grid(row=4, column=0, padx=(70, 0))
    paper2_btn = Button(start_window, image=paper2, width=125, borderwidth=5, bg='#150E56', height=125)
    paper2_btn.grid(row=4, column=10)
    scissor1_btn = Button(start_window, image=scissor1, width=125, borderwidth=5, bg='#DA0037',
                          height=125, command=lambda: update_choice("scissors"))
    scissor1_btn.grid(row=6, column=0, padx=(70, 0))
    scissor2_btn = Button(start_window, image=scissor2, width=125, borderwidth=5, bg='#150E56', height=125)
    scissor2_btn.grid(row=6, column=10)
    spock1_btn = Button(start_window, image=spock1, width=125, borderwidth=5, bg='#DA0037',
                        height=125, command=lambda: update_choice("spock"))
    spock1_btn.grid(row=8, column=0, padx=(70, 0))
    spock2_btn = Button(start_window, image=spock2, width=125, borderwidth=5, bg='#150E56', height=125)
    spock2_btn.grid(row=8, column=10)
    lizard1_btn = Button(start_window, image=lizard1, width=125, borderwidth=5, bg='#DA0037', height=125,
                         command=lambda: update_choice("lizard"))
    lizard1_btn.grid(row=10, column=0, padx=(70, 0))
    lizard2_btn = Button(start_window, image=lizard2, width=125, borderwidth=5, bg='#150E56', height=125)
    lizard2_btn.grid(row=10, column=10)




    # GRAPHICAL DEFINITION OF THE LABELS AND MESSAGES DISPLAYED

    player_label = Label(start_window, image=rock1, borderwidth=15, bg='#DA0037')
    player_label.grid(row=6, column=2, padx=(20, 200))
    computer_label = Label(start_window, image=rock2, borderwidth=15, bg='#150E56')
    computer_label.grid(row=6, column=8, padx=(200, 20))

    player_title = Label(start_window, text="PLAYER", font=("Arial Bold", 30), bg='#DA0037', fg='white', borderwidth=10)
    player_title.grid(row=2, column=2, padx=(30, 190))
    computer_title = Label(start_window, text="CPU", font=("Arial Bold", 30),
                           bg='#150E56', fg='white', borderwidth=10)
    computer_title.grid(row=2, column=8, padx=(150, 30))

    player_score = Label(start_window, text="0", font=("Arial Bold", 50), bg='#DA0037', fg='white', borderwidth=10)
    player_score.grid(row=10, column=2, padx=(30, 190))
    computer_score = Label(start_window, text="0", font=("Arial Bold", 50), bg='#150E56', fg='white', borderwidth=10)
    computer_score.grid(row=10, column=8, padx=(150, 30))

    message = Label(start_window, text="RESULT PANEL", width=50, font=("Arial Bold", 20), bg='orange', fg='black',
                    borderwidth=10)
    message.grid(row=6, column=5)

    message2 = Label(start_window, text="REASON", width=50, font=("Arial Bold", 20), bg='orange', fg='black',
                    borderwidth=10)
    message2.grid(row=7, column=5)



# RULES OF THE GAME AND A START BUTTON... THIS WINDOW CAN BE CLOSED IF NEEDED WITH MOUSE AND CURSOR

def rules():
    rules_window = Toplevel(window)
    rules_window.title("RULES OF THE GAME")
    rules_window.geometry('1990x900')
    rules_window.config(bg='#FFAA64')
    rules_text = Text(rules_window, height=20, width=50, bg='#FF8264', fg='black', font=("Arial Bold", 18))
    rules_text.grid(padx=450, ipady=5, pady=(90, 5))
    quote = """ HERE IS THE RULES OF THE GAME:
    
 *Scissors cuts Paper
 *Paper covers Rock
 *Rock crushes Lizard
 *Lizard poisons Spock
 *Spock smashes Scissors 
 *Scissors decapitates Lizard
 *Lizard eats Paper
 *Paper disproves Spock 
 *Spock vaporizes Rock
 *Rock crushes Scissors 
 
 *For each round first the player selects
   an action by clicking on any one of the
   Rock, Paper, Scissors, Lizard or Spock Button,
   after that the computer will randomly select an action
   and both will be evaluated. The winner gets a point.
 
 *The game ends when the player loses three times OR if the same thing happens to the computer. This scenario can also happen if the player score and cpu score reache 5 by additioning the 2
 """
    rules_text.insert(END, quote)
    rules_text.config(state='disabled')
    start_btn1 = Button(rules_window, text="START", borderwidth=9, bg="black", font=("Arial Bold", 18),
                        fg="#FFA900", command=start)
    start_btn1.grid()




# LAYOUT OF START AND RULES BUTTON OF BEGINING

start_btn = Button(window, text="START", borderwidth=9, bg="black", fg="#FFA900", font=("Arial Bold", 18),
                   command=start)
start_btn.grid(row=4, padx=(100, 250))

rules_btn = Button(window, text="RULES", borderwidth=9, bg="black", fg="#FFA900", font=("Arial Bold", 18),
                   command=rules)
rules_btn.grid(row=4, padx=(250, 100))


# CODE ENDS HERE

window.mainloop()