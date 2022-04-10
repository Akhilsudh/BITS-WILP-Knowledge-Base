# Module 2
## Machine Learning Pipeline
- Framing a machine learning problem
- Get the data
- Data Pre processing
- Data Visualization and Analysis
- Feature Engineering
- Model Building and Evaluation
- Fine tune the model
- Present the solution
- Launch, monitor and maintain

![[Pasted image 20220123125617.png]]

## Case Study
Bank is loosing too much money due to bad loans and wants to reduce losses. The following things are looked at to frame the problem
![[Pasted image 20220123125420.png]]

### Frame the problem
- Define the objectives in business terms
- How will your solution be used
- What are the current solutions
- How should you frame this problem (Supervised or unsupervised)
- How should the performance be measured
- Is the performance measure aligned with the business objective
- What are comparable problems
- Is Human expertise available
- How would you solve the problem?
- List the assumptions you have made
- What would be the minimum performance needed to reach the business objective? 

## An example problem statement
- Build a model of housing prices using census data
	- Data attributes <Population, median income, median housing price, ...> and so on for each district
	- Districts are the smallest geographical unit (population ~600-3000)
- The model to predict the median housing price in an district, given all the other metrics
- Goodness of the model is determined by how close the model output is wrt actual price for unseen data.

### Framing the problem
- What is the expected usage and benefit?
	- Impacts the choice of algorithms, goodness measure, and effort in lifecycle management of the model
- What is the baseline method and its performance?

![[Pasted image 20220206111531.png]]

- Analyze the dataset
	- Each instance comes with the expected output
	- Hence we are going with supervised
	- Goal is to predict a real valued price based on multiple variables line population, income etc
		- Regression is chosen for this reason
	- Output is based on input data at rest, not rapidly changing data rapidly.
	- Dataset small enough to fit in memory
		- Batch
	- Since we are predicting a single value we are calling it a univariate problem

- Choice of Performance metrics
	- Root Mean Square
	   ![[Pasted image 20220206112316.png]]
	- Mean Absolute Error (MAE)
	   ![[Pasted image 20220206112421.png]]
	   
- Types and properties of attributes
![[Pasted image 20220206120315.png]]
![[Pasted image 20220206121106.png]]

## Data types of attributes
![[Pasted image 20220223214645.png]]
job, marital -> nominal
education -> Ordinal
credit default -> Binary (symmetric)
housing loan -> Binary

- Categorical
- Binary
	- Symmetric (Simple matching coefficient proximity measure)
	- Asymmetric (Jaccart coefficient proximity measure)
- Nominal
- Numerical/continuous (Minkowsky distance for proximity measure)
- to find outliers


## Some pandas functions
```python
df.types() # Get the datatypes of all columns in dataframe
df.info() # Get more info on non null values in data frame
df.describe() # Get statistical summary of each attribute and 5 point summary of numberic attributes
```

## Data Types
- relational/Object data
- Transactional data
- Document data
- Web and social network data
- Spatial data
- time series data

## Model Evaluation Parameters
### Precision
What percentage of tuples that are positive are actually positive

$Precision = \frac{True Positives}{True Positives + False Positives}$

### Recall
What percentage of positive tuples did the classifier label as positive

$Recall = \frac{True Positives}{True Positives + False Negatives}$

### F Measure
Harmonic mean of precision and recall

$F = 2 \times \frac{precision \times recall}{precision + recall}$

High values of $F_1$ score indicates that both the precision and recall both are high

$F_\beta$ is the wighted measure of precision and recall. Here we assign $\beta$ times as much to weight to recall as to precision. This is done if either recall or precision is more important than the other.

$F_\beta = \frac{(1 + \beta^2) \times precision \times recall}{\beta^2 \times precision + recall}$

![[Pasted image 20220410131956.png]]

### Things to note
- Accuracy is useful when data is balanced and all tuples are almost equally occuring
- If the data is imbalanced (When the tuples of a particular category are very little) then we lean on precision and accuracy as a better metric for measuring the model performance
- To artificially create instances for the minority class to balance the data `sklearn` has a `smoat` library that helps us in achieving the same.

### Holdout and Cross validation
Hypermarameters are those that controls the learning process. To know this we need to use cross validation 
![[Pasted image 20220410132406.png]]
We train the model k number of times with different subsetting of train and test samples
The above is trained with taking a param as a hyperparam. We calculate the avg accuracy of the k models and assign the score for that hyperparam and repeat all these steps for other params as hyperparams and see which one has the best score. This helps us getting to know what the hyper parameter is.

### ROC AUC Curve
- ROC is a probability curve between TPR and FPR to show their tradeoff

$TPR = \frac{TP}{TP + FN}$

$FPR = \frac{FP}{TN + FP}$

- AUC shows degree of separateability. It shows how good a model is capable of distinguishing between classes
	- Higher AUC means better the model is at predicting
	- AUC of ROC evaluates model performance on average.
- For model comparison, AUC of ROC should be larger for the model to be superior or better performing.

![[Pasted image 20220410134416.png]]

In python we can use `sklearn`'s `predictProba` to calculate the probabilities that are required for plotting the ROC curve.

---
Tags: [[!AMLIndex]]