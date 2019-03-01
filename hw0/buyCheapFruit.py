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

  python buyCheapFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Welcome to shop fruit shop
By fruit with unit price <=6, cost of [('apples', 2), ('pears', 3), ('limes', 4)] is 22
By fruit with unit price <=4, cost of [('apples', 2), ('pears', 3), ('oranges', 2)] is 18
By fruit with unit price <=4, cost of [('apples', 2), ('pears', 3), ('limes', 4)] is 12
"""
from __future__ import print_function
from shop import FruitShop
import util


def buyCheapFruit(orderList, maxPrice, fruitShop):
    """
        orderList: List of (fruit, numPounds) tuples
        maxPrice: The maximum price. We only buy fruit with the unit price cheaper than maxPrice
        fruitShop: The FruitShop class

    Returns the cost of order. Only the fruit in the orderList and
    cheaper than maxPrice is bought.
    """
    totalCost = 0.0  # Then that's useless
    "*** YOUR CODE HERE ***"
    return sum(order[1] * fruitShop.getCostPerPound(order[0]) for order in orderList if (fruitShop.getCostPerPound(order[0]) and (fruitShop.getCostPerPound(order[0]) <= maxPrice)))
    # A temporary list whose elements are numPounds * costPerPound (if it exists and <= maxPrice)
    raise util.raiseNotDefined()
    

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    fruitPrices = {'apples': 5, 'oranges': 3, 'pears': 4}
    shop = FruitShop('shop', fruitPrices)
    orderList1 = [('apples', 2), ('pears', 3), ('limes', 4)]
    print('By fruit with unit price <=6, cost of', orderList1, 'is', buyCheapFruit(orderList1, 6, shop))
    orderList2 = [('apples', 2), ('pears', 3), ('oranges', 2)]
    print('By fruit with unit price <=4, cost of', orderList2, 'is', buyCheapFruit(orderList2, 4, shop))
    orderList3 = [('apples', 2), ('pears', 3), ('limes', 4)]
    print('By fruit with unit price <=4, cost of', orderList3, 'is', buyCheapFruit(orderList3, 4, shop))
