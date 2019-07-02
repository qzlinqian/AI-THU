## Deep Learning

### Inline Question

#### Inline Question 2 in FullyConnectedNets.ipynb

> Did you notice anything about the comparative difficulty of training the three-layer net vs training the five layer net? In particular, based on your experience, which network seemed more sensitive to the initialization scale? Why do you think that is the case?

$\color{blue}{\textit  Answer:}$

Training five layer net is far more difficult than training the three layer net and is more sensitive to the weight scale. The reason might be that the loss function of the five layer net is more complex and harder to optimal domain, which leads to more sensitive to initialization.

#### Inline Question 1 in RNN_Captioning.ipynb

The scale of the input set of character-level models is very small. However, the hidden layers of character-level models are far more larger than word-level models.



### Algorithms

#### Fully Connected Net

* The forward function from i-th layer to (i+1)-th layer is $a_{i+1} = f(a_{i}W_{i} + b)$ and the loss is $l_{i+1} = g(a_{i+1})$.

* For the backward part, take the partial derivatives to $l_{i+1}$, we have $d(a_{i+1}) = g' = dout$, $d(a_i) = dout * f' * W_{i}^T$, $d(b) = dout * f'$, $d(W_{i}) = dout * f' * x_i^T$.

* In ReLU case, we can just substitute the function $f(x) = max(0, x)$ into the fomula.

* In momentum update, we have 

  ```
  v = mu * v - learning_rate * dx # integrate velocity
  x += v # integrate position
  ```

#### RNN-Captioning

* The forward fomula for RNN is $x_{t+1} = RNN_t(x_h) = tanh(x_tW_x + h_tW_h + b)$. And the backward fomula can be obtained by take partial derivatives to the forward fomula.

#### Convolutional Networks

* The basic ConvNets can be described as

  > INPUT -> [ [CONV -> ReLU ] * N –> POOL ] * M –> [ FC -> ReLU ] * K –> FC



### Analysis

* With more layers, the error of the fully connected networks would drop faster, but would be more sensitive to the weight_scale value. Sometimes with a incorrect weight value, the accuracy of the multiple-layer networks would be close to 0.
* CNN partly connect the input data, thus far more efficient than the fully connected networks.
* RNN is a time-based model.
* In most cases, CNN is used to break the input into components and find features in it, while RNN is used to create the combinations between the sub-components.
* Training a GAN is very time consuming, especially with high-dimensional input.