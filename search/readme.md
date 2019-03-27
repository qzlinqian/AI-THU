## Project 1 -- Search in Pacman
This project implements some search algorithms (DFS, BFS, UCS, A\*) in a Pacman world and have some heuristic functions designed. There are 8 main tasks. The implementation of different algorithms only differs partly, so I would explain the solution to the first question in detail and only figure out the differences in other tasks.

### The Implementation Details

#### The explaination of some special words
* **Expand**/**Visit**: To search and traverse all the valid successors of a node.
* **Reach**: The node is a valid successor of an expanded node.

#### **Q1** Depth First Search
* For consistency, I maintain a *waiting_list* Stack here to store the reached nodes and a *visited* Count to store the nodes' status and precessor nodes (so that the information can be searched by position). The reached nodes to be visited would be in the *waiting_list* while the reached nodes would be updated in the *visited*.
* The agent search the successors of a state in a loop until the goal is hit (or the waiting_list is empty and there's nothing to add, in which case there would be no solution)
* In this algorithm, the node would be added even it has been added into the *waiting_list* before. We should take the last node to reach it before it is expanded as its precessor. So a status mark is also needed. The status is stored in the *visited* with the precessor information, and it would be *DISCOVERED* when it is in the waiting_list and not expanded; it would change to *VISITED* after being expanding.
* Once the goal state is hit, we can use the precessor node information stored in *visited* to track back its precessor node one by one. I stored the *action* information in the *visited*, and a Quene is maintained to store the actions along the road. When we get back to the start state, the full path is obtained.
* The *cost* information of a successor is not needed here.

#### **Q2** Breadth First Search
* The *waiting_list* here is a Quene, where the nodes added first would be first to expand.
* A state node has been visited when and only when the *state is in visited*.
* The enque rule: as long as a node has been reached, it can no longer enque again. Thus, the precessor node (and also the action) would not be updated; the status and cost information is not needed.

#### **Q3** Uniform Cost Search
* The data structure used for *waiting_list* is PriorityQueue this time.
* The single action cost would be recorded in *waiting_list*. The *visited* stored the total cost from start state to get that state, which is also used as the priority of the quene (it would be updated in time).
* The update rule: the node has not visited (or the former cost must be lower) and the new cost is lower. To update, update the precessor node, action, total cost information in *visited*, and update the priority of the state in *waiting_list* (if not in the quene, it would be added in).

#### **Q4** A\* search
* It's almost the same with Uniform Cost Search, just change the priority of *waiting_list* to the sum of the total cost to get there and a estimated cost from there to goal, i.e., `cost_new + heuristic(successor[0], problem)`.
* Note that heuristic would not change with time, so we can update node information just when the precessor's cost is lower.

#### **Q5** Finding All the Corners
* Here I define the state as (position, corner_state), where *position* is just the coordinate value of the point, and *corner_state* is a 4-digit number in base 2, each digit of which represent a corner. If a corner is visited by the node or its precessors, the relative number woudl be 1, or it would be 0.
* To obtain the successors, in the function *getSuccessors()*, if a state hit a corner, the relative digit would be set as 1, i.e., `corner_stat |= self.corner_index[i]`.
* The other part of this implementation is just same as in other search problem.
* I attempted to use the number of hit corners as the indicator, but you know, a corner may be hit for many times.
* Obviously, this state representation just change the problem into a 3-dimensional problem, where the start state is (startingPosition, (0000)<sub>2</sub>) and the goal is (1111)<sub>2</sub>. So the former search algorithms can still work.

#### **Q6** Corners Problem: Heuristic
* The task here is to determine a heuristic function for the corner search problem.
* I just use largest the manhattan distance between the current state and the unreached corners (by the state and its precessors).
* That's not bad because it expanded 1140 nodes in the test case.

#### **Q7** Eating All The Dots
* This task needs a heuristic function to estimate how many steps needed to eat all the remaining food.
* If there's no food, just return 0.
* I have tried the largest manhattan distance between the current state and the remaining food, but it turned out that it was too rough and over 9900 nodes were expanded.
* The problem of the former function is it cannot indicate whether other food is close to or far from the farthest food. So I use a rectangle to describe the positions of the remaining food, i.e., to find the four boundaries of the remaining food's positions. To reach all the food, take the *x* axis as example, the Pacman must travel from left boundary to right boundary, and it also needs to get to one of the two boundaries to complete the search. The same procedure is also needed in the *y* axis, for top and bottom boundaries. So the total cost could be estimated as `(top - bottom) + (right - left) + min(|x-left|, |x-right|) + min(|y-top|, |y-bottom|)`.
* The final result is 8218 nodes and I could not come up with a more proper heuristic function.

#### **Q8** Suboptimal Search
* This task needs a goal reach judgment and a search algorithm.
* To find the nearest food, we could just use BFS.
* In this case, the goal is to reach a remaining food, i.e., whether the state position in the argument has food.

### Some Notes
* The data structure adopted in `search.py` must be those provided in `util.py`, or the program would go wrong.
* I used to think the action information in Q1 & Q2 could be more than 1, namely, the Pacman could go many steps at once. Rationally speaking, then that scheme would be very slow and awkward. "Live a day at a time", move a step at a time, just as what I'm familiar with in the robotic motion planning.
