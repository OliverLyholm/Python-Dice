import tkinter as tk
from .dice import createDice
from .menu import createMenu
from functions.functions import rollDice





def createWindow():
    window = tk.Tk()
    window.title("Dice Roller")
    window.geometry("800x600")
    
    def addDice():
        for _ in range(diceAmount.get()):
            createDice(diceMainFrame, diceSides.get())
            
    def rollAllDice():
        for diceFrame in diceMainFrame.winfo_children():
            dice = diceFrame.dice
            result = rollDice(dice.sides)
            dice.config(text=result)

    
    diceSides = tk.IntVar(value=6)
    diceAmount = tk.IntVar(value=1)
    
    
    
    diceMainFrame = tk.Frame(window)
    diceMainFrame.pack()
    
    createMenu(window, diceSides, diceAmount, addDice)
    
    rollButton = tk.Button(window, text="Roll", command=rollAllDice)
    rollButton.pack()
    
    return window

