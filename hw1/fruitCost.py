# costs.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
To run this script, type

  python fruitCost.py

Once you have correctly implemented the fruitCost function,
the script should produce the output:

Welcome to shop fruit shop
The cost of 4 pounds of apples is 20
The cost of 5 pounds of oranges is 15
The cost of 6 pounds of grapes is 0
"""
from __future__ import print_function
from shop import FruitShop
import util


def fruitCost(fruit, numPounds, fruitShop):
    """
        fruit: Fruit string
        pound: Number of pounds
        fruitShop: The FruitShop class
        
    Return the cost of certain pounds of fruit. If the fruit doesn't 
    appear in the fruit shop, return 0.
    Hint: You may get the unit price of fruit from the fruitShop.fruitPrices.
    For example, the unit price of apples can be obtained from 
    fruitShop.fruitPrices['apples'] or fruitShop.getCostPerPound('apples').
    """
    "*** YOUR CODE HERE ***"
    raise util.raiseNotDefined()
    
    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    fruitPrices = {'apples':5, 'oranges': 3, 'pears': 4}
    shop = FruitShop('shop', fruitPrices)
    print("The cost of 4 pounds of apples is", fruitCost('apples', 4, shop))
    print("The cost of 5 pounds of oranges is", fruitCost('oranges', 5, shop))
    print("The cost of 6 pounds of grapes is", fruitCost('grapes', 6, shop))