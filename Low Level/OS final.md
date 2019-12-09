### Journelling
How journalling works 

1. Start with an empty journal.  
2. When a block is requested to be written, write the block into the journal; write where it goes into a journal hash.  
3. To read a block, check the page cache; if it's in there, done.  
4. check the journal hash to see whether it's in the journal; If so, read it from there.  
5. If not, read it from its actual place on disk.  
6. Put it back into the page cache. 

To flush the journal:  
1. write its contents into their respective block locations.  
2. clear the journal afterward.  
Because the journal is a contiguous piece of memory, we can write it to the disk (in another place) in one operation.  

Use this -- whenever we lose power -- to restore consistency. 
