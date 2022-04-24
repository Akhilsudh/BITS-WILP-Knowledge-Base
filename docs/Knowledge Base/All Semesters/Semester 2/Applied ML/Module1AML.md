# Module 1
## Machine Learning
- A scientific discipline that explores the construction and study of algos that can learn from data
- Such algos operate by building a model based on inputs and using that to make predictions or decisions rather than following only explicitly programmed instructions without human intervention

### Traditional Programming VS Machine Learning
We give the computer some data and a program and we expect an output from the same in the case of traditional programming
![[Pasted image 20220116112918.png]]

In case of ML we give the computer some training data and some expected output and we end up getting a procedure that solves the problem for new input data
![[Pasted image 20220116112930.png]]

### Definition by Tom Mitchell (1998)
A computer program is said to learn from **experience** $E$ with respect to some class of **tasks** T and **performance** measure $P$, if its performance at task in $T$, as measured by $P$, improves with experience $E$

### Where does ML fit in?
![[Pasted image 20220116113818.png]]

### Steps of ML
1. Define Business Problem
2. Gathering Data
3. Prepare said data (Takes most of the time, around 80%)
4. Choosing a model
5. Training
6. Evaluation
7. Hyperparameter Tuning
8. Prediction

## Types of Learning
- Supervised/Inductive Learning
- Unsupervised Learning
- Semi-supervised Learning
- Reinforcement Learning

### Supervised Learning
![[Pasted image 20220116120137.png]]
This learning type uses data that is labeled. Data that have categorized data into columns are considered labeled data. 

In the above image we are trying to predict a genralized function $f(x)$ that will predict the potential value of y given a  new value of x.

#### Regression

$$
y = f(x_1, x_2, x_3,..., x_n)
$$

$y = Output$

$f() = Prediction Function$

$x_1, x_2,.., x_n = Features Used$


**Training:** Given a training set of labeled examples, estimate the prediction function f by minimizing the prediction error on the training set
**Testing:** Apply f to a never before seen test example x and output the predicted value y  f(x)

#### Classification
![[Pasted image 20220116123809.png]]

### Unsupervised Learning
![[Pasted image 20220116124304.png]]
Unsupervised learning helps in getting to know not so obvious attributes that categorize data sets into smaller groups in case of clustering

### Reinforcement Learning
- No pre-defined data
- Semi supervised learning model in ML
- Allow an agent to take actions and interact with an environment so as to maximize the total rewards
- Examples
	- Autonomous Cars
	- Game playing
	- Robot in a maze

### Difference between the three types of learning
![[Pasted image 20220116125417.png]]

### Other Categories of Learning
![[Pasted image 20220116125550.png]]
- In batch learning there is a potential for relearning when an updation is needed. It is used ideally done once before deployment
- In case of changing data sets we use online/incremental learning

![[Pasted image 20220116125858.png]]
- Instance based learning: also called as lazy learning. Learning techniques do not build a model but stores all training instance in memory and when they undergo classification they use proximity measures k closely related members to categorize them.

![[Pasted image 20220123112721.png]]
- Model Based learning where we detect patterns in the training data and build a predictive model

## Challenges of machine learning
![[Pasted image 20220123114515.png]]

### Testing and Validation
![[Pasted image 20220123120545.png]]

### Cross Validation
![[Pasted image 20220123122730.png]]

### Choice of Hyperparameters
- Modern ML modesl often use a lot of model params
- Model performance depends on chouce of params
- Each parm can assume a number of values
- Expensive to perform
- Grid Search CV method

### Open Source ML Programming Tools
![[Pasted image 20220123123602.png]]

---
Tags: [[!AMLIndex]]