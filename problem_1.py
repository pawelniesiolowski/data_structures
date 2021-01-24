from collections import deque
import time


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_of_elements = 0
        self.data = {}
        self.timestamps = Timestamps()

    def get(self, key):
        if key in self.data:
            self.timestamps.actualize_for_key(key)
            return self.data[key]

        return -1

    def set(self, key, value):
        if key in self.data:
            return

        self.manage_capacity()

        self.data[key] = value
        self.num_of_elements += 1
        self.timestamps.add_for_key(key)

    def manage_capacity(self):
        if self.num_of_elements < self.capacity:
            return

        oldest_key = self.timestamps.get_and_remove_oldest_key()
        del self.data[oldest_key]
        self.num_of_elements -= 1


class Timestamps:

    def __init__(self):
        self.timestamps = deque()
        self.keys_for_timestamps = {}
        self.timestamps_for_keys = {}

    def actualize_for_key(self, key):
        previous_timestamp = self.timestamps_for_keys[key]
        del self.keys_for_timestamps[previous_timestamp]

        self._do_add_timestamp(key)

    def add_for_key(self, key):
        self._do_add_timestamp(key)

    def get_and_remove_oldest_key(self):
        oldest_timestamp = self.timestamps.popleft()

        while oldest_timestamp not in self.keys_for_timestamps:
            oldest_timestamp = self.timestamps.popleft()

        oldest_key = self.keys_for_timestamps[oldest_timestamp]

        del self.keys_for_timestamps[oldest_timestamp]
        del self.timestamps_for_keys[oldest_key]

        return oldest_key

    def _do_add_timestamp(self, key):
        timestamp = time.time()

        self.keys_for_timestamps[timestamp] = key
        self.timestamps_for_keys[key] = timestamp
        self.timestamps.append(timestamp)


our_cache = LRUCache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

result = our_cache.get(1)
assert result == 1
print(result)
# 1

result = our_cache.get(2)
assert result == 2
print(result)
# 2

result = our_cache.get(9)
assert result == -1
print(result)
# -1

our_cache.set(5, 5)
our_cache.set(6, 6)

result = our_cache.get(3)
assert result == -1
print(result)
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
