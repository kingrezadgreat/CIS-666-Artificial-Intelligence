Name: Reza Shisheie
CSU ID: 2708062
Project0

question 2:
    1. in this question fruits and prices were assigned to the first and second element of each member of the orderList. 
    2. if the fruit that is taken from the fruitList exists in the fruitPrices, it adds the price of that quantity to the total price
    3. finally it returns the value.
    
question 3:
    this one was a little tricky since I had to deal with an object. I seeked help from students and also got hints online.
    first I decided to do all the calculation manually for each one of them but the prblem was the number of objects and how to iterate. Even if that problem is resolved then I had to calcualte the total cost one by one, whcih I eventually relized there is a function availabel in shop to return the total cost. Moreover, the getName() of the 'shopSmart(orders, shops).getName()' only works if the return value of the function is an object. Thus it was a must to deal with object which has the right attribute otherwise you would get this error: AttributeError: 'str' object has no attribute 'getName'.
    
    1. two variables were defined as 'totalCost' for comparision of the total cost which maintains the minimum cost and 'retObj' which maintains the return value or the name of the object with minimum total cost.
    2.  the program iterates between the objects in the fruitShops and calulate the cost for each one by invoking the 'shop.getPriceOfOrder(orderList)' of each one of them. This order list the same for both shops. This is provided in the shop which already has been imported. 
    3. if the cost for the crrent object is less that 'totalCost' or 'totalCost' is empty, 'totalCost' and 'retObj' are updated.
    4. finally, the 'retObj' object is returned which is the object with minimum total cost. 
