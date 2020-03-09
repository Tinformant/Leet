Process abstraction: represents running instances of applications e.g., ls, cat, Emacs, Safari

 ## A process's memory:
* code: compiled application code
* data: constants
* heap: memory allocated during execution
* stack: local variables, function parameters

## A process's registers:
 * PC: points to next instruction to execute on CPU
 * stack pointer: last used address on stack
 * General purpose: Stores data from memory for computation

Memory virtualization (a process's memory is virtual)
* Memory mapping: process vritual memory to physical memory (also belongs to a process)
* Isolates processes memory from one another, Gives processes illusion of having all of a machine's memory

## Virtual Mem Abstraction
### Transparent Virtualization
* No modification to guest OS
* High performance overhead
* Hypervisor emulates hardware for every VM
* Binary translation of OS request to HW
### Full Virtualization (modify guest OS so it knows it's virtualized)
* Minimal performance overhead
* Lots of OS modification
* Change virtual memory manager, context switching code, etc. in kernel to be aware of other virtual machines
### Para Virtualization
* Less performance overhead
* fewer of OS modification
* Find guest OS code that accesses shared resources and modify it in guest OS to call hypervisor
### HW-Assisted Virtualization
* Modify CPU: privileged instructions trap into hypervisor.
* Add more hardware structures for virtualization.
* + lowest performance overhead
* - no guest kernel modification

State that is maintained:
 
Num of processes that can concurrently execute on 1 CPU?
A: Only one

Num of CPUs a single process can concurrently run on?
A: Also one

## Context Swithcing
### Different Processes
* context switching: yes
* switch registers and page tables and pc
* states saved to process control blocks
### Threads within the same process
* context swithcing: yes
* States saved to thread control blocks
* context to switch: registers, PC (each thread has a PC)
* Address space doesn't change (same pagetable)
### System Call
* If a system call is blocking, it can cause context switching.
# Distributed Systems
Distributed service: =set of processes that coordinate to accomplish a common goal

Why distributed?
* scalability: can run processcess on different machines
* separation of concern

Dealing w/i failures:
1. detection
2. mitigation: replication
3. diagnosis

How to keep replications consistent?
1. Master-slave architecture
2. Consensus algorithm

Performance Metrics
* throughput
* latency

## Traffic Engineering
Flow groups: applications grouped together. High-priority applications grouped together. Low-priority applications grouped together.

## Bandwidth fns
How much bandwidth to allocate for each app or flow group (FG) based on priority.

## Encapsulation
Family of technologies to isolate tenants processes running on the same machine
* To ensure privacy/security of data
* To avoid performance & correctness interference
* To allow flexibility in choice of OS / libs / software

Encapsulation tech presents tenants w/ abstraction of access to an entire machine. In actuality, machine is shared among tenants



## ACID:
* Atomicity: Everything happens or nothing
* Consistency: If the database has rules they are obeyed at transaction end (e.g. balance must be < $1,000,000)
* Isolation: Any two parallel transactions act as if serial
* Durability: Once committed, never lost

## CAP
* Consistency: everyone agrees on the data 
* Availability: nobody ever has to stop processing 
* Partition tolerance: keep going even when the network partitions

## B4
* Centralized system for prioritizing high-priority traffic and increasing efficiency
* Necessary at large scale to avoid cost overruns
* Takes advantage of fact that a single entity (Google) controls everything: apps, switches, network.
* Allows for more optimization than possible when multiple parties are involved.

# GFS
Geared for big data and high throughput.

## Chunks: Unit of data, typically 64MB
• GFS operates on data at this granularity
• Clients can still read/write smaller amounts
* Chunk servers store individual chuncks
* con: small files (few chunks) may result in hot spots (many requests)

## Chunk Fault Tolerance

## GFS limitation
* Single metadata master is a bottleneck
* Many small files are a problem since each one requires accesses to the master

### GFS’s Master server (Directory structure location of file data on chunk) fault tolerance approach
* Replicate master on several machines; any replica can take over if primary Master fails
* How to keep mappings on replica consistent: primary master periodically checkpoints mappings with replicas
* Use journaling to preserve operations committed before checkpoints

## Concurrency
* GFS only guareentes order for concurrent updates for individual chunks

## Record Append
* Traditional write: the client specifies the offset at which data is to be written. Concurrent writes to the same region are not serializable: the region may end up containing data fragments from multiple clients.
* Record append: the client specifies only the data. GFS
appends it to the file at least once atomically (i.e., as one
continuous sequence of bytes) at an offset of GFS’s choosing
and returns that offset to the client.
## ACID
* GFS only has CD.

All systems must choose between consistency and availability at scale.
