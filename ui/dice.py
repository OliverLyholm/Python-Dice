import tkinter as tk


def createDice(parent, sides):

    diceFrame = tk.Frame(parent, width=100, height=100, bg="black")

    dice = tk.Label(
        diceFrame,
        text="1",
        bg="black",
        fg="white",
        font=("Arial", 40),
    )

    diceFrame.pack_propagate(False)

    diceSides = tk.Label(diceFrame, text=(f"D{sides}"), bg="black", fg="white")

    diceSides.pack()
    dice.pack(expand=True)

    dice.sides = sides
    diceFrame.sides = sides
    diceFrame.dice = dice

    return diceFrame
