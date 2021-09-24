# Module 3
## Global State Recording
### Uses of Global State Recording
- Recording a consistent state of the GS, checkpointing in fault tolerance (rollback/recovery)
- Detecting stable properties in a distributed system via snapshots. A property is stable if once it holds in a state, it holds in all subsequent states:
	- Termination detection
	- Deadlock detection

### Issues in recording GS
- How to distinguish between the messages to be recorded in the snapshot from those not to be recorded
	- Any message sent prior to recording must be recorded
	- Any message that is sent by a process after recording its snapshot must not be considered
- How to determine the instant when a process takes its snapshot
	- A process $p_i$ must record its snapshot before processing a message $m_{ij}$ that was sent by process $p_i$ after recording its snapshot

Note that since DS are non deterministic in nature so there need not be just one event happening at a given instant of time

## Chandy Lamport Algorithm (FIFO)
- Uses a **marker** whose purpose is to differentiate messages to be included in the snapshot and the ones to not be included
- After a snapshot is recorded, the marker is sent to all outgoing channels before any other message is processed
- Snapshot must be recorded no later than when it receives a marker  on any of its incoming channels
- When all the process have received a marker on all of its incoming channels it is terminated
- The algo can be initiated by a process by executing the marker sending rule by which it records its local state and sends a marker on each outgoing channel
- When a marker received a process can record its LS and then do the marker sending rule

### Examples

![[Pasted image 20210915222348.png]]
![[Pasted image 20210915222500.png]]
- Now consider the 50 sent by A reaches B and balance becomes 150
- B receives the Marker M
	- B records its state as 150
	- A recorded its state as 50
	- B sends marker to c_2 and c_3
- C receives marker from B
	- C records state as 200
	- C sends marker through c_4
- A receives two markers from B and C
	- Since A has recorded its LS
	- A checks if messages are there in c_2 and C_4
	- since they are empty, it marks the state of channel as empty
The global state of this system if we sum all the LS of the processes it looks like it is consistent

## Lai-Yang Algorithm (non-FIFO)
- Every process is initially white
- When a process decides to take a snapshot it becomes red
- Every process sent by a white/red process is colored white/red respectively
- Thus a white/red message is a message that was sent before/after the sender of that message recorded its local snapshot
- Every white process takes its snapshot at its convenience, but no later than the instant it receives a red message
- Every white process records a history of all white messages sent or received
- When a process turns red, it sends these histories along with its snapshot to the initiator process
- The initiator process evaluates transit ($LS_i$, $LS_j$) to compute the state of a channel $C_{ij}$ as given below:
	
	$SC_{ij}$ $=$ white messages sent by $P_i$ on $C_ij$ - white messages received by $P_j$ on $C_ij$


---
Tags: [[!DistributedComputingIndex]]