# Pre Reading for Week 7
**NOTE THAT THIS PAGE HAS DIAGRAMS THAT ARE BEST VISIBLE IN LIGHT MODE**

## Module 6
### What is a deadlock?
- One or more processes waiting indefinitely for resources to be released by other waiting processes
- Can occur on h/w or s/w resources, and is mostly seen in DBs (Lock and Unlock events in DBs)
   ![[Pasted image 20210909213541.png]]
   Here you can see as time goes on, $T_1$ locks on to resource $x$, once that is done, $T_2$ cannot access $x$ until it is unlocked, and similarly even $T_1$ has to wait for $T_2$ to unlock $y$, this is a deadlock since both have locked the resource each other needs to complete its tasks and are waiting indefinitely.
   
### Conditions for deadlock
#### Mutual Exclusion
If a resource is supposed to be used by more than one node in a DS, that resource cannot be shared across nodes, and the nodes must wait for the node using the resource to finish with its tasks, such a scenario is called mutual exclusion

#### Hold and Wait
![[Pasted image 20210909214047.png]]
In the above diagram, the assignment edge denotes the resource $x$ being held by the process $P_1$ and $P_1$ is waiting for the resource $y$ after requesting for it. Such a scenario is required to say that a process could be in a potential deadlock

#### No Preemption
For a deadlock to happen, one must not be able to take away a resource that is being used by a process. Only if a resource cannot be preempted from a process, the other proccess's request could potentially go into deadlock.

#### Circular Wait
![[Pasted image 20210909214448.png]]
Here you can see that two processes P_1 and P_2 are waiting for resouirces that each other holds back to complete its tasks. Such a situation most likely leads to deadlocks

### Ways to handle deadlocks
1. **Prevention**: 
	1. One can prevent a deadlock from happening by making sure that a resource is preemptive for example.
	2. One can also give all the necessary resources that a process requires in the beginning itself so that no two processes can request for each others locked resources.
2. **Avoidance**: 
	1. One can avoid deadlocks by making someone arbitrate a resource and make a judicious decision before giving a resource to a process
	2. Bankers algorithm: An algorithm that determines if it is safe or unsafe to give a resource to a process and try to find an optimal way of giving access to them to avoid a deadlock from happening.
	3. Avoidance usually incurs heavy overhead in a big DS and is even complex to build such systems
3. **Detection and Resolution**: 
	1. One can detect a cycle in a set of processes, and take a decision to kill a process inorder to resolve the deadlock. Only one process needs to be killed to resolve a deadlock, so decision can be taken based on some sort of priority
	2. The most practical solution for handling deadlocks in a DS
4. **Ignorance**

### Cycle Vs Knot
- The AND model of requests requires all resources currently being requested to be granted to unblobk a computation
	- A **cycle** is **sufficient** condition to declare a deadlock with this model
- The OR modelof requests allows a computation making multiple resource requests to unbock as soon as any one is granted
	- A **cycle** is **necessary** condition 
	- A **knot** is a **sufficient** condition. A knot is when a path is taken in an OR graph, there is no way out of that path leading to getting locked.

Consider the AND graph shown below:
![[Pasted image 20210909220100.png]]
We can say that the cycle is sufficient to say that the system is in deadlock

Consider the following OR graph shown below:
![[Pasted image 20210909220134.png]]
Here the cycle is not sufficient because P_1 can finish the process if it takes the other path out of this cycle

Now consider another OR graph shown below:
![[Pasted image 20210909220459.png]]
Here you can see that even the other path becomes a cycle to $P_1$ through $R_4$, such a situation is called as a knot


### Detection requirements
- Progress
	- All deadlocks found
	- Deadlocks found in finite time
- Safety
	- No false deadlock detection
	- Phantom deadlocks caused by network latenecies

### Chandy-Misra-Haas (CMH Edge-Chasing for AND Graphs)
- Some processes wait for local resources
- Some processes wait for resources on other machines
- Algorithm invoked when a process has to wait for a resource for a longer period
- Uses local WFGs (Wait For Graphs) to detect local deadlocks and probes to determine the existence of global deadlocks

![[Pasted image 20210909221545.png]]
$i$ the processor that is blocked and initiating the algo
$j$ The process sending the probe message
$k$ The receiver of the probe message

![[Pasted image 20210909221814.png]]
![[Pasted image 20210909222056.png]]

#### Example 1
![[Pasted image 20210909222209.png]]
- $P_1$ sends $(1, 1, 2)$
- $P_2$ sets $dependent$ is set to $TRUE$ and sends $(1, 2, 3)$
- $P_3$ sets $dependent$ is set to $TRUE$ and sends $(1, 3, 4)$
- $P_4$ sets $dependent$ is set to $TRUE$ and sends $(1, 4, 5)$ and $(1, 4, 6)$
-  $P_5$ sets $dependent$ is set to $TRUE$ and sends $(1, 5, 7)$
-  $P_6$ sets $dependent$ is set to $TRUE$ and sends $(1, 6, 8)$
-  Since $P_8$ is not dependent on anything it will finish using the resource that $P_6$ wants and release it. It will also not forward the probe message since it is not dependent on other processes
-  $P_7$ sets $dependent$ is set to $TRUE$ and sends $(1, 7, 9)$
-  $P_9$ sets $dependent$ is set to $TRUE$ and sends $(1, 9, 1)$
	-  Since $i == k$ in the last probe message, we can conclude that the system is in a deadlock
![[Pasted image 20210909222859.png]]

#### Example 2
![[Pasted image 20210909222921.png]]
- When the probe messages travel the path $P_1 \rightarrow P_2 \rightarrow P_3 \rightarrow P_4 \rightarrow P_5$, there is no apparent cycle seen
- Similarly when the probe messages travel the path $P_1 \rightarrow P_4 \rightarrow P_5$, there is no apparent cycle seen.
- But when the probe message takes the path $P_1 \rightarrow P_2 \rightarrow P_6 \rightarrow P_7 \rightarrow P_1$, we can see that there is a cycle so we can conclude that there is a deadlock situation in the WFG.

### Advantages of and Disadvantages of CMH algorithm
#### Advantages
1. Popular, variants of this are used in locking schemes
2. Easy to implement as each message is of fixed length and requires few computational steps
3. No graph constructing and information collection
4. False deadlocks are not detected
5. Does not require a particular structure among processes

#### Disadvantages
1. Two or more processes may independently detect the same deadlock and hence while resolving, several processes could potentially be aborted.
2. Even though a process detects a deadlock, it does not know the full cycle.
3. $M(n - 1)/2$ messages required to detect deadlock, where $M$ = no. of processes, $n$ = no. of sites.

### OR WFGs
Consider the following OR WFG:
![[Pasted image 20210910174728.png]]
In the above graph you can see that there is a cycle between $P_1$ and $P_2$, but since this is an OR WFG we can say that there is no deadlock since $P_1$ can take the resource $P_3$ has in its hold and still cater to $P_2$'s needs hence a cycle is not sufficient to determine deadlocks

Now consider the following OR WFG:
![[Pasted image 20210910175027.png]]
You can see that $P_1$ and $P_3$ also have a cyclic dependency, so that would mean that in an OR graph such a  system where no matter what path takes would lead to a  cycle will determine the potential of a deadlock. Such a situation is called a knot.


### Chandy-Misra-Haas (CMH Diffusion Computation for OR Graphs)

![[Pasted image 20210910175306.png]]

#### Example 1
![[Pasted image 20210910193019.png]]
If we apply the above algorithm, the messages being send from $P_1$ is all marked in red and the state of the wait and the state of variable number is updated based on the messages sent. When the message comes to $P_1$ finally, it will send a reply (Marked in Green) and the values of $n$ is decremented whenever a reply is received. A reply is sent back only if $n == 0$. If for some case the $n$ does not become $0$, then the reply is not sent, so since P_i is sending several non enage queries, these will end up getting replies from P_2 since its wait is true and since the number of sent messages is not equal to the number of received messages, there is no deadlock.
The below WFG is the result of applying this algorithm:
![[Pasted image 20210910193409.png]]

In the above example if we add an edge from $P_8 \rightarrow P_9$, then $P_4$ would also get a reply from $P_8$ and this will make its $n == 0$ and it will also send a reply back. This will go till $P_1$ and since all the sent messages from $P_1$ is replied to we can conclude that this system has a knot and it is in a deadlock state.

#### Example 2
![[Pasted image 20210910194225.png]]
In the above example the message sent from $P_1$ will never receive a reply from $P_2$ since there wont be a reply from $P_5$, even though the other path gives a reply to $P_2$. So this algorrithm makes sure that a cycle alone does not constitute a deadlock since there is another path that can be taken.

### Deadlock Persistence and Resolution
1. **Deadlock Persistence:** Average time a deadlock exists before it is resolved
2. **Deadlock Resolution:**
	1. Aborting at least one process/request involved in the deadlock
	2. Efficient resolution of deadlock requires knowledge of all processes and resources
	3. If every process detects a deadlock and tries to resolve it independently it is highly inefficient Several processes might be aborted

---
Tags: [[!DistributedComputingIndex]]