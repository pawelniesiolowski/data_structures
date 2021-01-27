class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        cur_head = self.head
        data = []
        while cur_head:
            data.append(cur_head.value)
            cur_head = cur_head.next
        return data

    def __str__(self):
        cur_head = self.head
        out_string = ''
        while cur_head:
            out_string += str(cur_head.value) + ' -> '
            cur_head = cur_head.next
        return out_string


def union(list_1, list_2):
    checked_elements = set()
    new_list = LinkedList()

    cur_head_1 = list_1.head
    while cur_head_1:
        if not cur_head_1.value in checked_elements:
            new_list.append(cur_head_1.value)
            checked_elements.add(cur_head_1.value)
        cur_head_1 = cur_head_1.next

    cur_head_2 = list_2.head
    while cur_head_2:
        if not cur_head_2.value in checked_elements:
            new_list.append(cur_head_2.value)
            checked_elements.add(cur_head_2.value)
        cur_head_2 = cur_head_2.next

    return new_list


def intersection(list_1, list_2):
    first_list_elements = set(list_1.to_list())
    checked_elements = set()
    new_list = LinkedList()

    cur_head_2 = list_2.head
    while cur_head_2:
        if cur_head_2.value in first_list_elements and cur_head_2.value not in checked_elements:
            new_list.append(cur_head_2.value)
            checked_elements.add(cur_head_2.value)
        cur_head_2 = cur_head_2.next

    return new_list


if __name__ == '__main__':

    # Tests

    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    result = union(linked_list_1, linked_list_2)
    unioned_elements = set(element_1).union(set(element_2))
    assert result.size() == len(unioned_elements)
    assert all(el in result.to_list() for el in unioned_elements)
    print(result)
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->

    result = intersection(linked_list_1, linked_list_2)
    intersectioned_elements = set(element_1).intersection(element_2)
    assert result.size() == len(intersectioned_elements)
    assert all(el in result.to_list() for el in intersectioned_elements)
    print(result)
    # 6 -> 4 -> 21 ->

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    result = union(linked_list_3, linked_list_4)
    unioned_elements = set(element_1).union(set(element_2))
    assert result.size() == len(unioned_elements)
    assert all(el in result.to_list() for el in unioned_elements)
    print(result)
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->

    result = intersection(linked_list_3, linked_list_4)
    intersectioned_elements = set(element_1).intersection(element_2)
    assert result.size() == len(intersectioned_elements)
    assert all(el in result.to_list() for el in intersectioned_elements)
    print(result)
    # empty result

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [1,2,3,4,5,6]
    element_2 = [6,7,8,9,10]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    result = union(linked_list_5, linked_list_6)
    unioned_elements = set(element_1).union(set(element_2))
    assert result.size() == len(unioned_elements)
    assert all(el in result.to_list() for el in unioned_elements)
    print(result)
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 ->

    result = intersection(linked_list_5, linked_list_6)
    intersectioned_elements = set(element_1).intersection(element_2)
    assert result.size() == len(intersectioned_elements)
    assert all(el in result.to_list() for el in intersectioned_elements)
    print(result)
    # 6 ->

    # Test case 4

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [1,1,1,1,1]
    element_2 = [2,2,2,2,2]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    result = union(linked_list_7, linked_list_8)
    unioned_elements = set(element_1).union(set(element_2))
    assert result.size() == len(unioned_elements)
    assert all(el in result.to_list() for el in unioned_elements)
    print(result)
    # 1 -> 2 ->

    result = intersection(linked_list_7, linked_list_8)
    intersectioned_elements = set(element_1).intersection(element_2)
    assert result.size() == len(intersectioned_elements)
    assert all(el in result.to_list() for el in intersectioned_elements)
    print(result)
    # empty result

    # Test case 4

    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()

    element_1 = [1,1,2,2,3,4,5,6,7,8,1000000]
    element_2 = [1000000]

    for i in element_1:
        linked_list_9.append(i)

    for i in element_2:
        linked_list_10.append(i)

    result = union(linked_list_9, linked_list_10)
    unioned_elements = set(element_1).union(set(element_2))
    assert result.size() == len(unioned_elements)
    assert all(el in result.to_list() for el in unioned_elements)
    print(result)
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 1000000 ->

    result = intersection(linked_list_9, linked_list_10)
    intersectioned_elements = set(element_1).intersection(element_2)
    assert result.size() == len(intersectioned_elements)
    assert all(el in result.to_list() for el in intersectioned_elements)
    print(result)
    # 1000000 ->

    # Test case 5

    linked_list_11 = LinkedList()
    linked_list_12 = LinkedList()

    result = union(linked_list_11, linked_list_12)
    assert result.size() == 0
    print(result)
    # empty result

    result = intersection(linked_list_11, linked_list_12)
    assert result.size() == 0
    print(result)
    # empty result

    # Test case 6

    linked_list_13 = LinkedList()
    linked_list_14 = LinkedList()

    element_1 = [1,2,3]

    for i in element_1:
        linked_list_13.append(i)

    result = union(linked_list_13, linked_list_14)
    assert result.size() == len(element_1)
    print(result)
    # 1 -> 2 -> 3 ->

    result = intersection(linked_list_13, linked_list_14)
    assert result.size() == 0
    print(result)
    # empty result
