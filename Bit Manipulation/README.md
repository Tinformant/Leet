Find carry: use &
1. a =      001
2. b =      011
3. carry =  001 


>> (Signed right shift) In Java, the operator ‘>>’ is signed right shift operator. 

All integers are signed in Java, and it is fine to use >> for negative numbers. The operator ‘>>’ uses the sign bit (left most bit) to fill the trailing positions after shift. If the number is negative, then 1 is used as a filler and if the number is positive, then 0 is used as a filler.

>>> (Unsigned right shift) In Java, the operator ‘>>>’ is unsigned right shift operator. It always fills 0 irrespective of the sign of the number.
