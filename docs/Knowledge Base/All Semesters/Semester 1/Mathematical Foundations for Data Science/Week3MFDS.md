# Week 3
**Lecturer**: G Venkiteswaran, Faculty for BITS Pilani
[![MailBadge](https://img.shields.io/badge/-gvenki@pilani.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gvenki@pilani.bits-pilani.ac.in)
**Date**: 08/Aug/2021

## Topics Covered


## Gauss Elimination Analysis (cont.)

A time analysis of the algorithm for different size of inputs is shown below:

| Algorithm         | n = 1000 | n = 10000 |
| ----------------- | -------- | --------- |
| Elimination       | 0.7 s    | 11 min    |
| Back substitution | 0.001 s  | 0.1 s     |

### Corollary

Doolittle L
Crout Method U
Cholesky's Method $U = L^T$ when A is symmetric and positive definite
- A is written as $A = U^T U$. Hence we may have $U^T Ux = b$

![[Pasted image 20210808110951.png]]

![[Pasted image 20210808112226.png]]

![[Pasted image 20210808115605.png]]

## Iterative methods
### Gauss Jacobi
1. Computations for each element can be done in parallel since each step independent
3. Convergence is generally faster than Jacobi method


### Gauss Seidel
1. The gauss seidel method can be applied to any matrix with non zero elements on diagonal, but convergence is not guaranteed
2. Computations for each element cannot be done in parallel since each step depends on the previous calculation
3. Convergence is generally faster than Jacobi method

![[Pasted image 20210808115631.png]]


---
Tags: [[!MathematicalFoundationsIndex]]