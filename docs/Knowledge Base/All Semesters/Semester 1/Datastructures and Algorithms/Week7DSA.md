# Week 7
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 11/Sep/2021

## Topics Covered
1. Counting Sort
	1. Steps Done
	2. Algorithm
		1. Sort Function
		2. Algorithm Analysis
			1. Space Complexity
			2. Time Complexity


## Counting Sort
### Steps Done
Let us say that we know that an input unsorted array has values that are within a given range. Then we maintain another array that keeps track of the frequency of the elements that occur in this list. We parse the array and whenever we come across the element we increment the frequency of that element by one.
```
Value:		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Frequency:	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

A:	{ 6, 1, 8, 3, 7, 2, 3, 9, 7 }
New_Frequency:	[0, 1, 1, 2, 0, 0, 1, 2, 1, 1]

Using the above newly calculated frequency array we can insert elements into the sorted array:
S:	{ 1, 2, 3, 3, 6, 7, 7, 8, 9 }

```

### Algorithm
#### Sort Function
```python
CountSort(int[] A, int n)
	Input: An array of integers of lenght n where the values in A are between [0, R - 1]
	Output: The sorted version of A

	int F[R]
	for i = 0 to (R - 1)
		F[i] = 0
		
	for i = 0 to (n - 1)
		tmp = A[i]
		F[tmp] += 1
	
	int S[n]
	int k = 0
	for i = 0 to (R - 1)
		freq = F[i]
		for j = 1 to freq
			S[k] = i
			k++
	return S
```

#### Algorithm Analysis
##### Space Complexity
Space complexity depends on the length of the frequency array, so it is: 
$\mathcal{O}(R)$

##### Time Complexity 
The time complexity is max of $\mathcal{O}(n)$ or $\mathcal{O}(R)$
= $\mathcal{O}(max(n, R))$
The total complexity for the last loop is: $\mathcal{O}(max(n, R))$


---
Tags: [[!DatastructuresAndAlgorithmsIndex]]