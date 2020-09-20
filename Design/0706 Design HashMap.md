## 706 Design HashMap
### Two Issues: Hash Function Design & Collision Handling
1) hash function design: the purpose of hash function is to map a key value to an address in the storage spacefor a good hash function, it should map different keys evenly across the storage space.

2) collision handling: essentially the hash function reduces the vast key space into a limited address space and collision is inevitable.


### Modulo + Array
1. hash function design: modulo %; hash key = input % pre-picked modulo number (2069 in this case)
2. collision handling: use a **bucket** to hold all values
```java
class Pair<U, V> {
    public U first;
    public V second;
    
    public Pair (U first, V second) {
        this.first = first;
        this.second = second;
    }
}

class Bucket {
    private List<Pair<Integer, Integer>> bucket;
    
    public Bucket() {
        this.bucket = new LinkedList<Pair<Integer, Integer>>();
    }
    
    public Integer get (Integer key) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key))
                return pair.second;
        }
        return -1;
    }
    
    public void update (Integer key, Integer value) {
        boolean found = false;
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                pair.second = value;
                found = true;
            }
        }
        if (!found)
            this.bucket.add(new Pair<Integer, Integer>(key, value));
    }
    
    public void remove (Integer key) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                this.bucket.remove(pair);
                break;
            }
                
        }
    }
    
}

class MyHashMap {
    private int key;
    private List<Bucket> hashMap;

    /** Initialize your data structure here. */
    public MyHashMap() {
        this.key = 2069;
        this.hashMap = new LinkedList<Bucket>();
        for (int i = 0; i < key; i++)
            this.hashMap.add(new Bucket());
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int hashKey = key % this.key;
        this.hashMap.get(hashKey).update(key, value);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int hashKey = key % this.key;
        return this.hashMap.get(hashKey).get(key);
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int hashKey = key % this.key;
        this.hashMap.get(hashKey).remove(key);
    }
}
```
