from flask import Flask
from core.chain import Chain
import json

node = Flask(__name__)

@node.route('/blockchain.json', methods = ['GET'])
def blockchain():
    chain = Chain()
    blockchain = json.dumps(chain.node_blocks, indent=4)
    return blockchain

if __name__ == '__main__':
    node.run()
