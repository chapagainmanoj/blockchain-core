import hashlib
import datetime

class Block():
    """
    Create a block with index, nonce, data, and previous_hash
    """

    def __init__(self, index, nonce,  data, previous_hash, hash = None):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.nonce = nonce
        self.previous_hash = previous_hash
        if hash:
            self.hash = hash
        else:
            self.hash = self.gen_hash()

    def gen_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                str(self.nonce).encode('utf-8') +
                str(self.data).encode('utf-8') +
                str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        block = {}
        block['index'] = self.index
        block['nonce'] = self.nonce
        block['timestamp'] = self.timestamp
        block['data'] = self.data
        block['previous_hash'] = self.previous_hash
        block['hash'] = self.hash
        return block

    def __str__(self):
        return """
                Block {}
                ======
                timestamp: {}
                nonce: {}
                data: {}
                previous_hash: {}
                hash: {}
                """.format(
                        self.index,
                        self.timestamp,
                        self.nonce,
                        self.data,
                        self.previous_hash,
                        self.hash
                        )

if __name__ == '__main__':
    b = Block(0, 888, 'data', '', 'sdf')
    print(b.__repr__())
