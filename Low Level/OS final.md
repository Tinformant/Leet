## Journelling
### How journalling works 
To write a journal
1. Start with an empty journal.  
2. When a block is requested to be written, write the block into the journal; write where it goes into a journal hash.  

To read a block, check the page cache; if it's in there, done.  
1. check the journal hash to see whether it's in the journal; If so, read it from there.  
2. If not, read it from its actual place on disk.  
3. Put it back into the page cache. 

To flush the journal:  
1. write its contents into their respective block locations.  
2. clear the journal afterward.  
Because the journal is a contiguous piece of memory, we can write it to the disk (in another place) in one operation.  

Use this -- whenever we lose power -- to restore consistency. 


### Unjournaled VS journaled
unjournaled
1. fast read
2. lasy write
3. fsck takes forever 

## Filesystm
* blocks: contain data.
* inode: contain information on where the file is.
* superblock: describe where inodes and blocks are located on disk.
* directory: a special kind of file that associates file names with file numbers.

## Inode & Block(data)
"Identity node". Contains all attributes of a file or directory: 
* owner
* group,  
* protection 
* where its blocks are located.  
* Does not contain the name. Found by number, not name.  
What is a block?  
* Just a chunk of bits.  
*Typically, inodes and blocks are striped into alternating stripes on the disk: 

## super-block
* A descriptor with pointers to  
* All groups of inodes 
* All block groups 
* What directory is root ("/") 
* Duplicated all over the disk.  
* If it is lost, disk data becomes meaningless! 

## file  
A pair: <inode, sequence of blocks> 
Inode identified as a number.  
inode is an offset into a descriptor table; descriptor tells where the blocks are and how to find them.  
Better to say "array" of inodes:  
We require O(1) random access by inode number.  
Better to say: "array" of blocks.  
We require O(1) random access by block number.  

## Protection
user-group-other
Protection: Files/Directories
r: can read it/can ls it
w: can write it/can create and delete files in it 
x: can execute it as a program/can access things in it if you know their names already
