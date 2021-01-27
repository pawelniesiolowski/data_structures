import hashlib
import datetime


class Block:

    def __init__(self, data, prev_block):
        self.timestamp = datetime.datetime.utcnow()
        if not isinstance(data, str):
            raise TypeError(f'Block data must by type of string, {type(data)} given')
        self.data = data
        self.hash = self.calc_hash()

        self.prev_block = prev_block
        self.prev_block_hash = prev_block.hash if prev_block else 0

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data + ' ' + self.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f%Z')
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.tail = None

    def add_data(self, data):
        block = Block(data, self.tail)
        self.tail = block

    def to_list_of_tuples(self):
        data = []

        block = self.tail

        if block is None:
            return data

        while True:
            data.append((block.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f%Z'), block.data, block.hash, block.prev_block_hash))

            if block.prev_block is None:
                break

            if block.prev_block_hash != block.prev_block.hash:
                raise KeyError('Invalid previous block hash - blockchain integration violation')

            block = block.prev_block

        return data

if __name__ == '__main__':

    # Tests basic functionalities

    tested_texts = ('First text', 'Second text', 'Third text')

    blockchain = Blockchain()
    blockchain.add_data(tested_texts[0])
    blockchain.add_data(tested_texts[1])
    blockchain.add_data(tested_texts[2])

    result = blockchain.to_list_of_tuples()
    num = 0
    while len(result) > 0:
        data = result.pop()
        assert data[1] == tested_texts[num]
        num += 1
        print(data)
        # (timestamp, 'First text', block hash, 0)
        # (timestamp, 'Second text', block hash, prev block hash)
        # (timestamp, 'Third text', block hash, prev block hash)

    blockchain.add_data('Another text')
    result = blockchain.to_list_of_tuples().pop(0)
    assert result[1] == 'Another text'
    print(result[1])
    # Another text

    # Test blockchain integration violation

    blockchain.tail.prev_block = Block('Invalid data', blockchain.tail.prev_block.prev_block)

    exception_thrown = False

    try:
        blockchain.to_list_of_tuples()
    except KeyError as e:
        exception_thrown = True

    assert exception_thrown

    print(exception_thrown)
    # True

    # Test empty blockchain has empty data

    blockchain = Blockchain()
    result = blockchain.to_list_of_tuples()
    assert result == []
    print(result)
    # []

    # Trying to create block with empty string

    blockchain = Blockchain()
    blockchain.add_data('')
    result = blockchain.to_list_of_tuples()
    # assert result == []
    print(result[0])
    # (timestamp, '', block hash, 0)

    # Trying to create an block with None value should raise exception

    blockchain = Blockchain()

    exception_thrown = False
    try:
        blockchain.add_data(None)
    except TypeError:
        exception_thrown = True

    assert exception_thrown
    print(exception_thrown)
    # True
