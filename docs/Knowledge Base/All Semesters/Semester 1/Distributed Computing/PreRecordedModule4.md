# Module 4
## Birman Schiper Stephenson BSS Protocol
- This algorithm works with broadcasting messages
- Before broadcasting $m$, process $P_i$ increments vector time $VT_{pi}[i]$ and timestamps $m$
- Other processes receives this $VT_m$ from $P_i$
- The process delays the receive till the following two conditions are met:
	- $VT_{Pj}[i] = VT_m[i] - 1$, this means $P_j$ received all other messages from $P_i$
	- $VT_{Pj}[k] >= VT_m[k]$ for every $k \in \{1, 2, ... n\} = \{i\}$, meaning $P_j$ received all messages also received by $P_i$ before sending message $m$.
- When $P_j$ delivers $m$, $VT_{Pj}$ updated by IR2 of Vector clock

### Example 1
![[Pasted image 20210916225719.png]]
- $P_2$ receives $m_2$ first with a $VT = (2, 0)$
	- At $P_2$ the $VT = (0, 0)$ and $(0, 0) \ne (2, 0) - (1, 0)$
	- Since this rule is not satisfied, $m_2$ is kept in queue
- $P_2$ receives $m_1$ now with a $VT = (1, 0)$
	- At $P_2$  the $VT$ is still $(0, 0)$, and the first condition check satisfies since $(0, 0) = (1, 0) - (1, 0)$
	- Also second rule is satisfied as well.
	- Since the rule is satisfied, $m_1$ is received, and $VT_2$ is updated to $(1, 0)$
- $P_2$ now checks condition for the message $m_2$ in queue. Now since the $VT$ at $P_2$ is $(1, 0)$, the two rules are satisfied, and the message $m_2$ is now received. and the $VT$ is updated to $max(VT_2, VT_1) = (2, 0)$

### Example 2
![[Pasted image 20210916230830.png]]
- $P_1$ sends message to $P_2$ and $P_3$ with $VT_1 = (1, 0, 0)$
- $P_2$ has $VT_2 = (0, 0, 0)$
	- $P_2$ receives message from $P_1$
		- $VT_1 = (1, 0, 0)$ satisfies the first condition
		- It also satisfies the second condition
		- This message is received by $P_2$ and $VT_2 = (1, 0, 0)$
	- $P_2$ receives another message from $P_1$
		- $VT_1 = (2, 0, 0)$ satisfies the first condition
		- It also satisfies the second condition
		- This message is received by $P_2$ and $VT_2 = (2, 0, 0)$
- $P_3$ has $VT_3 = (0, 0, 0)$
	- $P_3$ receives message from $P_1$
		- $VT_1 = (2, 0, 0)$ does not satisfy the first condition
		- This message $m_{2P1}$ is kept in queue
		- $VT_3 = (0, 0, 0)$
	- $P_3$ receives message from $P_2$
		- $VT_1 = (2, 1, 0)$ satisfies the first condition
		- But it does not satisfy the second one because the 2 messages from $i$ are not yet received
		- This message $m_{1P2}$ is kept in queue
		- $VT_3 = (0, 0, 0)$
	- $P_3$ receives message from $P_1$
		- $VT_1 = (1, 0, 0)$ satisfies the first condition
		- It also satisfies the second condition
		- Since both are satisfied, $VT_3 = (1, 0, 0)$
	- Since $VT_3$ is $(1, 0, 0)$
		- The message $m_{2P1}$ with $VT_1 = (2, 0, 0)$, satisfies the first condition and the second condition
		- Now this message is marked received and updates the $VT_3$ to $(2, 0, 0)$
	- Since $VT_3$ is $(2 0, 0)$
		- The message $m_{1P2}$ with $VT_2 = (2, 1, 0)$, satisfies the first condition and the second condition
		- Now this message is marked received and updates the $VT_3$ to $(2, 1, 0)$
- $P_1$ has $VT_1 = (2, 0, 0)$
	- $P_1$ receives message from $P_2$
		- This message has $VT_2 = (2, 1, 0)$
		- This VT satisfies the first condition
		- This VT also satisfies the second one as well
		- This message is marked as received and $VT_1$ is updated to $(2, 1, 0)$

## Schiper-Eggli-Sandoz SES protocol
- There is no need for broadcast messages
- Each process maintains a vector $V_P$ of size $N - 1$, $N$ being the number of processes in the system
- $V_P$ is a vector of tuple $(P' , t)$: $P'$ is the destination process id and $t$ is the vector timestamp
- $T_m$: logical time of sending message $m$
- $T_{Pi}$: present logical time at $P_i$
- Initially $V_P$ is empty

![[Pasted image 20210916233533.png]]

### Example 1
![[Pasted image 20210917011333.png]]
- $P_1$ sends $m_1$ with $(1, 0)\{\}$ to $P_2$
	- $VP_1 = \{(P_2, 10)\}$
- $P_1$ sends $m_2$ with $(2, 0)\{(P_2, 10)\}$ to $P_2$
	- $VP_1 = \{(P_2, 20)\}$
- $P_2$ receives message $m_2$ from $P_1$ containing $(2, 0)\{(P_2, 10)\}$
	- Since $VP_1$ has a tuple for $P_2$, and since the clock value is greater than the local clock, the message is buffered
- $P_2$ receives message $m_1$ from $P_1$ containing $(1, 0)\{\}$
	- Since the $VP_1$ does not have a tuple for $P_2$ the message is received
	- And after receiving we apply IR2 to get $T_2$ to be $(1, 0)$ and then apply IR1 to get $(1, 1)$
- The buffered message is now considered for receiving
	- Since the tuple has $t_m = (1, 0)$, the $T_2$ becomes $(2, 1)$ after IR2 and then $(2, 2)$ after IR1

### Example 2
![[Pasted image 20210918001535.png]]
- $P_1$ sends $m_{13}$ with $(1, 0, 0)\{\}$
- $P_1$ sends $m_{12}$ with $(2, 0, 0)\{(P_3, 100)\}$
- $P_2$ receives message from $P_1$, since the vector does not have an entry for P_2 the message is delivered and the local clock becomes $max(000, 200) + 010 = 200 + 010 = 210$ and $VP_2$ now has $\{(P_3, 100)\}$
- $P_2$ sends a message to $P_3$ with  $(2, 2, 0)\{(P_3, 100)\}$ data
- $P_3$ receives message from $P_2$
	- since the vector has entry for $P_3$ and the clock is higher than local clock it is **buffered**
- $P_3$ receives message from $P_1$
	- Since vector is empty the message is received
	- The local clock of $P_3$ becomes $max(000, 100) + 001 = 101$
- $P_3$ receives buffered message
	- Since 101 is greater than 100 the message is received
	- Now the local time becomes $max(101, 220) + 001 = 222$

![[Pasted image 20210918003729.png]]

---
Tags: [[!DistributedComputingIndex]]