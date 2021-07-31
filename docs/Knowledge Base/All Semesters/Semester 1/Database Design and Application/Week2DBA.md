# Week 2
**Lecturer**: Uma Maheswari, Faculty for BITS Pilani WILP
[![MailBadge](https://img.shields.io/badge/-umamaheswaris@wilp.bits--pilani.ac.in-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umamaheswaris@wilp.bits-pilani.ac.in)
**Date**: 31/Jul/2021

## Topics Covered
1. Intro to DBMS
2. Advantages of DBMS


### Mapping

Traditional
Multimedia dbs
Geographical (GIS)
Data warehouses (OLAP) (analyze useful business information from very large databses, support descision making)
Real time and active DB
Time series db (volatile stocks/financial data)

### Database design process
#### Database design phases
![[Pasted image 20210731174234.png]]
1. Requirements specification
	1. Produces data reqs and functional reqs
2. Conceptual design
	1. We develop an ER model or UML class diagram
	2. We describe different entities, their relation and their attributes
3. Logical design
	1. Based on the ER diagrams created, the designers create 
	2. Primary and foreign keys are determined
	3. Normalization is to eliminate redundancy and potential update anomalies.
4. Physical design
	1. This phase is to develop the database
	2. Decide the datatypes
	3. The SQL clauses are written to ccreate the DBs 

**Example**:
![[Pasted image 20210731174956.png]]
![[Pasted image 20210731175008.png]]

#### Conceptual database design
##### Domains, Atttributes, Tuples, and Relations
![[Pasted image 20210731175120.png]]

#### ER
![[Pasted image 20210731175446.png]]
Entity in ER
![[Pasted image 20210731175517.png]]
Example of Entity
![[Pasted image 20210731175611.png]]

Attribute in ER
![[Pasted image 20210731175923.png]]

Simple and composite
Simple cannot be split, it is atomic
Composite can be divided into smaller sub parts (It is a combination of simple  attributes ex address)
single valued
multivalued
derived attribute
stored attributes: attributes from which other attributes can be derived (eg birth date, job join date)

key -> is either a single or a combination of more attributes to get a key
![[Pasted image 20210731181536.png]]

foreign key -> 

Table -> Entity Type; Row --> Entity/Tuple: Column --> Domain ; Entity Set --> set of all rows

##### Drawing attributes
![[Pasted image 20210731180930.png]]
flightid: Composite id and single valued
Rollno: key attribute since every STUDENT will have a unique value

![[Pasted image 20210731181903.png]]
![[Pasted image 20210731182249.png]]

![[Pasted image 20210731182455.png]]