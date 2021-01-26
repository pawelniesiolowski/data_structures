# Blockchain

This simple blockchain implementation is based on a list where each list node points to the previous node.
Getting and adding a new block has O(1) time complexity. Searching for the appropriate item in the list can be O(n) in the worst case scenario.
Additionally, the integrity of the elements is ensured by storing information about the previous element's hash
and checking it while the previous element passes through subsequent nodes.
The spatial complexity is dependent on the number of elements - O(n).
