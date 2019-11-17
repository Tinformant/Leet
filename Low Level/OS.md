### Little's laws
* Assuming that the system is in ____balance/equilibrium____ so that the ____input____ and output of the system occur at the same ____average____ rate. If λ is an arrival rate, then ____1/λ____ represents the corresponding time between arrivals. M/M/1 queues assume in addition that arrivals and processing have ____exponential/memoryless____ statistical distributions.
* average time in system
* average number of jobs waiting for completion
* average arrival rate
* arrival rate = average number of jobs waiting for completion / average time in system

Little's law relates arrival rate, time in system, and ____jobs in system____ for a queueing process. Little's law only requires that the system be ____in balance____. This is in contrast to all further results in queueing, which require some kind of assumption about the ____distribution____ of arrival times and/or service times.

If 20 people per hour arrive at a restaurant, and the same number of people leave every hour on average, and we observe that people stay an average of 2 hours, then there are ____40____ people on average inside the restaurant. This is only true because the system is in ____balance/steady state____ and because all values are ____averages____. 

If -- in addition -- there are always an average of 5 people waiting in line to be seated inside the restaurant , then the wait for seating is an average of ____1/4____ hour(s). λ=20/hour and L=5, so W=L/λ=5/20 = 1/4 hour.

Queueing theory is based upon the fundamental principle that the system under study is in balance, which means that the average ____input____ rate equals the average ____output____ rate.

## Scheduling
Scheduling policies that seem fair may be unfair because processes ____block/suspend____ when they require input, thus giving up the rest of their ____time slice/allotment____.

The Completely Fair scheduler differs from round robin and O(1) in that the process that runs next is the one that has spent the ____least____ time running in recent history. By contrast, round-robin and O(1) determine who runs next from a ____queue/list/set____ of ready processes, where each one gets a time slice length based upon its ____priority____.

A scheduler is called ____fair____ if every process in the run queue receives the same amount of time. In O(1) scheduling, every process gets one time slice per ____epoch____. This is not considered ____fair____ because it does not compensate for time a process spends ____waiting/sleeping____ for other events. The ____completely fair____ scheduler gives such processes extra time.

The ____O(1)____ scheduler for linux minimizes computation at the expense of non-optimal ____fairness____. The main feature of this scheduler is that every process in the run queue gets a constant amount of runtime per ____epoch/slice____.

The problem with O(1) scheduling is that it is not fair, in the sense that a process that blocks waiting for I/O gets ____less____ CPU time than a process that does not.


(Extra credit) The translation lookaside buffer replaced the segment table on modern processors largely to save ____money____.

## Filesystem
If several processes have the same file open, they all share the same ____kernel____ descriptor for the file. If every process used a different one to write to the same file, then output could potentially be ____lost/overwritten____.

If one device in linux is opened by two processes, these processes have different ____process____ file descriptors but the same ____kernel____ file descriptor. If two processes write to the same file descriptor at the same time, writes are done one at a time. To describe this situation, we say that "write is ____atomic____". We can force sections of code to be effectively ____atomic____ by surrounding each section with ____mutex locks____.
