 Week 8

**Lecturer**: [Barsha Mitra](http://a.impartus.com/#/profile/1985732), BITS Pilani, Hyderabad Campus
[![MailBadge](https://img.shields.io/badge/-barsha.mitra@hyderabad.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:barsha.mitra@hyderabad.bits-pilani.ac.in)
**Date**: 16/Oct/2021

## Topics Covered
1. Chandy Misra Haas Algorithm for the OR model
	1. Steps
	2. Examples
	3. Performance Analysis
2. Deadlock Resolution

## Chandy Misra Haas Algorithm for the OR model
- 2 types of messages are used:
	- $query(i, j, k)$
	- $reply(i, j, k)$
	- Denote that they belong to a deadlock detection initiated by $P_i$ and are being sent from $P_j$ to $P_k$
- A blocked process initiates deadlock detection by sending query messages to all processes in its dependent set $DEPEN$
- Local variable $num_k(i)$ = number of query messages sent
- $P_k$ maintains a boolean variable $wait_k(i)$
- $wait_k(i)$ denotes that $P_k$ has been continuously blocked since it received the last engaging query $P_i$

![[Pasted image 20211016145012.png]]

### Steps
![[Pasted image 20211016145647.png]]
![[Pasted image 20211016150057.png]]

### Examples
$B$ sends first message
![[Pasted image 20211016150853.png]]

$C$ sends query message after getting query from $B$
![[Pasted image 20211016151021.png]]

$F$ sends query message after getting query from $B$
![[Pasted image 20211016151200.png]]

$E$ sends query message after getting query from $C$
![[Pasted image 20211016151254.png]]
The message sent by $E$ is **non engaging** for $F$ so $F$ sends a $reply$ to $E$

$D$ sends a query to $E$ after getting query from $C$
![[Pasted image 20211016151438.png]]
The message sent by $D$ is **non engaging** for $E$ so $E$ sends a $reply$ to $D$

$A$ sends a query to $B$ after getting query from $F$
![[Pasted image 20211016151725.png]]
Since the query message from $A$ is received by $B$ who initiated the algorithm, hence $B$ sends out a reply

The reply path looks like this:
![[Pasted image 20211016153006.png]]
Since $B$ received all replies and $num_B = 0$ the node B declares deadlock

### Performance Analysis
- For every deadlock detection, the algorithm exchanges $e$ query messages and $e$ reply messages, where $e = n(n - 1)$
- $e$ is the number of edges, $n$ is the number of processes

## Deadlock Resolution
- Deadlock reslutions involves breaking exisiting wait-for dependencies between processes
- Rolling back one or more deadlocked processes
- Assigning resources of rolled back processes to blocked processes
- Blocked processes resume execution
- When a wait-for dependency is broken
	- Corresponding information should be immediately cleaned from the system
- Otherwise may result in detection of phantom deadlocks

## Agreement Problem
- Agreement among processes in a distributed system
- Processes need to exchange information to negotiate with one another and eventually reach a common understanding or agreement, before taking actions

**Failure Models**:
- Among the $n$ processes in the system, at most $f$ processes can be faulty
- Faulty process can behave in any manner allowed by the failure model assumed
- Various processor failure models - From recorded lecture

**Synchronous/Asynchronous communication**:
- If a failure prone processes chooses to send a message to process $P_i$ but fails, then $P_i$ cannot detect the non arrival of the messages in an asynchronous system
- Scenario is indistinguishable from the scenario in which the message takes a very long time to travel
- Impossible to reach a consensus in an asynchronous system.
- In a synchronous system, a message that has not been sent can be recognized by the intended recipient, at the end of the round
- The intended recipient can deal with the non arrival of the expected message by assuming the arrival of a message containing some default data, and then proceeding with the next round of the algorithm

**Network Connectivity**:
- System has full connectivity, i.e., each process can communicate with any other by direct message passing

**Sender Identification**:
- A process receiving a message always knows identity of sender process
- Also true for malicious senders

**Channel Reliability**:
- Channels are reliable
- Only the processes may fail (Under one of the various failure models)

**Agreement Variable**:
- May be boolean or multi valued
- Need not be an integer

**Non authenticated messages**:
- With such messages, when a faulty process relays a message to other processes
	- It can forge the message and claim that it was received from another process
	- It can also tamper with the contents of a received messages before relaying it
- Receiver cannot verify its authenticity
- Unauthenticated message is also called oral message or unsigned message

### Byzantine Agreement Problem
![[Pasted image 20211016161233.png]]
- Requires a designated process, called the **source process**, with an initial value, to reach agreement with the other processes about its initial value, subject to the following conditions:
	- **Agreement:** All non faulty process must agree on the same value
	- **Validity:** If the source process is non-faulty, then the agreed upon value by all the non-faulty processes must be the same as the initial value of the source
	- **Termination:** Each non faulty process must eventually decide on a value.
- If the source process is faulty, then the correct processes can agree upon any default value
- Irrelevant what the faulty processes agree upon - or whether they terminate and agree upon anything at all

## Consensus Problem
- It is initiated by all processes
- **Agreement:** All non faulty processes must agree on the same (single) value
- **Validity:**
	- If all the non-faulty processes have the same initial value, then the agreed upon value by all the non-faulty processes must be that same value
	- If non-faulty processes broadcast different initial values, then these processes should decide upon a common value
- **Termination:** Each non-faulty process must eventually decide on a value

## INteractive Consistency Problem
- Initiated by all processes
- **Agreement:** All non faulty processes must agree on the same array of values
- **Validity:**
	- If process $P_i$ is non faulty and its initial value is $V_i$ then all non faulty processes agree on $V_i$ as the $i^{th}$ element of the array $A$
	- If $P_j$ is faulty, then the non faulty processes can agree on any value for $A[j]$
- **Termination:** each non faulty process must agree on some value for $A[]$

## Upper Bound on Byzantine Processes
In a system of n processes, this problem can be solved in a synchronous system only fo the number of Byzantine processes f is such that 

$f \le floor((n - 1)/3)$


---
Tags: [[!DistributedComputingIndex]]