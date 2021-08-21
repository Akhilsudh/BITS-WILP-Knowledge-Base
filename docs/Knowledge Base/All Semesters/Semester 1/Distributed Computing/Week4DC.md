# Week 4

**Lecturer**: [Barsha Mitra](http://a.impartus.com/#/profile/1985732), BITS Pilani, Hyderabad Campus
[![MailBadge](https://img.shields.io/badge/-barsha.mitra@hyderabad.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:barsha.mitra@hyderabad.bits-pilani.ac.in)
**Date**: 21/Aug/2021

## Topics Covered
1. Singhal-Kshemakalyani's Differential Technique
2. Fowler-Zwaenepoel's Direct-Dependency Technique
3. Problems in recording global state
4. Some Key Concepts of Consistency and Channel State
5. Snapshot Recording Algorithms
	1. Chandy Lamport Algorithm (For FIFO)
	2. Lai and Yang algorithm (For NON-FIFO)

## Singhal-Kshemakalyani's Differential Technique
![[Pasted image 20210821143424.png]]
1. The message contains a list of tuples that follows the given syntax: $\{(index, val)\}$, where $index =$ Process that has the clock value of $= val$. 
2. We see that a process sends only the details of the clocks that are changed on that given process only.
3. This method considerably saves the amount of data that is sent between processed in the initial  timing

## Fowler-Zwaenepoel's Direct-Dependency Technique
![[Pasted image 20210821150854.png]]
1. Here we send only the local clock value of the process to the receiver
2. Dependency to other process that is directly not connected by messages is lost.
3. Direct dependence relationship is preserved

## Problems in recording global state
1. Lack of a globally shared memory
2. Lack of a global clock
3. Message transmission is asynchronous
4. message transfer delays are finite but unpredictable

## Some Key Concepts of Consistency and Channel State
![[Pasted image 20210821152647.png]]
![[Pasted image 20210821153229.png]]

## Snapshot Recording Algorithms
### Chandy Lamport Algorithm (For FIFO)
Process $p_i$ records its state
For each outgoing channel $C$ on which a marker has not been sent, $p_j$ sends a marker along $C$ before $p_i$ sends further messages along $C$

On receiving a marker along channel $C$:
if $p_j$ has not recorded its state then
Record the state of $C$ as empty set
Execute the "marker sending rule"
else
Record the state of $C$ as the set of messages received along $C$ after $p_j$ state was recorded and before $p_j$ received the marker along $C$

![[Pasted image 20210821154931.png]]

The vertical dashed lines are the amount of moneyt present between users A and B.
The arrow shows a transaction between A and B

Let $S1$ sends a marker to $S2$ through $C_{12}$ , so
	$S1$ => saves 450 as the local state
	$S2$ => Since it has not saved its local state, it will record the value of $C_{12}$ as empty and save the local state as 1030
	After it has recorded $S2$, Since S1 has already set its local state, it will store the 
	After $S1$ has recorded its local state

### Lai and Yang algorithm (For NON-FIFO)
1. Since markers cannot be used in NON FIFO channels we use piggybacking, so that messages sent after and before the marker are distinguished.
2. In Lai and Yang we use coloring scheme to do the piggy backing
3. every process is initially white
4. process turns red while taking a snapshot
5. equivalent of the "marker sending rule" is executed when a process turns red
6. Every message sent by a white process is colored white
	1. A white message is a message that was send before the sender of that message recorded its local snapshot
6. Every message sent by a red process is colored white
	1. A white message is a message that was send before the sender of that message recorded its local snapshot

![[Pasted image 20210821162034.png]]

![[Pasted image 20210821162250.png]]
$LS = 750$
All subsequent messages are red messages
$P2$ turns red when 10 is received, $P2$ will record the $LS$ as 190

$$C_{12} = white_message(20) + white_message(30) - white_message(20) = 30$$

$$C_{21} = white_message(30) - 0 = 30$$

---
Tags: [[!DistributedComputingIndex]]