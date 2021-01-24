# Huffman Coding

In HuffmanTreeEncoder I create nodes frequency queue in list which I sort in reverse order
to pop elements from the end of the list, which does not require recreating the list.
Re-sorting presorted list after appending it with parent node is cheap thanks to Timsort algorithm.

Iterating over characters building characters frequency queue, sorting builded frequency
(sorting for first time is O(n log n)) and creating nodes from elements needs O(n + 2m log m)
where m is the number of unique characters.

Creating huffman tree from the nodes frequency queue with resorting elements in list
(resorting presorted data after appending value to list is nearly O(1)) needs O(m).

Building codes for chars recursively needs O(m * t) time complexity. Where "m" is
the previously mentioned number of unique characters and "t" is number of recursive repetitions
to traverse the same nodes.

Encoding data is O(n) where "n" is number of characters to encode
(getting characters codes from dictionary is O(1)).

Huffman encoding time complexity: O(2n + 4m log m * t)

Huffman decoding is O(m * t) where m is number of a binary characters representing encoded data and
"t" is number of recursive repetition to traverse the same nodes.

Huffman coding space complexity: O(m + t) where m is number of unique characters
represented in the Huffman Tree and "t" is a binary representation of encoded data.
