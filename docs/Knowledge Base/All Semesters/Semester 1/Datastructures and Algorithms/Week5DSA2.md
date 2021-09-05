# Week 5 (cont.)
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 29/Aug/2021

## Topics Covered
1. Insertion Sort
	1. Steps
	2. Algorithm
		1. Sort Function
		2. Optimized Sort Function
	3. Algorithm Analysis
		1. Time Complexity
		2. Space Complexity


## Selection Sort

### Steps
Let us consider the following arrays
Initial State: $[\ 1, 4, 7, 5, 2, 3\ ]$
At each pass we sort the array that we get by adding one element to it, So we first sort indexes $1, 2$ of the array, after that we sort the indexes $1, 2, 3$ and so on till $1, 2, 3, .... , n$ to get the final sorted array
Pass 1: $[\ 1, 4, 7, 5, 2, 3\ ]$, $j = 0$
Pass 2: $[\ 1, 4, 7, 5, 2, 3\ ]$
Pass 3: $[\ 1, 4, 5, 7, 2, 3\ ]$
Pass 4: $[\ 1, 2, 4, 5, 7, 3\ ]$
Pass 5: $[\ 1, 2, 3, 4, 5, 7\ ]$

### Algorithm
#### Sort Function
```python
sort(A):
	Input: An array of size n
	Ouput: The sorted version of the array A
	
	for i = 1 to n - 1
		j = i - 1
		while A[i] < A[j]
			j = j - 1
			if j < 0
				break
		curr = A[i]
		k = i - 1
		while k >= j + 1
			A[k + 1] = A[k]
			k = k - 1
		A[j + 1] = curr
	
```

### Algorithm Analysis
#### Time Complexity
Just like the selection sort, here we see that the outer loop runs in the order of $n$ and the inner while loop is also running in the order of $n$
So the worst case time complexity is $\mathcal{O}(n^2)$
Best case time complexity (Where array is already sorted) is  $\mathcal{O}(n)$, since none of the loops are executed if the elements are sorted, so the order of $n$ operations that is contributed by them will not happen.

#### Space Complexity
Since no extra data structures were used, the space used is constant, so the space complexity in all cases is $\mathcal{O}(1)$


---
Tags: [[!DatastructuresAndAlgorithmsIndex]]