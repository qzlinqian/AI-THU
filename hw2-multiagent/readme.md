## Project 2 -- Multi-Agents

This project implement Minimax, Alpha-Beta Pruning, Expectimax search algorithms with multiple ghosts and tree layers.

### Implementation Details

#### Reflex Agent

This agent evaluate the all the legal actions rather than states and then returns the action with the highest value.

* I used a intuitional evaluate function -- the closer the pacman to one of the food dots, the farther from all of the ghosts, the higher the value is.
* To numerically present the influence of the distance, I employed reciprocal to the distance. This is also consistent with the reality -- if a food/ghost is too far, its influence can be very little.
* Note: if there's wall between the pacman and the "nearest" food (in Manhattan Distance), it would just stop unless the ghost is coming. I cannot solve this as long as I'm using Manhattan Distance...

#### Minimax

* In this implementation, I replaced the recursion with my own stack... That's tiring...

* I build the minimax tree by layers and expand the lowest layer every time.
* At ghost layer, just choose the minimum value, while the maximum at pacman layer. Nothing special.

#### Alpha-Beta Pruning

* Here I defined a recursive function `miniMaxProne(self, gameState, agent, depth, alpha, beta)`, so that as long as the alpha/beta is updated, i.e., the branch is pruned, the function will return to the last layer with a updated alpha/beta.
* The goal of all ghosts is consistent, no matter whether the ghost is adjacent to the pacman. We can just keep comparing the new values with the [alpha, beta] and update this interval.
* At first I expand the tree from the agent and layer in the argument, so I need to traverse the legal actions of the first step. That would wrongly expand some nodes.

#### Expectimax

* It's almost the same as the alpha-beta pruing question, except this time the ghosts won't choose the minimum action, but just return the mean (expectation) value of the following legal actions (because they are expected to choose different actions at random).

#### Evaluation Function

* It's a state evaluation function, so we don't know whether the pacman meet a food dot at current state. What we could account on is only the number of the food dots. The fewer the dots, the higher the value.
* I also introduced the food heuristic into this evaluation function. It is just the same as what I implemented in the search project, and finally I applied reciprocal to this cost.
* The ghost should also be considered. If the pacman is caught by a ghost in a state, the value would be pretty low. If the ghost is very far (no less than 6 steps in my implementation), or it is within its scared time by the time it meet the pacman, I just ignored it. Only the ghosts which is close and not scared should be considered and the value is also very low.
* However, as long as we use Manhattan Distance, the pacman would be fooled by the wall and sometimes stuck in a corner stationarily. In these cases, the pacman will only move if the ghost approaches, but I cannot find a proper substitution.

### Comparison

* The ReflexAgent always finds the best action so it is fast but is easy to die.
* The MinimaxAgent is slow, you know, especially in multiple depths. Although the AlphaBetaAgent is a little faster (not much), it has nothing to do with the result. However, they may also fail. The winning rate in smallClassic with depth=2 is 1/10.
* The ExpectimaxAgent is much likely to survive. In trappedClassic, the AlphaBetaAgent wins by the rate of 0/10, while 7/10 for ExpectimaxAgent.
* My evaluation function will help the pacman to win at a rate of 9/10 with a higher score at smallClassic case when depth=2. Otherwise, the rate is 2/10.

### Discussion

* The ReflexAgent cannot predict the motion of the other side, so it dies easily.
* The MinimaxAgent and AlphaBetaAgent think the ghosts are smart adversaries, which is contradict to the reality; while the ExpectimaxAgent takes the ghosts as ordinary adversaries, which describes the reality more properiately, so it plays better.
* The AlphaBetaAgent cannot always prune many branches, so the reduced time to the MinimaxAgent is limited. In the worst cases, it cannot save any time.
* The approximation of Manhattan Distance can lead to the pacman being fooled by the wall and sometimes stucking in a corner stationarily, which cannot be avioded. Thus, the pacman will lose some great eating timing and be caught by the ghosts.