import tkinter as tk
from .dice import createDice
from .menu import createMenu
from functions.functions import rollDice


def createWindow():
    window = tk.Tk()
    window.title("Dice Roller")
    window.geometry("800x600")

    diceSides = tk.IntVar(value=6)
    diceAmount = tk.IntVar(value=1)
    diceCount = 0

    def addDice():

        nonlocal diceCount

        for _ in range(diceAmount.get()):
            dice = createDice(diceMainFrame, diceSides.get())

            row = diceCount // 7
            column = diceCount % 7

            dice.grid(row=row, column=column, padx=5, pady=5)

            diceCount += 1

    def rollAllDice():
        for diceFrame in diceMainFrame.winfo_children():
            dice = diceFrame.dice
            result = rollDice(dice.sides)
            dice.config(text=result)

    def clearDice():
        nonlocal diceCount

        for diceFrame in diceMainFrame.winfo_children():
            diceFrame.destroy()

        diceCount = 0
        
    
    diceScrollFrame = tk.Canvas(window)
    diceScrollBar = tk.Scrollbar(window, orient="vertical", command=diceScrollFrame.yview)

    diceMainFrame = tk.Frame(diceScrollFrame)
    
    diceScrollFrame.configure(yscrollcommand=diceScrollBar.set)
    
    diceScrollBar.pack(side="right", fill="y")
    diceScrollFrame.pack( fill="both", expand=True)
    
    dicewindow = diceScrollFrame.create_window(
        (0, 0),
        window=diceMainFrame,
        anchor="n"
    )
    
    
    
    def updateScrollFrame(event):
        diceScrollFrame.configure(scrollregion=diceScrollFrame.bbox("all"))
        
    diceMainFrame.bind("<Configure>", updateScrollFrame)

    addDice()

    createMenu(window, diceSides, diceAmount, addDice, clearDice, rollAllDice)

    return window
