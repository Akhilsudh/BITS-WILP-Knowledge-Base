# Week 9

**Lecturer**: [Barsha Mitra](http://a.impartus.com/#/profile/1985732), BITS Pilani, Hyderabad Campus
[![MailBadge](https://img.shields.io/badge/-barsha.mitra@hyderabad.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:barsha.mitra@hyderabad.bits-pilani.ac.in)
**Date**: 24/Oct/2021

## Byzantine Agreement Problem
### Assumptions made
![[Pasted image 20211024145410.png]]

![[Pasted image 20211024143823.png]]
![[Pasted image 20211024143909.png]]
![[Pasted image 20211024143944.png]]
$n = 4$
$f = 1$
![[Pasted image 20211024145433.png]]

## Byzantine Agreement Tree Algorithm: Recursive Formulae
![[Pasted image 20211024145934.png]]

## Peer to Peer Network
![[Pasted image 20211024153845.png]]
![[Pasted image 20211024154037.png]]

### Well known P2P networks
- Napster
- Gnutella
- Freenet
- Pastry
- Chord
- CAN

### Introduction to P2P networks
- P2p networks allow the location of arbitrary data objects
- impose a low cost for scalability, and for entry into an exit from the network
- Ongoing entry and exit of various nodes and dynamic insertion and deletion of objects is termed as **churn**
- Impact of churn should be as transparent as possible


### Data Indexing and Overlays
#### Centralized Indexing:
- Use of one or a few central servers to store references to the data on many peers
- Napster uses centralized indexing

#### Local Indexing
- Requires each peer to index only the local data objects
- Remote objects need to be searched for
- Used in unstructured overlays
- Gnutella uses local indexing

Disctributed Indexing
- Involves the indexes to the objects at various peers being scattered across other peers throughoput the P2P network
- Disctributed indexing is the most challenging of the indexing schemes
- Many novel mechanisms have been proposed, most notably the disctributed hash table (DHT)

#### Structured Overlays
![[Pasted image 20211024155827.png]]

#### Unstructured Overlays
![[Pasted image 20211024160139.png]]

### Chord Distributed Hash Table: Overview
![[Pasted image 20211024160347.png]]
![[Pasted image 20211024160931.png]]
![[Pasted image 20211024161020.png]]

![[Pasted image 20211024161548.png]]
#### Simple Lookup
![[Pasted image 20211024162540.png]]


---
Tags: [[!DistributedComputingIndex]]