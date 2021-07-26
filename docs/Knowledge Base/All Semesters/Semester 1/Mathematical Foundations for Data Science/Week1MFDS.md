# Week 1 
**Lecturer**: [Barsha Mitra](http://a.impartus.com/#/profile/1985732), CSIS Dept, BITS Pilani, Hyederabad Campus
[![MailBadge](https://img.shields.io/badge/-barsha.mitra@hyderabad.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:barsha.mitra@hyderabad.bits-pilani.ac.in)
**Date**: 25/Jul/2021

**NOTE THAT THIS PAGE HAS DIAGRAMS THAT ARE BEST VIEWED IN LIGHT MODE**

## Topics covered
1. Matrices and their types
2. REF and RREF
3. Rank, its computation and properties
4. Determinent, it's computation and properties
5. Consistency and inconsistency of linear systems
6. Modelling using linear equations
7. Vector and matrix norms

### Matrices and their types
A rectangular array of numbers or functions enclosed in brrackets are considered as matrices (Matrix for singular). All of the following are valid matrices: 
$$
A = \begin{bmatrix}a & b & c & d\\e & f & g & h\end{bmatrix},
B = \begin{bmatrix}a & b & c\\d & e & f\\g & h & i\end{bmatrix},
C = \begin{bmatrix}a\\b\\c\end{bmatrix},
D = \begin{bmatrix}a & b & c\end{bmatrix}
$$
Each element within the matrix (```a```, ```b```, ```c``` etc) are called entities
Each matrix has a size that is represented as ```n x m``` where n is the number of rows and m is the number of columns. In the above example the array ```A``` has a **size** of ```2 x 4```

out of the last two matrices in the above example the matrix ```C``` is what we call a column matrix and ```D``` is called a row matrix. The other word for it is column/row Vector and Vectors are usually denoted with lower case characcters  like this:
$$
a = \begin{bmatrix}1\\2\\3\end{bmatrix},
b = \begin{bmatrix}4 & 5 & 6\end{bmatrix}
$$

Two matrices are equal if both have the same size (same number of rows and columns) and every element in one matrix matches with every element in the other (including their positions)

#### Matrix operations
- **Addition**: Two matrices can be added if both the matrices have the **same size**. The addition is merely adding the same values that have the same position on both matrices. Consider the following example
   $$
	\begin{aligned}
	A = \begin{bmatrix}1 & 2 & 3 & 4\\5 & 6 & 7 & 8\end{bmatrix},
	B = \begin{bmatrix}9 & 10 & 11 & 12\\13 & 14 & 15 & 16\end{bmatrix} \\ \\
	C = A + B = \begin{bmatrix}1 & 2 & 3 & 4\\5 & 6 & 7 & 8\end{bmatrix} + \begin{bmatrix}9 & 10 & 11 & 12\\13 & 14 & 15 & 16\end{bmatrix} \\ \\ 
	C = \begin{bmatrix}1 + 9 & 2 + 10 & 3 + 11 & 4 + 12\\5 + 13 & 6 + 14 & 7 + 15 & 8 + 16\end{bmatrix} \\ \\
	C = \begin{bmatrix}10 & 12 & 14 & 16\\18 & 20 & 22 & 24\end{bmatrix}
	\end{aligned}
  $$
  Addition adhere to the following rules:
  1. $$ A + B = B + A $$
  2. $$ (A + B) + C = A + (B + C) $$
  3. $$ A + 0 = A $$
  4. $$ A + (-A) = 0 $$

