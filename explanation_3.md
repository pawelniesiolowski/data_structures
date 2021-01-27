# Huffman Coding

In HuffmanTreeEncoder I create nodes frequency queue in list which I sort in reverse order
to pop elements from the end of the list, that does not require recreating the list.
Re-sorting presorted list after appending it with parent node is cheap thanks to Timsort algorithm.

Iterating over characters building characters frequency queue, sorting builded frequency
(sorting for first time is O(n log n)) and creating nodes from elements needs O(n log n)
where "n" is the number of unique characters.

Creating Huffman Tree from the nodes frequency queue with resorting elements in list
(resorting presorted data after appending value to list is nearly O(1)) needs O(n).

Building codes for chars recursively needs O(n log n) time complexity. Where "n" is
the previously mentioned number of unique characters and "log n" stands for number of recursive repetitions
to traverse the same nodes.

Encoding data is O(n) where "n" is number of characters to encode
(getting characters codes from dictionary is O(1)).

Huffman encoding time complexity is approximately: O(n log n)

Huffman decoding is O(n log n) where "n" is number of binary characters representing encoded data and
"log n" means number of recursive repetitions to traverse the same nodes.

Huffman coding space complexity: O(n) where "n" is number of characters
represented as binary encoded data.
