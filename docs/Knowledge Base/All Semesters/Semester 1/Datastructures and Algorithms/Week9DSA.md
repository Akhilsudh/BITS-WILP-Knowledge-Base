# Week 9
**Lecturer**: [Pritam Bhattacharya](http://a.impartus.com/#/profile/3467741), BITS Pilani, Goa Campus
[![MailBadge](https://img.shields.io/badge/-pritamb@goa.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pritamb@goa.bits-pilani.ac.in)
**Date**: 16/Oct/2021

## Topics Covered
1. Abstract Data Types
	1. Stack
		1. Array Implementation
	2. Queue
		1. Array Implementation

## Abstract Data Types
It is a mathematical model for a data type, it is a container for how data is stored.

## Stack
A stack is a **Last In First Out (LIFO)** data structure, it supports the following operations, both at the same end:
1. `void push(<type> key)`: This operation adds a new value to the top of the stack
2. `<type> pop()`: This operation removes the top most element from the stack and returns it to the caller of this function
3. `int size()`: This operation returns the current size of the stack
4. `<Type> top()/peek()`: Returns the value of the top most value
5. `bool isEmpty()`: Returns True when the stack is empty
6. `bool isFull()`: Returns True when the stack is full

### Applications
1. Check for proper parenthesisation. To see the validity of parenthesis in an expression

### Array Implementation
The following is an implementation for `Stack<int>`:
```Python
class Stack {
	int stack[100];
	int top;
	
	Stack() {
		top = -1;
	}
	void push(int item) {
		if(isFull()) {
			print("Stack is full")
			return
		}
		stack[++top] = item
		return
	}
	int pop() {
		if(top != -1) {
			return stack[top--]
		}
		else {
			print("Stack is empty")
			return exception
		}
	}
	int size() {
		return top + 1
	}
	int top() {
		return stack[top]
	}
	bool isEmpty() {
		return (top == -1)
	}
	bool isFull() {
		return (top == stack.length - 1)
	}
}
```

## Queue
A queue is a **First In First Out (FIFO)** data structure, it supports the following operations, both at the same end:
1. `void enqueue(<type> key)`: This operation adds a new value to the rear end of the queue
2. `<type> dequeue()`: This operation removes the front most element from the queue and returns it to the caller of this function
3. `int size()`: This operation returns the current size of the queue
4. `<Type> front()/peek()`: Returns the value of the front most value
5. `bool isEmpty()`: Returns True when the queue is empty
6. `bool isFull()`: Returns True when the queue is full

### Applications
Simulating anything that needs a queue such as a ticket counters, message queues and any Distributed computing algorithm that uses a FIFO message channels and any buffer.

### Array Implementation
The following is an implementation for `Queue<int>`:
```Python
class Queue {
	int queue[100];
	int front;
	int rear;
	
	Queue() {
		rear = -1;
		front = 0;
	}
	void enqueue(int item) {
		if(isFull()) {
			return exception
		}
		rear = (rear + 1) % queue.length
		queue[rear] = item
	}
	int dequeue() {
		if(isEmpty()) {
			return exception
		}
		temp = queue[front]
		front = (front + 1) % queue.length
		return temp
	}
	int size() {
		size = rear - front + 1
		return (size >= 0) ? size : (size + queue.length) 
	}
	int peek() {
		return queue[front]
	}
	bool isEmpty() {
		return (size() == 0)
	}
	bool isFull() {
		return (size() == queue.length)
	}
}
```
 
---
Tags: [[!DatastructuresAndAlgorithmsIndex]]