Process abstraction: represents running instances of applications e.g., ls, cat, Emacs, Safari

A process's memory:
* code: compiled application code
* data: constants
* heap: memory allocated during execution
* stack: local variables, function parameters

Memory virtualization (a process's memory is virtual)
* Memory mapping: process vritual memory to physical memory (also belongs to a process)
* Isolates processes memory from one another, Gives processes illusion of having all of a machine's memory


A process's registers:
  * PC: points to next instruction to execute on CPU
  * stack pointer: last used address on stack
  * General purpose: Stores data from memory for computation
  
  State that is maintained:
 
# of processes that can concurrently execute on 1 CPU?
A: Only one

# of CPUs a single process can concurrently run on?
A: Also one

## Traffic Engineering
Flow groups: applications grouped together. High-priority applications grouped together. Low-priority applications grouped together.

## Bandwidth fns
How much bandwidth to allocate for each app or flow group (FG) based on priority.
