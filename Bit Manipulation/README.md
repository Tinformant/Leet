# Bit Manipulation
* 136 Single Number
* 137 Single Number II
* 461 Hamming Distance
* 371 Sum of Two Integers
* 169 Majority Element
* 191 Number of 1 Bits
* 338 Counting Bits
* 268 Missing Number
* 190 Reverse Bits
* 476 Number Complement

* Set union A | B
* Set intersection A & B
* Set subtraction A & ~B
* Set negation ALL_BITS ^ A or ~A
* Set bit A |= 1 << bit
* Clear bit A &= ~(1 << bit)
* Test bit (A & 1 << bit) != 0
* Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
* Remove last bit A&(A-1)
* Get all 1-bits ~0

Find carry: use &
1. a =      001
2. b =      011
3. carry =  001 


>> (Signed right shift) In Java, the operator ‘>>’ is signed right shift operator. 

All integers are signed in Java, and it is fine to use >> for negative numbers. The operator ‘>>’ uses the sign bit (left most bit) to fill the trailing positions after shift. If the number is negative, then 1 is used as a filler and if the number is positive, then 0 is used as a filler.

>>> (Unsigned right shift) In Java, the operator ‘>>>’ is unsigned right shift operator. It always fills 0 irrespective of the sign of the number.

i >>= 1 is equivalent to i = i >> 1;

