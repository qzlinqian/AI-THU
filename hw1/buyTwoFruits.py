# buyLotsOfFruit.py
# -----------------
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

  python buyTwoFruits.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Welcome to shop fruit shop
The sum of unit prices of ('oranges', 'pears') is 7
The sum of unit prices of ('apples', 'oranges') is 8
The sum of unit prices of ('apples', 'strawberries') is 13
"""
from __future__ import print_function
from shop import FruitShop
import util


def buyTwoKindsOfFruit(totalCost, fruitShop):
    """
        orderList: List of (fruit, numPounds) tuples
        totalCost: 
        fruitShop: The FruitShop class

    Returns two kinds of fruits such that the sum of unit prices is totalCost.
    """
    "*** YOUR CODE HERE ***"
    raise util.raiseNotDefined()
    

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    fruitPrices = {'apples':5, 'oranges': 3, 'pears': 4, 'limes': 6, 'strawberries': 8}
    shop = FruitShop('shop', fruitPrices)
    print('The sum of unit prices of', buyTwoKindsOfFruit(7, shop), 'is', 7)
    print('The sum of unit prices of', buyTwoKindsOfFruit(8, shop), 'is', 8)
    print('The sum of unit prices of', buyTwoKindsOfFruit(13, shop), 'is', 13)
