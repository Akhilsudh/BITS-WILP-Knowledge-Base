# Week 2 
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 31/Jul/2021

## Topics Covered
1. Questions Answered on Previous Week Topics
2. Concept of Recursion

### Questions Answered on Previous Week Topics
- **Question**: If an algorithm for solving a problem has a loop that runs $n$ times and another algorithm to solve the same problem and has a loop that runs $n\over2$, then what is the comparative analysis for these two algorithms?
  **Answer**: Both are proportional to $n$ since the only thing that changed here is the constant $c$, which is $1$ in the first case and $1\over2$ in the other.
- **Question**: Do all primitives have the same constant running time?
  **Answer**: This is not the case but as a concept it is taken as to be the same since the running time for a given operation is not dependent on the number of inputs.
- **Question**: From the array max example (discussed here: [[Week1DSA#What is time and space complexity]]) we see that the algorithm in its worst case is $7n - 2$, what is it in its best case?
  **Answer**: In the best case, the maximum value is in the starting of the array $A[0]$ itself. In this case the inside of the if block will not even execute so we can reduce $2$ primitive steps from the calculation, this will lead to the following analysis:
  
$$TimeComplexity < (2 + 1 + n + (n - 1) * (2 + 0 + 2) + 1)$$

$$TimeComplexity < 5n$$

### Concept of Recursion
Consider the algorithm for finding the factorial of a number:
```
Algorithm factorial(n):
	Input: A number n > 0.
	Output: The factorial of n.
	
	product <- 1
	for i <- 1 to n do
		product <- i * product
	return product
```

The above algorithm is called an iterative one since it employs loops, the same can be written through recursive function calls such as below:
```
Algorithm factorial(n):
	Input: A number n > 0.
	Output: The factorial of n.
	
	product <- 1
	if n = 1 then
		return 1
	else
		result = n * factorial(n - 1)
		return result
```
Here you see that the loop is removed and the algorithm is called recursively, but it yields the same result. One must be careful to have at least one base case (Here $product \longleftarrow 1$) must exist, else recursion will go on indefinitely.

Now a recursive implementation for the array max algorithm ([[Week1DSA#What is time and space complexity]]) would be as follows:
```
Algorithm recursiveMax(A, n):
	Input: An array A storing n >= 1 integers.
	Output: The maximum element in A
	
	if n = 1 then
		return A[0]
	return max{recursiveMax(A, n-1), A[n-1]}
```

The running time for the same will be shows as below:

$$T(n) = 3,\ if\ n=1$$

$$T(n) = T(n-1)+7,\ otherwise$$

---
Tags: [[!DatastructuresAndAlgorithmsIndex]]