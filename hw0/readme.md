## Project0 -- Python Practice

This assignment is for getting familiar with python, and there are three main tasks.

#### **Q1** Get Cost

* There is a function `getCostPerPound` in the *FruitShop* class, so I just call it directly.
* Note that some fruits in the list are not available, i.e., the `getCostPerPound` returns `None`, so remember to check this case and set the cost to 0.

#### **Q2** Buy Cheap Fruits

* This task asks us to select the fruits whose price is no more than the maximum price. So we can just traverse the whole order list and select the needed fruits to cash up.
* There's a bonus that writing the process in 1 line. I adopted the `sum` function, which returns the sum of a temporary list. The temporary list consists of the production of the *numPounds* and the *costPerPound* (filtered by the *maxPrice*).
* Note that some fruits may also be unavailable, so make sure its *costPerPound* exists before comparing it with the *maxPrice*.

#### **Q3** Buy Two Kinds of Fruit

* This task is to find two kinds of fruit, of which the sum of the price equals to the *totalCost*.
* This could be achieved by enumerating, but to search in numerous kinds of fruits efficiently, we can still employ some simple algorithms. First I sort the fruit list in shop by the price to form a list of tuples. Let *A[]* be the price sequence. Then I set two iterators, *i* and *j*, initially pointing to the first and the last tuples, respectively. If the sum of the two pointed elements is higher than the *totalCost*, since the sequence is ordered, we can just let `i+1`; similarly, if that's too small, just let `j-1`. This would go on as long as `i<j` if not hitting the *totalCost*.
* Why not `j+1`/`i-1` here? Consider the first `i-1`/`j+1`. Assume that is `j+1`. It must have been traversed when the other iterator pointed to somewhere *k*, which was not greater than *i*, so we can obtain *totalCost < A[k] + A[j+1] ≤ A[i] + A[j+1]*. It's obviously we do not need to consider `j+1`, and the same as `i+1`.
* Note that the return value shoud be the a touple of keys of *fruitShop.fruitPrices*, but not a string, or the whole string would be sorted out of recognition by the testor.

