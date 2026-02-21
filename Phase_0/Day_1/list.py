arr = [10, 20, 30, 40]
print(arr)

## Basic loop
print("Basic loop")
for x in arr:
    print(x)

## Iterate with index using range
## len gives the number of items present in an object that are considered to be a sequence/collection
print("Iterate with index using range")
for x in range(len(arr)):
    print(x, arr[x])

"""
Iterate with index and value using enumerate()
Same as for(auto[key, value]: mpp)
enumerate() always returns 2 values: (index, element) — no matter what the element is.
If the element is a tuple/list, you can choose to unpack it manually.
"""

print("Iterate with index and value using enumerate()")
for index, value in enumerate(arr):
    print(index, value)

"""
Iterate backwards
"""
print("Iterate backwards")
for x in reversed(arr):
    print(x)

"""
   range(start, stop, step) same as for (int i = arr.size() -1; i >= 0(in this case -1); i--)
"""
print("Using range")
for x in range(len(arr) - 1, -1, -1):
    print(x, arr[x])
