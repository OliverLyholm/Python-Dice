import random


def rollDice(sides):
    """Generates a random number inbetween 1 and sides of the dice

    Args:
        sides (tk.VarINT): Amount of sides a dice has

    Returns:
        Randint: Random number between 1 and sides
    """    
    return random.randint(1, sides)
