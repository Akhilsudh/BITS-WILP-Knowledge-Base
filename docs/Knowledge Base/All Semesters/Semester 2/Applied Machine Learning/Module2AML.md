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



---
Tags: [[!AMLIndex]]