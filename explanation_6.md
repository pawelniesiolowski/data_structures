# Union and Intersection of Two Linked Lists

Union and intersection are typical operations on sets, because the order of the elements in the set does not matter and the elements cannot be repeated.
To perform these operations on linked lists, one needs to store information about the list values that have already been checked.
By storing used values in the set, this check has a constant time complexity - O(1). Doing union and intersection on two lists requires only a single pass through each of these lists.
The time complexity is O(n + m), where "n" and "m" are the numbers of elements in the first and second list.
By using a set the spatial complexity is reduced to O(j + k), where "j" and "k" are the numbers of unique values in the first and second list.

