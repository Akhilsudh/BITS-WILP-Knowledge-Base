# Pre Recorded Lecture Module 3

## Domain Model
- Illustrates meaningful conc3ets in a problem domain
- It is a representation of real world things, not software components
- It is a set of static structure diagrams; no operation are defined.
- It may show:
	- Concepts
	- Associations between concepts
	- Attribute of concepts
- Every domain concept has a name and a set of attributes

## Domain Model in UML
![[Pasted image 20220307110953.png]]
Reading direction by default is either top -> down or left -> right

### Domain Concepts in POS
#### Strategy to identify conceptual classes
- Use noun phrase identification
	- In textual descriptions of the problem domain and consider them as concepts or attributes
	- Use cases are excellent descriptions for this analysis

Consider the following scenario:
![[Pasted image 20220307111956.png]]
Customer, POS checkout, items, cashier, quantity, system, item price, item info, sale all these are nouns
![[Pasted image 20220307112111.png]]


item info, item price and quantity are all nouns that are attributes for the domain concept.
![[Pasted image 20220307112253.png]]

### Adding Associations
![[Pasted image 20220307121335.png]]
![[Pasted image 20220307121450.png]]
![[Pasted image 20220307121552.png]]

### Multiplicity
![[Pasted image 20220307121951.png]]
![[Pasted image 20220307124259.png]]

### Adding Attributes
![[Pasted image 20220307124837.png]]
![[Pasted image 20220307124953.png]]

### Sample Domain Model
![[Pasted image 20220307162409.png]]


## System Sequence Diagram
- Investigate the behaviour of the ysstem as a blackbox
- System behaviour is a description of what the system does
- Use cases describe how external actors interact with the system. During this interaction an actor generates events
- A request even initiates an operation upon the system

### SSD for Process Sale Scenario
![[Pasted image 20220307163816.png]]
![[Pasted image 20220307163504.png]]

### Significance of SSD
- Shows interaction of the system with the outside world
- It is used to depict how system responds to external events
- It plays key role in GUI design of the system

## Operation Contract
![[Pasted image 20220307220305.png]]

### Writing an OC for a sale line item
![[Pasted image 20220307220709.png]]

---
Tags: [[!OOADIndex]]