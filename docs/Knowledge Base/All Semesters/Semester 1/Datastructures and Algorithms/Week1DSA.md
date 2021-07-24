# Week 1 
Lecturer: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741)
Date: 24/Jul/2021
## Topics covered
1. What is an algorithm?
2. What is time and space complexity?


### What is an algorithm?
An algorithm is a sequence of steps to be followed to reach a pre determined goal for a predetermined set of inputs. An algorithm has the following properties:
1. **Finiteness**:  the sequence of steps the algorithm has must be finite
2. **Definiteness**: Each step should be atomic and precise and cause no confusion on what it does
3. **Input**: There may or may not be an input passed to the algorithm to work on
4. **Termination**: Due to the finiteness of algorithms the algorithm must terminate and produce an output
5. **Correctness**: The output produces must be the right one for any given input

### What is time and space complexity?
It is a way to analyze the performance of algorithms. Experimental studies for analyzing algorithms have some limitations:
1. It is difficult to compare running times of two algorithms in different software/hardware configurations
2. To truly know the performace we need to implement and run the algorithms on a computer since things like type of data provided for an algorithm can greatly alter the running time of the algorithm (For example an algorithm can run really slow for a single but large value and faster for mulitple values)
3. One must need to make sure that the set of inputs used to analyze the algorithms are representative, meaning that the inputs must cover some particular use case (say for a sorting algorithm, we can have one input where all values are already sorted, sorted in reverse, all values being same and all values being jumbled)

Consider the following example:
```
Algorithm arrayMax(A, n):
	Input: An array A storing n >= 1 integers.
	Output: The maximum element in A
	
	currentMax <- A[0]
	for i <- 1 to n - 1 do
		if currentMax < A[i] then
			currentMax <- A[i]
	return currentMax
```

The above example is what we call a ***pseudo code***. It is meant to represent the flow of logic to find the maximum value in a given array.

Consider A = [3, 2, 7, 5]

| Step i | What we are comparing it with | currentMax |
| ------ | ----------------------------- | ---------- |
| 0      | null                          | = A[0] = 3 |
| 1      | A[1] = 2                      | 3 > 2 so 3 |
| 2      | A[2] = 7                      | 3 < 7 so 7 |
| 3      | A[3] = 5                      | 7 > 5 so 7 |

So going over the steps we see that at the end we can determine that the max value is A[2] = 7. We see that:
> "Algorithm arrayMax runs in time proportional to n"
>> If we were to actually run experiments, then the running time of arrayMax given any input of size n would never exceed c.n where c is the amount of time taken by the given software to run for an input of size 1.

As seen above the constant c depends on the language used to run the algorithm and the hardware used to run the algoithm. A workstation can compute a more complex algorithm faster than a slow computer would for a less complex algorithm, hence to truly compare two algorithms all the parameters (The language, software and the hardware used) must be the same.

Given two algorithms has two implementations where:
1. **A algorithm**: that runs proportional to N and 
2. **B algorithm** that runs proportional to N<sup>2</sup>
we need to ideally makes sure that the algorithm chosen is the one that is proprtional to N since for a very large input A would perform better.

Addition, Multiplication, Subtraction and Division are exmaples of primitive operations. Primitive operation are those that cannot be further broken down to more simpler steps. For example given:

$$
CGPA = {(U_1G_1 + U_2G_2 + U_3G_3 + U_4G_4)\over(U1 + U2 + U3 + U4)}
$$
  
  adsf