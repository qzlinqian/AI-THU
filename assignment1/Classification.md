## Classification

### Inline Questions

#### Inline Question 3 in knn.ipynb

> Which of the following statements about 𝑘k-Nearest Neighbor (𝑘k-NN) are true in a classification setting, and for all 𝑘k? Select all that apply.
>
> 1. The decision boundary of the k-NN classifier is linear.
> 2. The training error of a 1-NN will always be lower than that of 5-NN.
> 3. The test error of a 1-NN will always be lower than that of a 5-NN.
> 4. The time needed to classify a test example with the k-NN classifier grows with the size of the training set.
> 5. None of the above.

$\color{blue}{\textit  Answer:}$
2, 4


$\color{blue}{\textit  Explanation:}​$
1. The shape of the decision boundary of k-NN depends on the real boundaries of the different classes. Namely, if the boundary between two classes is round, the decision will also be round.
2. If we use training data as test set, the result of 1-NN would always be the exact same point. Thus, the error is 0. While for 5-NN, the error can be greater than 0.
3. That is false. Take my running result as example, when the test data set is X_train_folds[1], and the training set is the other folds, the accuracy of 1-NN is 0.257000, while that of 5-NN is 0.266000.
4. During classifying, the k-NN classifer needs to explore the entire data and sort the distance. Obviously, the time increases with the data size.

#### Inline question 2 in svm.ipynb

> Describe what your visualized SVM weights look like, and offer a brief explanation for why they look they way that they do.

$\color{blue}{\textit Answer:}​$ 

* They are ambiguous, but we can find some features of the class they present from the figure. Namely, they are just like some low-resolution templates. That is because of sampling, which introduces noise.
* Many of the figures are symmetrical, e.g., in the horse case, it seems that the horse has two heads. That is because the result depends heavily on the layout of the image, which is a weakness of this method.

### Algorithms

#### k-NN

* Obviously, the distance between *i* th test point and *j* th test point is $\sqrt{\sum_{k=1}^{D} (test^{(i)}[k] - train^{(j)}[k])^2}$, i.e., `dists[i, j] = np.sqrt(np.sum(np.square(X[i, :] - self.X_train[j, :])))`.

* In the case of one loop, we can manipulate a whole row together; while in the no loop implementation, if we just extend the two sets into 3-dimensional matrixes, i.e., `dists = np.sqrt(np.sum(np.square(X[:, np.newaxis] - self.X_train), axis=-1))`, it would cost a lot of time, so we need to simplify the process.

* $distances[i, j] = \sqrt{\sum_{k=1}^D(test^{(i)})^2[k] + \sum_{k=1}^D(train^{(j)})^2[k] - 2\sum_{k=1}^D test^{(i)}[k] \cdot train^{(j)}[k]}$.

  Thus, $distances = \sqrt{||test||_{2(row)} \cdot ones(1, n) + ones(n, 1) \cdot ||train||_{2(row)}^T - 2 \cdot test \cdot train^T}$.

#### SVM

* We can define the score function as, $s = X \cdot W​$. The loss of the *i* th element is $L_i = \sum_{j \ne y_i}{max(0, s_{i,j} - s_{i,y_i} + \Delta)}​$. So $loss = \sum L_i + \lambda \cdot \sum_{i,j} W^2​$.
* $\frac{\partial L_i}{\partial s_{i,j}} = \begin{cases} 0 &,  s_{i,j} - s_{i,y_i} + \Delta<0 \\ 1 &, j \ne y_i \\ -num(s_{i,j} - s_{i,y_i} + \Delta>0) & ,j=y_i \end{cases}​$.
* $\frac{\partial s_{i,j}}{\partial W_{:,j}} = X[i,:]$, and $dW[:,j] = \sum \frac{\partial L_i}{\partial W_{:,j}} = \sum \frac{\partial L_i}{\partial s_{i,j}} \cdot \frac{\partial s_{i,j}}{\partial W_{:,j}}$. The $dW$ should also add the regulation by $+2\lambda W$.

#### Softmax

* According to the softmax function, the loss can is: $L_i = -ln(\frac{e^{s_{i,y_i}}}{\sum_{j}e^{s_{i,j}}}) = ln(\sum_{j}e^{s_{i,j}}) - s_{i,y_i}$.
* $\frac{\partial s_{i,j}}{\partial W_{:, j}} = X[i,:]$.
* $\frac{\partial L_i}{\partial W_{:,j}} = \begin{cases} \frac{1}{sum_j e^{s_{t,r}}} \cdot \frac{\partial e^{s_{i,:}}}{\partial W_{:,j}} = \frac{e^{s_{i,:}}}{sum_j e^{s_{t,r}}} \cdot X[i,:] &, \text{when }  j \ne y_i  \\ (\frac{e^{s_{i,:}}}{sum_j e^{s_{t,r}}} -1) \cdot X[i,:] &, \text{when } j=y_i \end{cases}$.

### Performance Analysis

* The vectorised implementation is very efficient and fast.
* The accuracy of k-NN on test set is about 28% in the best case, while svm and softmax can reach 36-38%.
* When use *Stochastic Gradient Descent*, the loss (in the svm case) would decrease rapidly during the first 800 loops, and seldomly changes after 1500 iterations. That can help us to decide the iteration times in validation.
* k-NN shows that the best k in this case is 10; while the svm and softmax show that the best parameter is a learning rate of $10^{-7}$ and a regulation strength of $2.5\times 10^4$.
* The visualisation result of svm and softmax is interesting. There are much more noise in the softmax figure, and the origin shape cannot always be recognised by human eyes; while the result no longer depends on the picture layout.