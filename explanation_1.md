# Last Recently Used (LRU) cache

To achieve constant time complexity, I use a dictionary to store the data and a queue to store the last timestamps.
Also, to keep time complexity constant, I map timestamps to dictionary keys and vice versa.

Time complexity is always: O(1).
Space complexity is also O(1).

