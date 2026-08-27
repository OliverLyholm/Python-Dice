import tkinter as tk

from tkinter import simpledialog


def createMenu(window, diceSides, diceAmount, addDice, clearDice, rollAllDice):
    menu = tk.Menu(window)

    diceMenu = tk.Menu(menu, tearoff=0)

    sidesMenu = tk.Menu(diceMenu, tearoff=0)

    def setDiceAmount():
        amount = simpledialog.askinteger(
            "Dice amount", "How many dice do you want?", parent=window, minvalue=1
        )
        if amount is not None:
            diceAmount.set(amount)
            addDice()

    sidesMenu.add_radiobutton(
        label="4 sides", variable=diceSides, value=4, command=setDiceAmount
    )

    sidesMenu.add_radiobutton(
        label="6 sides", variable=diceSides, value=6, command=setDiceAmount
    )

    sidesMenu.add_radiobutton(
        label="8 sides", variable=diceSides, value=8, command=setDiceAmount
    )

    sidesMenu.add_radiobutton(
        label="10 sides", variable=diceSides, value=10, command=setDiceAmount
    )

    sidesMenu.add_radiobutton(
        label="12 sides", variable=diceSides, value=12, command=setDiceAmount
    )

    sidesMenu.add_radiobutton(
        label="20 sides", variable=diceSides, value=20, command=setDiceAmount
    )

    diceMenu.add_cascade(label="Sides", menu=sidesMenu)

    menu.add_cascade(label="Add Dice", menu=diceMenu)

    menu.add_command(label="Roll", command=rollAllDice)

    menu.add_command(label="Clear Dice", command=clearDice)

    window.config(menu=menu)
