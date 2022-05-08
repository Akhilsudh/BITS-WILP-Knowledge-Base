# Module 6
## Architectural Patterns
### Properties of patterns
- Addresses a recurring design problem that arises in specific design situations and presents a solution to it
- Document existing well proven design experience
- Identify and specify abstractions at the high level
- Helps to build complex systems
- Manage software complexity

A set of guidelines that help to get a good design are:
1. Avoid rigidity (Hard to change)
2. Avoid Fragility (Whenever the design changes, it should not break)
3. Avoid Immobility (Cannot be reused)

### OO Design Principles

- **Open Close:**
	- Open to extension and close for modification
	- Template and strategy pattern

- **Dependency Inversion:**
	- Decouple two module dependencies
	- Adapter pattern

- **Liskov's Substitution:** Superclass can be replaced by subclass

- **Interface Segregation:** Interfaces are made only for a particular purpose

- **Single responsibilies:** One class for only one task

### Three part schema for a pattern
![[Pasted image 20220507214941.png]]

### Context
- A scenario or situation where design problem arises
- Ideally the scenario should be generic but it might not always be possible
- Example
	- Developing messaging solution for mobile applications
	- Developing software for a man machine interface

### Problem
- Start with a problem statement that captures the theme
- Completed by forces
	- A requirement
	- A constraint
	- A desirable property
- The forces can complement or contradict. This can be used to choose what force needs to be taken into consideration and what should not be

### Solution
- It is a configuration to balance the forces mentioned earlier
	- Like structure with components and relationships
	- Run time behavior
- Structure: Addresses static part of the solution
- Run time: Behavior while running

![[Pasted image 20220507215508.png]]

### Problem Categories
![[Pasted image 20220507215735.png]]

![[Pasted image 20220507215838.png]]

![[Pasted image 20220507220305.png]]

### Layering Pattern
![[Pasted image 20220507220803.png]]

#### Example
![[Pasted image 20220507220954.png]]

#### Layers
- Services of Layer J are only used by Layer J + 1
- No further direct dependencies between layers
- Each layer can have many components
![[Pasted image 20220507221903.png]]

![[Pasted image 20220507222601.png]]


The following is used to define the layer abstraction criteria
- Most generic components are in the lowest layer and domain specific components are in the top layer
- More stable components are in lower layers.
- Distance from hardware is also used in determining the layers

![[Pasted image 20220507222913.png]]

#### Construction of layer
- Use black box approach to specify layer interface
- Structure each layer
	- Identify components in each layer
	- Bridge or strategy pattern can help

![[Pasted image 20220507230739.png]]

#### Examples
![[Pasted image 20220507230903.png]]

#### Summary
![[Pasted image 20220507231009.png]]

### Pipe and Filter Pattern
#### Filter
- Has interfaces from which a set of inputs flow in and set of outputs flow out
- Processing step is in a filter component
- Independent entities
- Does not share state with other filters

#### Pipes
- Data is passed through pipes between adjacent filters
- Stateless data stream
- Source end feeds filter input and sink receives output

#### 3 Part schema
![[Pasted image 20220507231438.png]]

#### A simple case
![[Pasted image 20220507231629.png]]

- Passive Filters
![[Pasted image 20220507232741.png]]
- Active Filters
![[Pasted image 20220507232811.png]]
- Buffered Pipe for synchronizing
![[Pasted image 20220507233106.png]]

#### Components of Pipe and Filter
![[Pasted image 20220507232726.png]]

#### Implementation Steps
![[Pasted image 20220507233151.png]]
![[Pasted image 20220507233219.png]]
![[Pasted image 20220507233258.png]]

#### Pros and Cons
- No intermediate files necessary
- Filter addition replacement and reuse
- Rapid prototyping
- Concurrent execution
- Certain analysis possible like deadlock Throughput and latency checks

- Data transformation overhead
- Error handling is a challenge
- Sharing state is expensive
- Lowest common denominator on data transmission determines the overall throughput

#### Examples
- Most PaaS providers have message oriented service orchestration
- Azure has queing services
- Amazon SQS is used to communicate between EC2 instances

### Blackboard Pattern
| Title   | Details                                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------------------- |
| Context | A set of heterogeneous specialized modules which dynamically change their strategies as a response to unpredictable events |
| Problem | When there is no deterministic solutions to process                                                                        |
|         | Solutions to partial problems require representation                                                                       |
|         | No predetermined strat is present to solve a problem                                                                       |
|         | Dealing with uncertain knowledge                                                                                           |
| Forces  | A complete search of solution is not possible                                                                              |
|         | Different algos used for partial solutions                                                                                 |
|         | One algorithm uses results of another algo                                                                                 |
|         | No strict sequence between algos                                                                                           |


#### Examples
- Speech recognition
- Vehicle Identification
- Robot Control
- Modern Machine Learning algos for complex task
- OCR based text recognition

#### Components
- Central data structures
- Control plan encapsulates information necessary to run the system
- Domain KS are concerned with the solving of domain specific problems
- Control KS adapt the current control plan to the current situation

![[Pasted image 20220508001542.png]]

#### Pros and cons
![[Pasted image 20220508002510.png]]

### Distributed System Patterns
| Title   | Description                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| Context | Complex environment of systems to take advantage of computing power via clusters                                   |
|         | A software may be available only on a specific computer                                                            |
|         | Due security we might have to run different parts in different systems                                             |
|         | Some services are provided by business partners over internet                                                      |
| Problem | To build a sw system as a set of decoupled interoperating components rather than a monolith                        |
|         | Require a flexible means of interprocess communication                                                             |
| Forces  | It should be possible to distribute components during deployment                                                   |
|         | Need to exchange add or remove components at run time                                                              |
|         | Architecture should hide system specific and implementation specific details from users of components and services |

### Broker Pattern
A broker component helps in achieving better decoupling of clients and servers
- Servers: Register themselves with the broker and make their services available
- Clients: access the functionality of servers by sending requests via the broker

**The broker:**
- Locating the appropriate server and forwarding a request to that server
- Transmitting results and exceptions back to the client

![[Pasted image 20220508011116.png]]

#### Implementation
- Define an object model or use an existing one
- Decide which kind of component interoperability the system should offer
- Specify the APIs the broker component provides for collaborating
- Use proxy objects to hide implementation details from clients and servers
- Design the broker component in parallel with steps 3 and 
- Develop IDL compilers

#### CORBA
- CORBA is the oldest amongst the middleware technologies used in today's IT world
- CORBA stands for Common Object Request Broker Architecture
- CORBA supports Dynamic Invocation Interface (DII)

#### Remote Method Invocation
- Sun's Java RMI is based on the transparent Broker variant pattern
- Client side proxy and server side invoker have to be created manually by am additional compilation step
- The service interface is written in Java
- RMI is limited to usage in Java
- To establish interoperability RMI IIOP is provided

#### Benefits
- Location independence
- Type system transparency (Marshaling and unmarshaling are done)
- Isolation
- Separation of concern
- Resource management
- Portability

#### Liability
- Error handling
- Overhead since developers  do not know about the location of objects
- Performance
- Lower fault tolerance (server / broker failures)

### Model View Controller
![[Pasted image 20220508153720.png]]
![[Pasted image 20220508153516.png]]
![[Pasted image 20220508153624.png]]

![[Pasted image 20220508153741.png]]
![[Pasted image 20220508153855.png]]

#### MVC Dynamics
![[Pasted image 20220508153923.png]]

#### MVC Initialization
![[Pasted image 20220508154026.png]]

#### AJAX application as MVC
![[Pasted image 20220508160140.png]]

#### Benefits
- Multiple views can be done for the same model
- Synchronized views
- Pluggable views and controllers
- Exchangeability of look and feel
- Framework potential

#### Liabilities
- Increased complexity
- Potential execssive number of updates
- Inefficiency of data access in view
- Difficulty of using MVC with modern user interface tools

---
Tags: [[!SoftwareArchitecturesIndex]]
