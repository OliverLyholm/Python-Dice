import tkinter as tk

def createDice(parent, sides):
    
    diceFrame = tk.Frame(parent)
    
    dice = tk.Label(
        diceFrame,
        text="1",
        bg="black",
        fg="white",
        font=("Arial", 40),
        width=3,
        height=1
    )
    
    diceSides = tk.Label(
        diceFrame,
        text=(f"D{sides}")
    )
    
    diceSides.pack()
    dice.pack()
    
    diceFrame.pack(side="left", padx=5, pady=5)
    
    dice.sides = sides
    diceFrame.sides = sides
    diceFrame.dice = dice
    
    return dice