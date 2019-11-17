### Little's laws
* average time in system
* average number of jobs waiting for completion
* average arrival rate
* arrival rate = average number of jobs waiting for completion / average time in system

Little's law relates arrival rate, time in system, and ____jobs in system____ for a queueing process. Little's law only requires that the system be ____in balance____. This is in contrast to all further results in queueing, which require some kind of assumption about the ____distribution____ of arrival times and/or service times.

If 20 people per hour arrive at a restaurant, and the same number of people leave every hour on average, and we observe that people stay an average of 2 hours, then there are ____40____ people on average inside the restaurant. This is only true because the system is in ____balance/steady state____ and because all values are ____averages____. If -- in addition -- there are always an average of 5 people waiting in line to be seated inside the restaurant , then the wait for seating is an average of ____1/4____ hour(s).

### Scheduling
Scheduling policies that seem fair may be unfair because processes ____block/suspend____ when they require input, thus giving up the rest of their ____time slice/allotment____.

The Completely Fair scheduler differs from round robin and O(1) in that the process that runs next is the one that has spent the ____least____ time running in recent history. By contrast, round-robin and O(1) determine who runs next from a ____queue/list/set____ of ready processes, where each one gets a time slice length based upon its ____priority____.
