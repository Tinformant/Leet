### Buddy system
The buddy system guarantees that if one frees and then reallocates the same amount of storage, one will always get the __same__ memory back. This is because the freed block is linked at the __head/beginning__ of the appropriate free list.

## Scheduling
A scheduler is called ____fair____ if every process in the run queue receives the same amount of time. 

### O(1) Scheduler
In O(1) scheduling, every process gets one time slice per ____epoch____. This is not considered ____fair____ because it does not compensate for time a process spends ____waiting/sleeping____ for other events.

The ____O(1)____ scheduler for linux minimizes computation at the expense of non-optimal ____fairness____. The main feature of this scheduler is that every process in the run queue gets a constant amount of runtime per ____epoch/slice____.

O(1) scheduling is unfair: a process that blocks waiting for I/O gets ____less____ CPU time than a process that does not.

### Completely Fair Scheduler
The ____completely fair____ scheduler gives such processes extra time. Scheduling policies that seem fair may be unfair because processes ____block/suspend____ when they require input, thus giving up the rest of their ____time slice/allotment____.

Completely fair scheduling tries to ensure fairness by storing the run queue as a red-black tree of processes whose search key is the ____time____ for which the process has executed so far. At each scheduling step, the process with the ____least/leftmost____ key is executed, and then moved to where it then belongs in the tree.

The completely fair scheduler attempts to give each process in the run queue the ____same____ time per scheduling epoch, while in the O(1) scheduler, processes get differing times based upon how much ____I/O____ they perform.

The Completely Fair scheduler differs from round robin and O(1) in that the process that runs next is the one that has spent the ____least____ time running in recent history. By contrast, round-robin and O(1) determine who runs next from a ____queue/list/set____ of ready processes, where each one gets a time slice length based upon its ____priority____.

## Queueing
### M/M/1
An M/M/1 queue with arrival rate λ and processing rate μ is only in steady state if ____λ/μ____ < 1. 
* M = Memoryless
* 1st M: independent previous arrival time
* 2nd M: independent processing time

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

## Virtual Memory
### Page
____Page____ can mean
1. how ____virtual/process____ memory is managed.
2. how disk files are ____read/written____.

(EXTRA CREDIT ) In allocating a new block for a file, the filesystem driver first looks for blocks whose "used" descriptors are currently located in the ____page table cache____, to increase performance.

Although linux continues to use segment descriptors internally, modern processors use ____page____ descriptors for the same purpose. Very efficient data structures are required in the OS so that ____page faults____ can be processed as quickly as possible. Each ____page____ can be read/write or ____read-only____.

The disk subsystem and the virtual memory subsystem both use the concept of ____paging____ things to and from memory, but the disk subsystem uses ____kernel____ memory while the virtual memory subsystem utilizes ____process____ memory.

The Ext2 filesystem and its derivatives only function properly because of the ____paging_____ subsystem for the raw disk device.

A page of memory in a process maps to a ____frame____ of memory in the operating system.
The function malloc allocates one ____page/frame____ of memory at a time from the operating system, and then packages it for your use. On average, a call to malloc returns ____more____ memory than you requested. The justification for this apparent waste is that as a result, malloc and free can run in ____constant/O(1)____ time.

A memory page/block that has been changed since it was read from disk virtual memory is called ____dirty____ and must be ____flushed/written____ to the disk before the memory can be reused.

Virtual memory and file paging use the same strategy to deal with the situation in which the page cache is ____full____; the cache entry that was ____least recently used/accessed____ is reused to cache a new page. If a page is ____dirty____ it is written to disk first.

The translation lookaside buffer maps from ____logical/process/page____ memory addresses to ____physical/frame____ memory addresses. This mapping associates what we call ______pages____ in the process with what we call ____frames____ in the operating system.

The structure of a modern linux filesystem is largely based upon the existence of the ____paging____ system; crucial structures are updated quickly because they are always in ____memory____.

Modern memory addressing uses ____hashing____ to represent sparse maps, and ____caching____ to represent dense maps. Segments are utilized to decrease the amount of information one must store about each memory ____frame/page____.

The ____LRU____ reclamation strategy is commonly used to recover pages in the disk page table. This has one weakness; it does not deal efficiently with ____(long) loops____.

### Fragmentation
memory is broken up into segments with gaps between them; must find a "fragment" big enough for each use. 
* Internal fragmentation: processes must allocate more memory than needed.
* External fragmentation: unused memory lies in small fragments in the global memory map, between processes

From the point of view of a process, memory fragmentation of the frame table is called ____external____ fragmentation, while fragmentation due to malloc is called ____internal____ fragmentation. From the operating system's point of view, fragmentation of the frame table is ____internal____.




## Filesystem
If one device in linux is opened by two processes
* Different ____process____ file descriptors 
* same ____kernel____ file descriptor. 

If every process used a different one to write to the same file, then output could potentially be ____lost/overwritten____.

If two processes write to the same file descriptor at the same time, writes are done one at a time. To describe this situation, we say that "write is ____atomic____". We can force sections of code to be effectively ____atomic____ by surrounding each section with ____mutex locks____.

The fact that multiple processes share the same kernel descriptor for the same file means that output from the processes is appended to the file in ____time order/sequence____. If multiple processes write to independent kernel descriptors, then the content of the file is determined by the __last/latest__ process to close it.

### Inode
Every file in a linux filesystem is described by an ____inode____ that describes the owner, group, protection, and location of blocks in the file. Inode of a file does not contain the file's ____name____. Instead, the file's ____name______ is contained in a ____directory____ that maps its inode number to its ____name____.

The location of the first few blocks of the file are recorded directly inside the inode, while subsequent blocks are located by ____indirection____ in which a block is re-interpreted as an array of ____pointers____ to blocks. Thus a file is logically a list but physically very similar to a(n) ____array____, in the sense that access to any block is O(1).

In order to create a file one must initialize these and also mark the disk space required as ____used____. This is typically done through the use of ____bit/binary____ vectors.


### I/O
There are two kinds of buffering associated with I/O: one kind in the ____process____ and another in the ____kernel/IO subsystem____. The one in the ____kernel/IO subsystem____ allows one to write character output to ____block____ devices. The one in the ____process____ calls one write for several printf calls.

The I/O subsystem is a concatenation of multiple producer-consumer systems. For example. in writing to the raw disk, the producer is ____running processes____, while the consumer is the ____disk scheduler/update____.

### Disk
One reason that disk update is lazy is that it is ____faster/more efficient____ to make many disk changes in a batch rather than individually. The reason for this is that batch updates require less ____seek____ time during the update.

In linux, devices can be
1. block devices: only write and read large chunks of data.
2. character devices:  that can write one character at a time. A character can only be written to a block device by ____reading the destination block____ first.

The structure of a linux filesystem is based upon a contractual arrangement between the ____filesystem driver____ and the ____pager____. The former determines the structure of disk, while the latter makes disk updates ____more efficient____.

## Hashes
Inside an operating system, most structures are ____arrays____. Dense ones are sometimes ____cached____, while sparse ones are sometimes ____hashed____.

Correspondences can be implemented as:  
* Arrays (if small)  
* Hashes (if sparse and large)  
* Caches (if dense and large) 

