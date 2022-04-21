# Code with Drex
# Best guessing game with python tkinter
import random
import tkinter as tk

root = tk.Tk()

secret_no = random.randint(1, 10)
no_of_guess = 0
guess_limit = 3

def create_ui():
    myFrame = tk.Frame(root, height=250, width=700)
    myFrame.pack()

    upperLabel = tk.Label(myFrame, text="You have 3 triers\n Guess any Number betweend 1 to 10:", bg='blue')
    upperLabel.place(relheight=0.3, relwidth=1)

    myEntry = tk.Entry(myFrame)
    myEntry.place(relx=0.4, rely=0.35)

    playagainBtn = tk.Button(myFrame, text="Play Again", command=lambda: playagain(), state='disabled')
    playagainBtn.place(rely=0.45, relx=0.425)

    checkBtn = tk.Button(myFrame, text="Check", command=lambda: guess())
    checkBtn.place(rely=0.57, relx=0.45)

    resultLabel = tk.Label(myFrame, text="Give your best Guess", bg='blue')
    resultLabel.place(relheight=0.3, relwidth=1, rely=0.7)

    def playagain():
        global secret_no
        global no_of_guess
        secret_no = random.randint(1, 10)
        no_of_guess = 0
        resultLabel['text'] = "Try Again"
        playagainBtn['state'] = 'disabled'
        checkBtn['state'] = 'active'

    def guess():
        global secret_no
        global no_of_guess
        global guess_limit
        guess = int(myEntry.get())
        no_of_guess += 1
        if no_of_guess < guess_limit:
            try:
                if secret_no == guess:
                    resultLabel['text'] = "You won!"
                    playagainBtn['state'] = 'active'
                    checkBtn['state'] = 'disabled'
                elif secret_no > guess:
                    resultLabel['text'] = "Incorrect! Go Higher!"
                elif secret_no < guess:
                    resultLabel['text'] = "Incorrect! Go Lower!"
            except ValueError:
                resultLabel['text'] = "You can only enter Numbers"
        elif no_of_guess == guess_limit:
            resultLabel['text'] = "You Lose! Try Again"
            playagainBtn['state'] = 'active'
            checkBtn['state'] = 'disabled'



create_ui()
root.mainloop()