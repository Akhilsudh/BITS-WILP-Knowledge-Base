# Week 9
**Lecturer**: Uma Maheswari, Faculty for BITS Pilani WILP
[![MailBadge](https://img.shields.io/badge/-umamaheswaris@wilp.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umamaheswaris@wilp.bits-pilani.ac.in)
**Date**: 16/Oct/2021

## Topics Covered

## Normalization or Logical Design
### Functional Dependencies
![[Pasted image 20211016163703.png]]
Here you can see that the $roll_no$ is a functional dependency because it can be used to get other values

### Key Terms
![[Pasted image 20211016163921.png]]

### Armstrong's axioms/properties of functional dependencies
![[Pasted image 20211016164036.png]]

### Functional Dependency
![[Pasted image 20211016164243.png]]

#### Multivalued Functional Dependency
![[Pasted image 20211016164300.png]]

#### Trivial Functional Dependency
![[Pasted image 20211016164311.png]]

#### Non Trivial Functional Dependency
![[Pasted image 20211016164355.png]]

#### Transitive Functional Dependency
![[Pasted image 20211016164511.png]]

### Keys
#### Primary Keys
![[Pasted image 20211016164543.png]]
#### Foreign Keys
![[Pasted image 20211016164641.png]]
Foreign Keys help in maintaining the **Referential Integrity** between tables

#### Compound Keys
![[Pasted image 20211016164743.png]]

#### Composite Keys
![[Pasted image 20211016164823.png]]

#### Surrogate Key
![[Pasted image 20211016164930.png]]
The DBMS automatically creates a surrogate key

## Normalization
![[Pasted image 20211016165028.png]]

### Tutorial
![[Pasted image 20211016165051.png]]
![[Pasted image 20211016165420.png]]

### Normal Forms
![[Pasted image 20211016165448.png]]
![[Pasted image 20211016165539.png]]

#### 1NF
In a functional dependency if the RHS has only one attribute then it is in 1NF
![[Pasted image 20211016165605.png]]
Another way to do this is as follows:

**Employee Details:**

| EMP_ID | EMP_NAME | EMP_STATE |
| ------ | -------- | --------- |
|        |          |           |

**Employee Phone Numbers:**

| EMP_ID | PH_NO |
| ------ | ----- |
|        |       |

![[Pasted image 20211016170019.png]]

#### 2NF
![[Pasted image 20211016170051.png]]
![[Pasted image 20211016170423.png]]
![[Pasted image 20211016165953.png]]

#### 3NF
![[Pasted image 20211016170503.png]]
![[Pasted image 20211016170542.png]]

#### Summary of 1, 2, 3 NF
![[Pasted image 20211016170753.png]]

#### BCNF
![[Pasted image 20211016170830.png]]
![[Pasted image 20211016171003.png]]

#### 4NF
![[Pasted image 20211016171103.png]]
![[Pasted image 20211016171232.png]]
![[Pasted image 20211016171323.png]]

#### 5NF
![[Pasted image 20211016171413.png]]
![[Pasted image 20211016171554.png]]
![[Pasted image 20211016171613.png]]

#### Spurious Tuples
![[Pasted image 20211016171637.png]]
![[Pasted image 20211016171646.png]]

#### Lossless Decomposition
![[Pasted image 20211016171721.png]]
![[Pasted image 20211016171738.png]]
![[Pasted image 20211016171803.png]]


## Extraneous Attributes
### Example 1
$R(A, B, C)$
$F: \{A \rightarrow B, B \rightarrow C\}$
Since:
1. $A^+ \implies \{A, B, C\}$, hence we can say that $A$ is a $CK$
2. $B^+ \implies \{B, C\}$, since all other attributes cannot be derived, $B$ cannot be a $CK$
3. $C^+ \implies \{C\}$, since all other attributes cannot be derived, $C$ cannot be a $CK$

### Example 2
$R(A, B, C, D, E)$
$F: \{A \rightarrow D, BC \rightarrow A, BC \rightarrow D, C \rightarrow B, E \rightarrow A, E \rightarrow D\}$

$B^+ \implies \{B\}$
$C^+ \implies \{C, B, A, D\}$

Since C covers all attributes we can remove the extraneous attributes from:
$BC \rightarrow A, BC \rightarrow D$ to $C \rightarrow A, C \rightarrow D$

## Canonical/Minimal Cover Problem
1. RHS must be singleton
2. Extraneous attributes must be resolved
3. Remove redundant FD

### Example
$R(A, B, C)$
$F: \{A \rightarrow B, AB \rightarrow C\}$
1. Both relations have a singleton RHS
2. The second one has extraneous attributes
$A^+ \implies \{ABC\}$
$B^+ \implies \{B\}$
Since A covers B we can reduce the second relation to: $A \rightarrow C$

so the minimal cover is:
$F: \{A \rightarrow B, A \rightarrow C\}$

### Example
$R(A, B, C, D)$
$F: \{A \rightarrow B, AB \rightarrow C, D \rightarrow AC, D \rightarrow E\}$
Does $F$ cover $G$?
$G: \{A \rightarrow BC, D \rightarrow AB\}$

#### For $F$
1. Decomposing to singleton relations:
$A \rightarrow B$
$AB \rightarrow C$
$D \rightarrow A$
$D \rightarrow C$

2. Resolve Extraneous attributes:
$AB \rightarrow C$
$A^+ \implies \{ABC\}$
$B^+ \implies \{B\}$

new $F$: 
$\{A \rightarrow B, A \rightarrow C, D \rightarrow A, D \rightarrow C, D \rightarrow E\}$

3. Redundant FD
Since the dependency $D \rightarrow C$ is not needed we can drop that dependency

Final $F$:
$\{A \rightarrow B, A \rightarrow C, D \rightarrow A, D \rightarrow E\}$

#### For $G$

## Normalization Problems
![[Pasted image 20211016181246.png]]
![[Pasted image 20211016182014.png]]
![[Pasted image 20211016182448.png]]
![[Pasted image 20211016183004.png]]


---
Tags: [[!DatabaseDesignAndApplicationIndex]]