import tkinter as tk
from .dice import createDice
from .menu import createMenu
from functions.functions import rollDice
from pathlib import Path


def createWindow():
    
    """Creates the main window

    Returns:
        tk.tk: Tkinter window
    """    
    window = tk.Tk()
    window.title("Dice Roller")
    window.geometry("800x600")

    iconPath = Path(__file__).parent.parent / "DiceIcon.png"
    icon = tk.PhotoImage(file=iconPath)
    window.iconphoto(True, icon)

    diceSides = tk.IntVar(value=6)
    diceAmount = tk.IntVar(value=1)
    diceCount = 0

    def addDice():
        
        """Add dice depending on what diceamount was chosen
        """        

        nonlocal diceCount

        for _ in range(diceAmount.get()):
            dice = createDice(diceMainFrame, diceSides.get())

            row = diceCount // 7
            column = diceCount % 7

            dice.grid(row=row, column=column, padx=5, pady=5)

            diceCount += 1

    def rollAllDice():
        
        """Roll all dice when button in pressed
        """        
        for diceFrame in diceMainFrame.winfo_children():
            dice = diceFrame.dice
            result = rollDice(dice.sides)
            dice.config(text=result)

    def clearDice():
        
        """Clear all currently created Dice
        """        
        
        nonlocal diceCount

        for diceFrame in diceMainFrame.winfo_children():
            diceFrame.destroy()

        diceCount = 0

    diceScrollFrame = tk.Canvas(window)
    diceScrollBar = tk.Scrollbar(
        window, orient="vertical", command=diceScrollFrame.yview
    )

    diceMainFrame = tk.Frame(diceScrollFrame)

    diceScrollFrame.configure(yscrollcommand=diceScrollBar.set)

    diceScrollBar.pack(side="right", fill="y")
    diceScrollFrame.pack(side="left", fill="both", expand=True)

    diceScrollFrame.create_window((0, 0), window=diceMainFrame, anchor="nw")

    def updateScrollFrame(event):
        """Update the scroll region when the dice frame changes size.

        Args:
            event (event): The Tkinter Configure event.
        """        
        diceScrollFrame.configure(scrollregion=diceScrollFrame.bbox("all"))

    diceMainFrame.bind("<Configure>", updateScrollFrame)

    addDice()

    createMenu(window, diceSides, diceAmount, addDice, clearDice, rollAllDice)

    return window
