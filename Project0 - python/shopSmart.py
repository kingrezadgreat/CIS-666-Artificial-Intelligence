# shopSmart.py
# ------------
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
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    
    """totalCost=0;
    for fruits, prices in orderList: 
        if fruits in fruitShops[0].fruitPrices:
              totalCost = totalCost + fruitShops[0].fruitPrices[fruits] * prices
    """
    # I changed my mind at this point to alternate by shops and use the getPriceOfOrder(orderlist) which is provide by the library instead of going to each one one by one and manipulating 
    # to deal with the object all values have to be initialized to None and only replace them by values directly take from an instance of an object. I dont know why but that is it I guess.
    # the only way to use 'shopSmart(orders, shops).getName()' in the main is to provide the return type of 'shopSmart' as object which has the right attribute otherwise you would get this error: AttributeError: 'str' object has no attribute 'getName'
 
    #x=0
    #print fruitShops[x].name
    #print fruitShops[x].getPriceOfOrder(orderList)
    #print fruitShops
    #print fruitShops.item()
    #print fruitShops.getName
                
    totalCost= None   # comparision variable to find the minimum cost
    retObj = None   # return name of the object with min value
    maxRange = len(fruitShops)
    x=0 # counter
    for i in range(0, maxRange): 
        shopCost = fruitShops[x].getPriceOfOrder(orderList)  # cost for each object
        if totalCost == None or shopCost < totalCost:  # if the cost for the crrent object is less that totalCost or totalCost is empty do:
            totalCost= shopCost
            retObj = fruitShops[x] 
        x=x+1
    return retObj  # return object
       
    
if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  shopSmart(orders, shops)
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples',3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
