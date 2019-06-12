from flask import Flask
from core.chain import Chain
import json

node = Flask(__name__)

@node.route('/blockchain.json', methods = ['GET'])
def blockchain():
    a_node = Chain()
    blockchain = json.dumps(a_node.node_blocks, indent=4)
    return blockchain

if __name__ == '__main__':
    node.run()
