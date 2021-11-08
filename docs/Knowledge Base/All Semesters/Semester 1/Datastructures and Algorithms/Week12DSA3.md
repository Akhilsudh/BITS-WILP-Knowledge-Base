# Week 12 (cont.)
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 5/Nov/2021

## Hashing
Example for the hashing function taken $h(k) = k\ \%\ 7$

### Finding an array
```Python
find(x) {
	pos = x % 7
	if(T[pos] == x) {
		return True
	}
	else {
		return False
	}
}
```

### Insert to an array
```Python
insert(x) {
	pos = x % 7
	if(T[pos] = EMPTY) {
		T[pos] = x
	}
	else {
		# Handle Collision
	}
}
```

## Open Addressing Hashing
![[Pasted image 20211105211412.png]]
### Finding in open addressing
```Python
find(x) {
	pos = x % 7
	currNode = T[pos]
	while(currNode != NULL) {
		if(currNode -> data == x) {
			return True
		}
		curNode = currNode -> next
	}
	return False
}
```

### Insertion in open addressing
```Python
insert(x) {
	pos = x % 7
	struct Node* newNode
	newNode -> data = x
	newNode -> next = NULL
	if(T[pos] == NULL) {
		T[pos] = newNode
	}
	else {
		currNode = T[pos]
		while(currNode -> next != NULL) {
			currNode = currNode -> next
		}
		currNode -> next = newNode
	}
}
```
 
## Linear Probing
When a collision is reached, what we end up doing is if there is a collision, we find the next hash value as so:

$h(k, 0) = k\ \%\ 7$
$h(k, 1) = (h(k) + 1 )\ \%\ 7$
$...$
$h(k, n) = (h(k) + n )\ \%\ 7$

### Insertion
```Python
insert(k) {
	i = 0
	pos = ((k % 7) + i) % 7
	while(T[pos] != EMPTY) {
		i += 1
		pos = ((k % 7) + i) % 7
		if(pos == k % 7) {
			return "ERROR! HASHTABLE IS FULL"
		}
	}
	T[pos] = k
}
```

### Finding
```Python
insert(k) {
	i = 0
	pos = ((k % 7) + i) % 7
	while(T[pos] != k) {
		i += 1
		pos = ((k % 7) + i) % 7
		if(T[pos] == EMPTY || pos == k % 7) {
			return "NOT FOUND IN HASHTABLE"
		}
	}
	return pos
}
```


---
Tags: [[!DatastructuresAndAlgorithmsIndex]]