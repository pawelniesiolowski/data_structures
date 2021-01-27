import sys


def huffman_encoding(data):
    encoder = HuffmanTreeEncoder(data)
    return (encoder.encode(), encoder.get_head_of_tree())


def huffman_decoding(data,tree):
    decoder = HuffmanTreeDecoder(tree)
    return decoder.decode(data)


class HuffmanTreeEncoder:
    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError('Encoder encodes only string data')

        if data != '':
            self.data = data
            nodes_frequency = self._create_nodes_frequency_queue()
            self._create_huffman_tree(nodes_frequency)
            self._build_codes_for_chars()
        else:
            self.data = ''
            self.head = HuffmanTreeNode(None)

    def encode(self):
        encoded_data = ''
        for char in self.data:
            encoded_data += self.codes[char]
        return encoded_data

    def get_head_of_tree(self):
        return self.head

    def _create_nodes_frequency_queue(self):
        chars_frequency = {}
        for char in self.data:
            chars_frequency[char] = chars_frequency.get(char, 0) + 1
        chars_frequency_queue = sorted(chars_frequency.items(), key=lambda item: item[1], reverse=True)
        nodes_frequency_queue = [HuffmanTreeNode(item) for item in chars_frequency_queue]
        return nodes_frequency_queue

    def _create_huffman_tree(self, nodes_frequency):
        while len(nodes_frequency) > 1:
            first_node = nodes_frequency.pop()
            second_node = nodes_frequency.pop()

            first_value = first_node.get_frequency() if first_node.has_char() else first_node.value
            second_value = second_node.get_frequency() if second_node.has_char() else second_node.value
            parent_node = HuffmanTreeNode(first_value + second_value)

            parent_node.left_child = first_node if first_value < second_value else second_node
            parent_node.right_child = first_node if first_value >= second_value else second_node

            nodes_frequency.append(parent_node)

            nodes_frequency = sorted(
                nodes_frequency,
                key=lambda node: node.get_frequency() if node.has_char() else node.value,
                reverse=True
            )

        self.head = nodes_frequency.pop()

    def _build_codes_for_chars(self):
        codes = {}

        def do_build_codes(node, code):
            if node.has_char():
                codes[node.get_char()] = code or '0'
            else:
                do_build_codes(node.left_child, code + '0')
                do_build_codes(node.right_child, code + '1')

        do_build_codes(self.head, '')
        self.codes = codes


class HuffmanTreeDecoder():
    def __init__(self, tree):
        self.tree = tree

    def decode(self, data):
        message = ''
        node = self.tree

        single_node_in_tree = False
        if node.left_child is None and node.right_child is None:
            single_node_in_tree = True

        for char in data:
            if single_node_in_tree and node.has_char():
                message += node.get_char()
                continue

            if node.has_char():
                message += node.get_char()
                node = self.tree
            if char == '0':
                node = node.left_child
            else:
                node = node.right_child

        if node.has_char() and not single_node_in_tree:
            message += node.get_char()

        return message


class HuffmanTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def has_char(self):
        return isinstance(self.value, tuple)

    def get_char(self):
        return self.value[0]

    def get_frequency(self):
        return self.value[1]

    def __repr__(self):
        def show_tree(node, tree, level):
            if node is not None:
                tree.append((str(node.value), level))
                show_tree(node.left_child, tree, level + 1)
                show_tree(node.right_child, tree, level + 1)
            else:
                tree.append(('None', level))

        tree = []
        show_tree(self, tree, 0)
        tree = sorted(tree, key=lambda item: item[1])

        string = ''
        prev_level = 0
        for i in range(len(tree)):
            if prev_level < tree[i][1]:
                string += '\n'
                prev_level += 1
            elif prev_level != 0:
                string += ' | '
            string += tree[i][0]
        return string


if __name__ == '__main__':

    # Tests

    codes = {}

    a_great_sentence = 'The bird is the word'

    print('The size of the data is: {}\n'.format(sys.getsizeof(a_great_sentence)))
    print('The content of the data is: {}\n'.format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The size of the encoded data is: {}\n'.format(sys.getsizeof(int(encoded_data, base=2))))
    print('The content of the encoded data is: {}\n'.format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The size of the decoded data is: {}\n'.format(sys.getsizeof(decoded_data)))
    print('The content of the encoded data is: {}\n'.format(decoded_data))


    first_test_sentence = 'This is my first test of the Huffman Coding'
    encoded_data, tree = huffman_encoding(first_test_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert first_test_sentence == decoded_data
    print(decoded_data)
    # This is my first test of the Huffman Coding

    second_test_data = '12345678910'
    encoded_data, tree = huffman_encoding(second_test_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert second_test_data == decoded_data
    print(decoded_data)
    # 12345678910

    empty_string = ''
    encoded_data, tree = huffman_encoding(empty_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert empty_string == decoded_data
    assert isinstance(decoded_data, str)
    print(decoded_data)
    # empty string

    repetitive_char = 'AAAAAA'
    encoded_data, tree = huffman_encoding(repetitive_char)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert repetitive_char == decoded_data
    assert isinstance(decoded_data, str)
    print(decoded_data)
    # AAAAAA
