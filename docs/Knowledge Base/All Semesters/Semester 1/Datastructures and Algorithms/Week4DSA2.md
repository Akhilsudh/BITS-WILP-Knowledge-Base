# Week 4 (cont.)
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 22/Aug/2021

## Topics Covered
1. Rules to Find Big$\mathcal{O}$ Notation (cont.)
2. Little$\mathcal{o}$ and ## Little$\omega$
3. Bubble Sort

## Rules to Find Big$\mathcal{O}$ Notation (cont.)
- It is considered poor taste to include constant factors and lower order terms in the big$\mathcal{O}$ notation
- Consider a function $2n^2$ is $\mathcal{O}(4n^2 + 6nlog(n))$, although this is right it is always easier and simpler to write $\mathcal{O}(n^2)$

| Logrithmic            | Linear           | Quadractic         | Polynomial                    | Exponential                   |
| --------------------- | ---------------- | ------------------ | ----------------------------- | ----------------------------- |
| $\mathcal{O}(log(n))$ | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^k)\ (k \ge 1)$ | $\mathcal{O}(a^n)\ (a \gt 1)$ |

- Even though in general we ignore constants in the big$\mathcal{O}$ notation, we need to be careful and check if the constants have very large constants, in this case big$\mathcal{O}$ might not be the right assumption for an algorithm.

| Some Functions Ordered By Growth Rate | Commone Name    |
| ------------------------------------- | --------------- |
| $\mathcal{O}(log(n))$                 | Logrithmic      |
| $\mathcal{O}(log^2(n))$               | Polytlogrithmic |
| $\mathcal{O}(\sqrt{n})$               | Square Root     |
| $\mathcal{O}(n)$                      | Linear          |
| $\mathcal{O}(nlog(n))$                | Linearithmic    |
| $\mathcal{O}(n^2)$                    | Quadratic       |
| $\mathcal{O}(n^3)$                    | Cubic           |
| $\mathcal{O}(2^n)$                    | Exponential     | 

![[Pasted image 20210902212635.png]]

- In the above chart you see that $\sqrt{n}$ crosses over much later over $log^2(n)$ in comparison to other function pairs.

## Little$\mathcal{o}$ and ## Little$\omega$
No matter what value of $c \gt 0$ we choose, we need to see if $g(n) \ge f(n)$. For example for a functions $12n^2 + 6n$, the little$\mathcal{o}$ is $\mathcal{o}(n^3)$.

if $f(n$) is $\mathcal{o}(g(n)$ then $g(n)$ is $\omega(f(n))$


## Bubble Sort
```python
BubbleSort(int [] A, int n)
	Input: An array A containing n>= 1 integers
	Output: The sorted version of the array A
	
	for i = 0 to (n - 1)
		for j = 0 to (n - 1 - i)
			if A[i] > A[j + 1]
				# swap A[j] with A[j + 1]
				temp <- A[j]
				A[j] <- A[j + 1]
				A[j + 1] <- temp
	return A
```
**Analysis of the above algorithm:**
Number of primitive operations



```python
BubbleSortOptimized(int [] A, int n)
	Input: An array A containing n>= 1 integers
	Output: The sorted version of the array A
	
	for i = 0 to (n - 1)
		swaps = 0
		for j = 1 to (n - 1 - i)
			if A[i] > A[j + 1]
				# swap A[j] with A[j + 1]
				temp <- A[j]
				A[j] <- A[j + 1]
				A[j + 1] <- temp
				swaps <- swaps + 1
			if swaps == 0
				break
	return A
```

---
Tags: [[!DatastructuresAndAlgorithmsIndex]]