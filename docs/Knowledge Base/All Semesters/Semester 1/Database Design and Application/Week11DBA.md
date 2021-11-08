# Week 11
**Lecturer**: Uma Maheswari, Faculty for BITS Pilani WILP
[![MailBadge](https://img.shields.io/badge/-umamaheswaris@wilp.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umamaheswaris@wilp.bits-pilani.ac.in)
**Date**: 30Oct/2021

## 2PL
### Basic
All locks are obtained in growth phase and during shrinking phase all the unlocks are done

### Conservative
All locks are obtained before any transactions and all are unlocked after transactions

### Strict
Exclusive locks are unlocked after a commit, shared locks 

### Rigourous
All locks are unlocked after a commit

## Problems on Locking
![[Pasted image 20211030165450.png]]
Basic 2PL

![[Pasted image 20211030165651.png]]
Strict 2PL

![[Pasted image 20211030165939.png]]
No growth or shrinking phase so not in 2PL

## Deadlock
![[Pasted image 20211030170624.png]]

### Problems
![[Pasted image 20211030170706.png]]
No deadlocks

![[Pasted image 20211030171056.png]]
Deadlock happens because the two processes are waiting for each other

---
Tags: [[!DatabaseDesignAndApplicationIndex]]