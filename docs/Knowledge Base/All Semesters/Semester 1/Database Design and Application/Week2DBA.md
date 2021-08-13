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

---

#### Entity Relationship Diagram
![[Pasted image 20210731175446.png]]
##### Entity in ER
![[Pasted image 20210731175517.png]]
##### Example of Entity
![[Pasted image 20210731175611.png]]
##### Attributes in ER
![[Pasted image 20210731175923.png]]

1. **Simple and composite**:
	1. Simple cannot be split, it is atomic
	2. Composite can be divided into smaller sub parts (It is a combination of simple  attributes example address)
2. **Single valued and multivalued**:
	1. Single valued means there is only one value for that column (Example name)
	2. Multivalued means there are more than one value for that column (Example Phone numbers)
3. **Stored attributes and Derived attribute**: 
	1. Attributes from which other attributes can be derived is a stored attribute (Example birth date, job join date) This will be stored in the DB
	2. Derived attribute are attributes that are derived from stored attributes (Example age from birth date, experience from job joining date) This value would not be stored in the DB
4. **Key Attributes**
	![[Pasted image 20210731181536.png]]

##### Relationship between the physical design to the conceptual design
1. Table -> Entity Type 
2. Row --> Entity/Tuple
3. Column --> Domain
4. Set of all rows --> Entity Set

##### Drawing attributes
![[Pasted image 20210731180930.png]]
flightid: Composite id and single valued
Rollno: key attribute since every STUDENT will have a unique value

![[Pasted image 20210731181903.png]]
![[Pasted image 20210731182249.png]]




---
Tags: [[!DatabaseDesignAndApplicationIndex]]