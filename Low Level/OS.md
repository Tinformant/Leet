### Buddy system
The buddy system guarantees that if one frees and then reallocates the same amount of storage, one will always get the __same__ memory back. This is because the freed block is linked at the __head/beginning__ of the appropriate free list.

## Scheduling & Queueing
Scheduling policies that seem fair may be unfair because processes ____block/suspend____ when they require input, thus giving up the rest of their ____time slice/allotment____.

The Completely Fair scheduler differs from round robin and O(1) in that the process that runs next is the one that has spent the ____least____ time running in recent history. By contrast, round-robin and O(1) determine who runs next from a ____queue/list/set____ of ready processes, where each one gets a time slice length based upon its ____priority____.

A scheduler is called ____fair____ if every process in the run queue receives the same amount of time. In O(1) scheduling, every process gets one time slice per ____epoch____. This is not considered ____fair____ because it does not compensate for time a process spends ____waiting/sleeping____ for other events. The ____completely fair____ scheduler gives such processes extra time.

The ____O(1)____ scheduler for linux minimizes computation at the expense of non-optimal ____fairness____. The main feature of this scheduler is that every process in the run queue gets a constant amount of runtime per ____epoch/slice____.

The problem with O(1) scheduling is that it is not fair, in the sense that a process that blocks waiting for I/O gets ____less____ CPU time than a process that does not.

The completely fair scheduler attempts to give each process in the run queue the ____same____ time per scheduling epoch, while in the O(1) scheduler, processes get differing times based upon how much ____I/O____ they perform.

An M/M/1 queue with arrival rate λ and processing rate μ is only in steady state if ____λ/μ____ < 1. Both 'M's in the above stand for ____memoryless____, which means that a previous arrival time or processing time does not affect the next.

An M/M/1 queue is a device where job arrivals and service times conform to ____memoryless/exponential____ statistical distributions. Since real service times are not ____memoryless____, the theory of M/M/1 queues rather consistently ____underestimates____ the average time in system for a request.

### Little's laws
* Assuming that the system is in __balance/equilibrium__ so that the ____input____ and output of the system occur at the same ____average____ rate. If λ is an arrival rate, then ____1/λ____ represents the corresponding time between arrivals. M/M/1 queues assume in addition that arrivals and processing have ____exponential/memoryless____ statistical distributions.
* average time in system
* average number of jobs waiting for completion
* average arrival rate
* arrival rate = average number of jobs waiting for completion / average time in system

Little's law relates arrival rate, time in system, and ____jobs in system____ for a queueing process. Little's law only requires that the system be ____in balance____. This is in contrast to all further results in queueing, which require some kind of assumption about the ____distribution____ of arrival times and/or service times.

If 20 people per hour arrive at a restaurant, and the same number of people leave every hour on average, and we observe that people stay an average of 2 hours, then there are ____40____ people on average inside the restaurant. This is only true because the system is in ____balance/steady state____ and because all values are ____averages____. 

If -- in addition -- there are always an average of 5 people waiting in line to be seated inside the restaurant , then the wait for seating is an average of ____1/4____ hour(s). λ=20/hour and L=5, so W=L/λ=5/20 = 1/4 hour.

Queueing theory is based upon the fundamental principle that the system under study is in balance, which means that the average ____input____ rate equals the average ____output____ rate.




(Extra credit) The translation lookaside buffer replaced the segment table on modern processors largely to save ____money____.

## Filesystem
If one device in linux is opened by two processes
* Different ____process____ file descriptors 
* same ____kernel____ file descriptor. 

If every process used a different one to write to the same file, then output could potentially be ____lost/overwritten____.

If two processes write to the same file descriptor at the same time, writes are done one at a time. To describe this situation, we say that "write is ____atomic____". We can force sections of code to be effectively ____atomic____ by surrounding each section with ____mutex locks____.

The fact that multiple processes share the same kernel descriptor for the same file means that output from the processes is appended to the file in ____time order/sequence____. If multiple processes write to independent kernel descriptors, then the content of the file is determined by the __last/latest__ process to close it.

### Inode
An inode of a file does not contain the file's ____name____. Instead, the file's ____name______ is contained in a ____directory____ that maps its inode number to its ____name____.

A file's identity is determined by its ____inode____, which contains information about its owner but not its ____name____. The latter is instead contained in the ____directory____ entry for the file.

Every file in a linux filesystem is described by an ____inode____ that describes the owner, group, protection, and location of blocks in the file. The location of the first few blocks of the file are recorded directly inside the inode, while subsequent blocks are located by ____indirection____ in which a block is re-interpreted as an array of ____pointers____ to blocks. Thus a file is logically a list but physically very similar to a(n) ____array____, in the sense that access to any block is O(1).

In a file system, a(n) ____inode____ documents the location of a file, while a(n) ____directory____ documents its name. In order to create a file one must initialize these and also mark the disk space required as ____used____. This is typically done through the use of ____bit/binary____ vectors.



