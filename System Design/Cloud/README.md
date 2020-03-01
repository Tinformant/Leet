Process abstraction: Represents running instances of applications e.g., ls, cat, Emacs, Safari

Memory mapping: process vritual memory to physical memory

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
