import os
import json
import datetime
from .setting import *
from .block import Block

"""
Chain: list of block objects
"""

class Chain:
    def __init__(self):
        self.node_blocks = []
        self.sync()

    def sync(self):
        if os.path.exists(LEDGER_NAME):
            print('Ledger exists')
            with open(LEDGER_NAME, 'r') as ledger:
                init = json.load(ledger)
                self.node_blocks.append(init)
        else:
            print('Creating a ledger')
            first_block = self.genesis().__repr__()
            self.node_blocks.append(first_block)
            # json.dump(self.node_blocks, setting.LEDGER_NAME)
            with open(LEDGER_NAME, 'w') as ledger:
                jsonstr = json.dumps(self.node_blocks, indent = 4)
                ledger.write(jsonstr)

    def check_integrety (self):
        # check if any data is tampered
        pass

    def __repr__(self):
        return json.dumps(self.node_blocks)

    def genesis(self):
        return Block(0, 4, GENESIS, None)

    def mine(last):
        pass

if __name__ == '__main__':
    chain = Chain()
