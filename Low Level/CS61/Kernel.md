# Kernel

## Virtual Memory
Virtual memory is a hardware mechanism used to isolate process memory, both from the kernel and from other processes. What it means is that an instruction attempting to move data from kernel memory or other processes' memory should not succeed.

Most modern architectures provide such guarantee through a mechanism called the page table.

### Page table
Page table can be thought of a filter, through which a process accesses memory. Every process has its own page table, and the process accesses memory through its page table. We will study a simple version of a page table before moving on to introducing the real x86 page table.
