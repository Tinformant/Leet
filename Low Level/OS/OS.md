A process is a running version of a program and has an execution context, including register values and memory map.

**Context switching** accomplishes latency hiding, where one process accomplishes work while another one is waiting for something.

A process communicates with OS (and devices) via **system calls**.

OS sends signals to process via **signals**.

Time
* Wallclock time: the usual notion of time, in elapsed seconds.
* User time: the time spent in a process.
* System time: the time spent in system calls, at the request of a process.
* (OS time or "overhead": the time spent outside processes) 

__Frame__ a unit of memory in OS.
  * __physical address__ where is it in the machine.
__Page__ 
  * a unit of memory in process.
  * Every page has __logical address__ within the process.
__Memory Mapping__ associates frames with pages

Memory Mapping
