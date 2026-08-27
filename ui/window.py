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

    

    
    
    
    diceMainFrame = tk.Frame(window)
    diceMainFrame.pack()
    
    createMenu(window, diceSides, diceAmount, addDice)
    
    rollButton = tk.Button(window, text="Roll", command=rollAllDice)
    rollButton.pack()
    
    return window

