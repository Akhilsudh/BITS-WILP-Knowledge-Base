# Module 6

## Information Gain
![[Pasted image 20220417111409.png]]
![[Pasted image 20220417111739.png]]
![[Pasted image 20220417112504.png]]

## Gini Index
![[Pasted image 20220417113241.png]]
![[Pasted image 20220417113622.png]]

Inexpensive to construct
Extremely fast at 


### Inductive bias in decision tree learning
- Inductive bias is the assumption made by the model to learn the target function and to generalize beyond training data
- What is the inductive bias of DT Learning
	- Shorter trees are preferred over longer trees
	- Prefer trees that place high information gain attributes close to the root

### Limitations of decision tree learning
- Overfitting
- Building trees that "adapt too much" to the training example may lead to "overfitting"
- May therefore fail to fit additional data or predict future observations reliably

![[Pasted image 20220417114048.png]]

> Training data accuracy increases but the test data accuracy decreases when the size of the tree increases

- Pre pruning:
	- Stop the algorithm before it becomes a fully grown tree
	- General stopping conditions for a node
		- Stop if all instances belong to the same class
		- Stop if all the attribute values are the same
	- More restrictive conditions:
		- Stop if number of instances is less than some user specified threshold
		- Stop if class distribution of instances are independent of the available features
		- Stop if expanding the current node foes not improve impurity measures.
- Post pruning:
	- Grow decision tree to its entirity
	- Trim the nodes of the decision tree ina  bottom up fashion
	- If generalization error improves after trimming, replace sub tree by a leaf node
	- Majority class of instances in the sub tree is used as the class label of leaf node.

## Ensemble methods
- Use multiple learning algorithms to obtain better predictive performance than could be obtained from any one of the constituent learning algorithm
- By combining individual models we can get less bias and less variance.
- This method will perform worse if the error rate is $\varepsilon \gt 0.5$
![[Pasted image 20220417120324.png]]

- Each base class has to be independent of each other.

![[Pasted image 20220417121350.png]]

### Methods for constructing ensemble classifier
- Using different algorithms
- Using different hyper parameters
- Using different training sets
- By manipulating input features
- By manipulating the class labels

### Types of ensemble methods
- Simple methods: 
	- Max voting
	- Averaging
	- Weighted averaging
- Advanced methods:
	- Bagging: Homogeneous weak learners, learning done independently from each other.
	- Boosting: Homogeneous weak learners, learning done sequentially in a adaptive way.
	- Stacking: Heterogeneous weak learners, learning done independently and combines them by training a meta model to output a prediction based on the different weak models predictions.

### Bootstrap Sampling
![[Pasted image 20220417123516.png]]
![[Pasted image 20220417123524.png]]
![[Pasted image 20220417123757.png]]

### Bagging
![[Pasted image 20220417124104.png]]
![[Pasted image 20220417124123.png]]
![[Pasted image 20220417124150.png]]
![[Pasted image 20220417124457.png]]


---
Tags: [[!AMLIndex]]