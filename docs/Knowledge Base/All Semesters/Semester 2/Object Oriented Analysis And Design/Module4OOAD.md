# Module 4
## Sequence Diagrams
### Example Code and its sequence diagram
```java
Public class A
{
	Private BB myB = new BB();
	Public void doOne()
	{
		myB.doTwo();
		myB.doThree();
	}
}
```
![[Pasted image 20220219112604.png]]

### Sequence diagram for payment system
![[Pasted image 20220219112756.png]]

### Sequence vs Communication
- UML tools usually emphasize sequence
- Easier to see call flow sequence—read from top to bottom
- Communication diagrams are more space-efficient
- Communication Diagrams expand top to bottom; Sequence Diagrams expand left to right

### Common Notation
![[Pasted image 20220219113601.png]]

### Singleton Objects
- Only one instance of the class instantiated at any time
![[Pasted image 20220219113642.png]]

### Lifeline Boxes
- Lifeline is a dashed line below the object that creates a shortlived object
![[Pasted image 20220219113913.png]]

### Messages
![[Pasted image 20220219114012.png]]

### Reply or Returns
- Use the message syntax `returnVar=Message(parameter)`
- Using a reply or return message at the end of an activation bar
![[Pasted image 20220219114112.png]]

### Messages to self
- We use a nested activation bar to satisfy this
![[Pasted image 20220219114225.png]]

### Condition and looping
![[Pasted image 20220219114555.png]]

### Other frame operators
![[Pasted image 20220219114621.png]]
![[Pasted image 20220219114630.png]]
![[Pasted image 20220219114640.png]]
![[Pasted image 20220219114655.png]]

![[Pasted image 20220219115002.png]]
![[Pasted image 20220219115015.png]]

### Relating interaction diagrams
- Interaction occurances is a reference to an interaction within another interaction
![[Pasted image 20220219115247.png]]

### Polymorphic Messages
![[Pasted image 20220219120028.png]]

## Communication Diagrams
- Connection path between objects. Navigation and visibility. Instance of an association.
- Multiple messages and messages both ways
![[Pasted image 20220219120156.png]]

### Creation of instances
![[Pasted image 20220219120615.png]]

### Sequencing
![[Pasted image 20220219120640.png]]

### Conditional Messages
![[Pasted image 20220219120714.png]]

### Mutually Exclusive Conditions
![[Pasted image 20220219120733.png]]

### Iterations
![[Pasted image 20220219120848.png]]
![[Pasted image 20220219120907.png]]

## Design Class Diagrams
- During analysis emphasize domain concepts
- During design shift to software artifacts
- UML has no explicit notation for DCDs
- Uniform UML notation supports smoother development from analysis to design

### Domain model vs design class diagram
![[Pasted image 20220226170306.png]]

### Developing DCD for POS DCD
![[Pasted image 20220226170525.png]]
![[Pasted image 20220226170535.png]]
![[Pasted image 20220226170742.png]]
![[Pasted image 20220226170915.png]]
![[Pasted image 20220226171125.png]]
![[Pasted image 20220226171246.png]]

### Adding dependencies:
![[Pasted image 20220226171440.png]]
An instance of product description is used by a method in the sale class making sale dependent on the product description.:
![[Pasted image 20220226171522.png]]

### Composition (Whole part) relationship
![[Pasted image 20220226171642.png]]
an aggregation is shown with a  hollow diamond instead of a fully coloured one.

### Association Classes
![[Pasted image 20220226171904.png]]
![[Pasted image 20220226172956.png]]

### Interfaces and template classes
![[Pasted image 20220226173051.png]]


---
Tags: [[!OOADIndex]]	