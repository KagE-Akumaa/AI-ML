# Phase 0 — Python Foundations (Backend/System Programming Notes)

## 1. Python Lists (Dynamic Arrays)

### **Definition**
Lists are dynamic arrays that store elements in contiguous memory (CPython). Elements are mutable and ordered.

### **Key Properties**
- Ordered  
- Mutable  
- Supports duplicates  
- Fast random access (O(1))  
- Append: Amortized O(1)  
- Insert/remove in middle: O(n)

### **Essential Operations**
- `append(x)` — add element to end  
- `pop()` — remove last element  
- `pop(i)` — remove element at index  
- Indexing: O(1)  
- Slicing creates a copy

### **System/Backend Relevance**
- Ideal for buffers, queues, batching logs  
- Behaves similarly to C++ `vector`

---

## 2. Python Dictionaries (Hash Maps)

### **Definition**
Dictionaries are hash tables mapping keys to values. Optimized for fast lookup.

### **Key Properties**
- Unique keys  
- Values can be any type  
- Keys must be hashable (immutable types)  
- Stable insertion order (Python 3.7+)  
- Average O(1) for insert, delete, lookup

### **Essential Operations**
- `d[k] = v` — insert/update  
- `d[k]` — lookup  
- `k in d` — membership check  
- `.keys()` — view of keys  
- `.values()` — view of values  
- `.items()` — view of key-value pairs  
- `.pop(k)` — remove key

### **System/Backend Relevance**
- Used in routing tables, configs, JSON payloads, caches  
- Perfect for counting (IP hits, user frequency)  
- Equivalent to C++ `unordered_map`

---

## 3. Python Sets (Unique Hash Table)

### **Definition**
Sets are hash tables storing only unique keys.

### **Key Properties**
- Unordered  
- Unique elements  
- Membership check O(1)  
- Great for filtering duplicates

### **Essential Operations**
- `add(x)` — insert  
- `remove(x)` / `discard(x)` — delete  
- `x in set` — fast membership test  
- Convert list → set for deduplication

### **System/Backend Relevance**
- Remove duplicate IPs from logs  
- Track unique API keys, URLs, syscalls  
- Fast filtering structure  
- Similar to C++ `unordered_set`

---

## 4. Memory Behavior (Low-Level View)

### **Lists**
- Store pointers in contiguous memory  
- Grow capacity using geometric expansion (~12.5%)

### **Dicts/Sets**
- Sparse hash tables  
- Open addressing with probing  
- Good CPU-cache locality

---

## 5. What You Should Practice

### **Lists**
- Buffering requests, collecting logs  
- Append/pop operations  
- Slicing and iteration  

### **Dictionaries**
- Mapping `user → metadata`  
- `IP → hit count`  
- `URL → latency`  
- Routing and configuration structures  

### **Sets**
- Deduplicating logs  
- Tracking unique items  
- Filtering repeated events  

---

## 6. Skills Required Before Phase 1

### **List Skills**
- Append, pop  
- Indexing and slicing  
- Understanding O(1) vs O(n)

### **Dict Skills**
- Create/update/delete entries  
- Using `.keys()`, `.values()`, `.items()`  
- Frequency counting  

### **Set Skills**
- Deduplication  
- Membership checks  
- Safe add/remove usage  

---

This completes the Phase 0 Python fundamentals notes for backend and system programming.
