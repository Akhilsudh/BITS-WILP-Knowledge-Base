# Module 3
## Operation Contract
- Operation contract identifies system state changes when an operation happens.
- Define what each system operation does
- An operation is a single event from the system sequence diagram
- A domain model is used to help generate an operation contract
- When making an operation contract, think of the state of the system before the action and the state of the system after the action.
- The conditions both before and after the action should be described in the operation contract.
- The pre and post conditions describe state, not actions.

### Sections of an Operation Contract
- Operation: Name of the operation and parameters
- Cross references: Use cases and scenarios this operation can occur within
- Preconditions: Noteworthy assumptions about the state of the system or objects in the domain model before execution of the operation
- Postconditions: This is the most important section. The state of objects in the domain model after completion of the operation

## Example of operation contracts
### Main Success Scenario   
1. Customer arrives at POS checkout with goods and/or services to purchase.
2. Cashier starts a new sale.
3. Cashier enters item identifier.
4. System records sale line item and presents item description, price, and running total.
	1. Price calculated from a set of price rules.
	2. Cashier repeats steps 3-4 until indicates done.
5. System presents total with taxes calculated.
6. Cashier tells Customer the total, and asks for payment.
7. Customer pays and System handles payment.

### POS Domain Model
![[Pasted image 20220219105636.png]]

### Operation Contract for makeNewSale operation
- Operation: makeNewSale()
- Cross References:
	- Use case: Process sale
	- Scenario: Process sale
- Preconditions: none
- Postconditions:
	- a sale instance "s" was created (instance creation)
	- s was associated with the register    (association formed)
	- attributes of s were initialized
![[Pasted image 20220219105854.png]]

### Operation Contract for enterItem operation
- Operation: enterItem(itemID,quantity)
- Cross References:
	- Use Case: Process Sale
	- Scenario: Process Sale
- Preconditions: There is a sale underway.
- Postconditions:
	- A salesLineItem instance sli was created (instance creation)
	- sli was associated with the current Sale (association formed)
	- sli.quantity became quantity (attribute modification)
	- sli was associated with a ProductDescription, based on itemId match (association formed)
![[Pasted image 20220219111019.png]]

### Operation Contract for endSale operation
- Operation: endSale()
- Cross references:
	- Use case: Process sale
	- Scenario: Process sale
- Preconditions: There is a sale underway
- Postconditions:
	- s.isComplete became true (attribute modification)
![[Pasted image 20220219112130.png]]

### Operation Contract for makePayment operation
- Operation: makePayment(amount:Money)
- Cross References:
	- Use Case: Process Sale
	- Scenario: Process Sale
- Preconditions: There is a sale underway
- Postconditions
	-  a payment instance “p” was created (instance creation)
	-  p.amountTendered became amount (attribute modification)
	-  p was associated with s:Sale (association former)
	-  s:Sale was associated with the Store (association formed)
![[Pasted image 20220219112327.png]]




---
Tags: [[!OOADIndex]]	