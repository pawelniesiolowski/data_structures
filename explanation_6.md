# Union and Intersection of Two Linked Lists

Union and intersection are typical set operations because the order of the elements in the set does not matter and the elements cannot be repeated.
To perform these operations on Linked Lists, you need to store information about the list values that have already been checked.
By storing used values in the set, this check has a constant time complexity - O(1). Doing union and intersection on two lists only requires a single pass through each of these lists.
The time complexity is O(n + m), where "n" and "m" are the numbers of elements in the first and second lists successively.
The spatial complexity by using a set is reduced to O(j + k), where "j" and "k" are the number of unique values in the first and second lists.

