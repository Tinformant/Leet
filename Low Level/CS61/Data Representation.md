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
* static lifetime: The object lasts as long as the program runs. (Example: global_ch, const_global_ch)
* automatic lifetime: The compiler allocates and destroys the object automatically. (local_ch, allocated_ch)
* dynamic lifetime: The programmer allocates and destroys the object explicitly. (*allocated_ch)

## Memory Layout
* Code (aka text). Contains instructions and constant static objects; unmodifiable; static lifetime.
* Data. Modifiable; static lifetime.
* Heap. Modifiable; dynamic lifetime.
* Stack. Modifiable; automatic lifetime.

## Pointer Representation
* Addresses: hardware concepts.
* Pointers: concepts in the C abstract machine; a pointer combines an address and a type.


