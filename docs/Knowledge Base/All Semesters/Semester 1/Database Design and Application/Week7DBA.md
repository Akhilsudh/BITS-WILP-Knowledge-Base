# Week 7
**Lecturer**: Uma Maheswari, Faculty for BITS Pilani WILP
[![MailBadge](https://img.shields.io/badge/-umamaheswaris@wilp.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umamaheswaris@wilp.bits-pilani.ac.in)
**Date**: 4/Sep/2021

## Topics Covered
1. Query Languages
2. Relational Algebra
	1. SELECT Operation
	2. PROJECT Operation
	3. TYPE COMPATIBILITY
	4. UNION Operation
	5. INTERSECTION Operation
	6. SET DIFFERENCE Operation
	7. Some properties for UNION, INTERSECTION and SET DIFFERENCE operations
	8. CARTESIAN (Cross Product) Operation
	9. RENAME Operation
	10. JOIN Operation
	11. OUTER UNION Operation
	12. Complete Set of Relational Operations
	13. DIVISION Operation
	14. Aggregate Functions and Grouping Operation
3. Tutorial Session
4. Post Lecture Notes


## Query Languages
![[Pasted image 20210904164609.png]]
	- **Procedural:** 			What to do and how to do
	- **Non Procedural:** 	What to do


## Relational Algebra

[REFERENCE LECTURE](http://www.cbcb.umd.edu/confcour/Spring2014/CMSC424/Relational_algebra.pdf)

![[Pasted image 20210904164759.png]]

Consider the example schema
![[Pasted image 20210904164858.png]]
Which is populated with these data
![[Pasted image 20210904164906.png]]

- The basic set of operations for the relational model is known as the relational algebra
- These operations enable a user to specify basic retrieval requests
- The reult of a retreival is a new relation, which may have been formed from on or more relations.
- A sequence of relational algebra operations forms a relational algebra expression, whose result will also be a relation

### SELECT Operation
Select operation is used to select a subset of the tuples from a relation that satisfy a selection condition. The select operation is denoted by a *sigma*  letter

$\sigma_{DNO} = 4 (EMPLOYEE)$ (This represents all employees in department 4)
$\sigma_{SALARY} \gt 30000 (EMPLOYEE)$ (This represents all employees in with salary greater than 30000)

#### Properties
- SELECT is commutative 
- A cascade SEKLEECT operation may be applied in any order
  $\sigma_{<condition\ 1>}(\sigma_{<condition\ 2>}(R))$ $=$ $\sigma_{<condition\ 2>}(\sigma_{<condition\ 1>}(R))$
- A cascade SELECT operation can be 
  $\sigma_{<condition\ 1>}(\sigma_{<condition\ 2>}(\sigma_{<condition\ 3>}(R)))$ $=$ $\sigma_{<condition\ 2>}(\sigma_{<condition\ 3>}(\sigma_{<condition\ 1>}(R)))$
- A cascade can also be written as:
   $\sigma_{<condition\ 1>}(\sigma_{<condition\ 2>}(\sigma_{<condition\ 3>}(R)))$ $=$ $\sigma_{<condition\ 1>}(\sigma_{<condition\ 2>}(\sigma_{<condition\ 3>}(R)))$

#### Example
![[Pasted image 20210904165747.png]]

### PROJECT Operation
This operation selects certain columns from the table and discards the rest. This is shown as the *pi* letter

$\pi_{LNAME,\ FNAME,\ SALARY}(EMPLOYEE)$

#### Properties
- The number iof tuples in the result of projection $\pi_{<list>}(R)$ is always less or equal to the number of tuples in R
- If the list of attributes 
	
####  Example
![[Pasted image 20210904170101.png]]
![[Pasted image 20210904170133.png]]

Combination of SELECT and PROJECT
![[Pasted image 20210904170208.png]]


### TYPE COMPATIBILITY
- The operand relations must have the same number of attributes and the domains of the corresponding attributes must be compatible

### UNION Operation
Denoted as $R \cup S$, means that all the tuples of $R$ and $S$ will be accumulated together and any duplicates are thrown away 

#### Example
![[Pasted image 20210904170342.png]]
![[Pasted image 20210904170429.png]]
![[Pasted image 20210904170608.png]]

### INTERSECTION Operation
Denoted as $R \cap S$, means that common tuples of $R$ and $S$ will be accumulated together and others are thrown away 

#### Examples
Consider the same example as the UNION operation, then intersection is:
![[Pasted image 20210904170742.png]]

![[Pasted image 20210904170812.png]]
![[Pasted image 20210904170831.png]]

### SET DIFFERENCE Operation
- The result of this operation denoted by $R - S$ is a relation that includes all tuples that are in $R$ but not in $S$
- Here order matters, meaning $R - S$ need not be the same as $S - R$


#### Examples
![[Pasted image 20210904171006.png]]
![[Pasted image 20210904171032.png]]

### Some properties for UNION, INTERSECTION and SET DIFFERENCE operations
$R \cup S = S \cup R$
$R \cap S = S \cap R$


### CARTESIAN (Cross Product) Operation
Cartesian product combines each and every row of the two relations. It is denoted by $R x S$

#### Examples
![[Pasted image 20210904171311.png]]
![[Pasted image 20210904171518.png]]



![[Pasted image 20210904171633.png]]

### RENAME Operation
- Name conflicts can arise in some situations
![[Pasted image 20210904171752.png]]

#### Examples
![[Pasted image 20210904171815.png]]
![[Pasted image 20210904171833.png]]


### JOIN Operation
Sequence of CARTESIAN Operation followed by a SELECT

#### Types of JOIN Operations
![[Pasted image 20210904172202.png]]

##### Conditional Join
![[Pasted image 20210904172219.png]]
In the employee example the condition is $EMPLOYEE.EMP\_CODE = SALARY.EMP\_CODE$

##### Natural Join
denoted as $*$
![[Pasted image 20210904172608.png]]
Join such that the tuples are equal on all the common attribute names

![[Pasted image 20210904173017.png]]
![[Pasted image 20210904173021.png]]

A Complete Example:
![[Pasted image 20210904174819.png]]

##### Equi Join
A join where the only comparison operator used is $=$. In the result of an EQUIJOIN we always have one or more pairs
![[Pasted image 20210904173156.png]]


##### THETA Join
Apart from $=$ all the other comparison operators are also used

##### OUTER Join
- Left Outer Join: Keeps every tuple in the first/left relation $R$; if no matching tuple is found in $S$, then attributes of $S$ are given null values
   ![[Pasted image 20210904180741.png]]
- Right Outer Join: Keeps every tuple in the second/right relation $S$; if no matching tuple is found in $R$, then attributes of $R$ are given null values
   
- Full outer join: Keeps every tuple in both the relations $R$ and $S$ and the rest are padded with $null$ 


### OUTER UNION Operation
![[Pasted image 20210904181147.png]]

--- 

### Complete Set of Relational Operations
![[Pasted image 20210904175142.png]]

### DIVISION Operation
denoted by $\div$ 
![[Pasted image 20210904180026.png]]
#### Examples
![[Pasted image 20210904175239.png]]
![[Pasted image 20210904175412.png]]

Another example
![[Pasted image 20210904175800.png]]

### Aggregate Functions and Grouping Operation
![[Pasted image 20210904180042.png]]
![[Pasted image 20210904180214.png]]
![[Pasted image 20210904180306.png]]

---

## Tutorial Session
![[Pasted image 20210904181514.png]]
![[Pasted image 20210904182239.png]]
![[Pasted image 20210904182350.png]]


## Post Lecture Notes
- Go through the SQL slides for the next week
- Go through the example problems in the book for relational algebra

---
Tags: [[!DatabaseDesignAndApplicationIndex]]