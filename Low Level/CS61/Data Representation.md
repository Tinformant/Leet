# Data Representation

## Objects
```cpp
char global_ch = 65;
const char const_global_ch = 66;

void f() {
    char local_ch = 67;
    char* allocated_ch = new char(68)
    // C-style: `allocated_ch = (char*) malloc(sizeof(char)); *allocated_ch = 68;`
}
```

* static lifetime: object lasts as long as the program runs. (Example: global_ch, const_global_ch)
* automatic lifetime: compiler allocates and destroys the object automatically. (local_ch, allocated_ch)
* dynamic lifetime: programmer allocates and destroys the object explicitly. (*allocated_ch)

## Memory Layout
* Code (aka text). Contains instructions and constant static objects; unmodifiable; static lifetime.
* Data. Modifiable; static lifetime.
* Heap. Modifiable; dynamic lifetime.
* Stack. Modifiable; automatic lifetime.


## Data Layout
Each object uses a contiguous range of addresses (and thus bytes).

* sizeof(T) returns the number of bytes in the representation of an object of type T
* sizeof(x) returns the size of object x. 


## Signed Integer Representation
### Two's complement
Representation for signed integers (x86-64) is two’s complement; 

principle: addition and subtraction of signed integers shall use the same instructions as addition and subtraction of unsigned integers.

principle: adding x and -x result in 0.

To see what this means, let’s think about what -x should mean when x is an unsigned integer. Wait, negative unsigned?! This isn’t an oxymoron because C++ uses modular arithmetic for unsigned integers: the result of an arithmetic operation on unsigned values is always taken modulo 2B, where B is the number of bits in the unsigned value type. Thus, on x86-64,

Given an array a[N] of N elements of type T:
1. Forming a pointer &a[i] (or a + i) with 0 ≤ i ≤ N is safe.
2. Forming a pointer &a[i] with i < 0 or i > N causes undefined behavior.
3. Dereferencing a pointer &a[i] with 0 ≤ i < N is safe.
4. Dereferencing a pointer &a[i] with i < 0 or i ≥ N causes undefined behavior.

## Collections: Abstract Mahine Layout 
The collections are structs, arrays and unions (classes are a kind of struct).

**1. First-Member Rule:** the address of the first member of the collection equals the address of the collection.
For example, the address of an array is the same as the address of its first element. The address of a struct is the same as the address of the first member of the struct.

**2. Struct Rule:** the second and subsequent member of a struct are laid out in order, with no overlap, subject to alignment constraints.

**3. Array Rule:** the address of the ith element of an array of type T is ADDRESSOF(array) + i * sizeof(T).

**4. Union Rule:** all members of a union share the address of the union.

### Alignment
C compiler and library restrict the addresses at which some kinds of data appear.

* char(signed char, unsigned char): 1, no restriction
* short(unsigned short): 2, multiple of 2
* int(unsigned int): 4, multiple of 4
* long(unsigned long): 8, multiple of 8
* float: 4, multiple of 4
* double: 8, multiple of 8
* T*: 8, multiple of 8

## Alignment Rules
5. Malloc rule. Any non-null pointer returned by malloc has alignment appropriate for any type. In other words, assuming the allocated size is adequate, the pointer returned from malloc can safely be cast to T* for any T.

Oddly, this holds even for small allocations. The C++ standard (the abstract machine) requires that malloc(1) return a pointer whose alignment is appropriate for any type, including types that don’t fit.

The last rule is not required by the abstract machine, but it’s how sizes and alignments on our machines work:

6. Minimum rule. The sizes and alignments of user-defined types, and the offsets of struct members, are minimized within the constraints of the other rules.


## Pointer Representation
* Addresses: hardware concepts.
* Pointers: concepts in the C abstract machine; a pointer combines an address and a type.
