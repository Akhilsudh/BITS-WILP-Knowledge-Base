# Week 11
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 30/Oct/2021


## Linked List
![[Pasted image 20211030084656.png]]
The linked list has a node where the node has a data and a pointer component that points to the next node (can be a node or null if it ends in this node)
```C
struct Node {
	int data
	struct Node* next
}
```
### ADT Operations
1. `first()` -> This function returns the head of the linked list
	```C
	first() {
		return head;
	}
	```
1. `last()` -> This function returns the last element of the linked list
	```C
	last() {
		if(head == NULL) {
			return NULL
		}
		struct Node* temp = head
		while(temp -> next != NULL) {
			temp = temp -> next
		}
		return temp
	}
	```
2. `before(p)` -> This function returns the previous node to a given node p
	```C
	before(struct Node* p) {
		if(p == head || p == NULL) {
			return NULL
		}
		struct Node* curr = head
		while(curr -> next != p) {
			curr = curr -> next
		}
		return curr
	}
	```
3. `after(p)` -> This function returns the next node
	```C
	after(struct Node * p) {
		if(p == NULL) {
			return NULL
		}
		return p -> next
	}
	```
4. `insertBefore(p, key)` -> Insert a node before p with the key value
	```C
	insertBefore(struct Node* p, int key) {
		if(head == NULL || p == NULL) {
			return ERROR
		}
		struct Node* newNode;
		newNode -> data = key
		newNode -> next = pos
		struct node* curr = head
		while(curr -> next != p && curr -> next != NULL) {
			curr = curr -> next
		}
		if(curr -> next == NULL) {
			return ERROR
		}
		curr -> next = newNode
	}
	```
5. `insertAfter(p, key)` -> Insert a node with value key to a position after p
	```
	insertAfter(struct Node* p, int key) {
		if(p == NULL) {
			return ERROR
		}
		struct Node* newNode
		newNode -> data = key
		newNode -> next = p -> next
		p -> next = newNode
	}
	```
6. `remove(p)` -> remove the node from the linked list
	```
	remove(struct Node* p){
		if(p == NULL || head == NULL) {
			return NULL
		}
		struct Node* curr = head
		while(curr -> next != p && curr -> next != NULL) {
			curr = curr -> next
		}
		if(curr -> next == NULL) {
			return NULL
		}
		curr -> next = p -> next
		return p
	}
	```

## Double Linked list
In a doubly linked list the Node contains the next node as well as the previous node as well along with the data. The struct would look somthing like this:
```C
struct Node {
	int data
	struct Node* next
	struct Node* prev
}
```
 The ADT functions can now utilize the previous pointer for reference in operations such as insert before and insert after and one must also make sure to correctly set the previous and next pointers as well.
 
---
Tags: [[!DatastructuresAndAlgorithmsIndex]]