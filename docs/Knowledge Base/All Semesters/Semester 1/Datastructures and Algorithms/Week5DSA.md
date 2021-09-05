# Week 5
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 28/Aug/2021

## Topics Covered
1. Selection Sort
	1. Steps
	2. Algorithm
		1. Sort Function
		2. Optimized Sort Function
	3. Algorithm Analysis
		1. Time Complexity
		2. Space Complexity


## Selection Sort
Selection sort uses similar concepts of Bubble sort but then instead of bubbling up the max value in each pass, we select the max value in the given array and then swap that to the last position directly and do the same to the second last element and so on.

### Steps
Let us consider the following arrays
Initial State: $[\ 4, 1, 7, 5, 2, 3\ ]$
At each pass we select the maximum value of the array and move it to the end:
Pass 1: $[\ 4, 1, 3, 5, 2, 7\ ]$
Pass 2: $[\ 4, 1, 3, 2, 5, 7\ ]$
Pass 3: $[\ 2, 1, 3, 4, 5, 7\ ]$
Pass 4: $[\ 2, 1, 3, 4, 5, 7\ ]$
Pass 5: $[\ 1, 2, 3, 4, 5, 7\ ]$

### Algorithm
#### Sort Function
```python
sort(A):
	Input: An array of size n
	Ouput: The sorted version of the array A
	
	for i = 1; i < n do
		max = A[0]
		maxIndex = 0
		for j = 1; j < (n - i) do
			if A[j] > max then
				max = A[j]
				maxIndex = j
		A[maxIndex] <-> A[n - i]
```

#### Optimized Sort Function
```python
optimizedSort(A):
	Input: An array of size n
	Ouput: The sorted version of the array A
	
	for i = 1; i < n do
		
		inversions = 0
		for j = 0; j < (n - 1 - i) do
			if A[j] > A[j + 1] then
				inversion = inversion + 1
		if invversions == 0 then
			break 
		
		max = A[0]
		maxIndex = 0
		for j = 1; j < (n - i) do
			if A[j] > max then
				max = A[j]
				maxIndex = j
		A[maxIndex] <-> A[n - i]
```

### Algorithm Analysis
#### Time Complexity
Just like the bubble sort, here we see that the outer loop runs in the order of $n$ and the inner loop is also running in the order of $n$
So the worst case time complexity is $\mathcal{O}(n^2)$
Best case time complexity (Where array is already sorted) is also  $\mathcal{O}(n^2)$

#### Space Complexity
Since no extra data structures were used, the space used is contant, so the space complexity in all cases is $\mathcal{O}(1)$

---
Tags: [[!DatastructuresAndAlgorithmsIndex]]