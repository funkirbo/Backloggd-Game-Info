from tkinter import*
from new_functions import*

def update(): 
    game = my_entry.get()
    game = createBackloggdLink(game)

    title = getFormattedTitle(game)
    score = getGameScore(game)
    plays = getPlays(game)

    sVar.set(title + "\nScore: " + str(score) + "/5\n" + plays + "Plays\n")

root = Tk()
root.geometry("500x500")
frame = Frame(root)
frame.pack()





label = Label(frame, text = "Enter your game", font = ("Bahnschrift", 25), bg = "Light Grey")
label.pack(pady = 50)





my_entry = Entry(frame, width = 20)
my_entry.insert(0,'')
my_entry.pack(padx = 5, pady = 5)






Button = Button(frame, text = "Submit", command = update)
Button.pack(padx = 5, pady = 5)




sVar = StringVar()
sVar.set("")
label_game = Label(frame, textvariable = sVar)
label_game.pack()

root.mainloop()