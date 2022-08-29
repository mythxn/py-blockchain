import sys

from node import Node

if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    api_port = int(sys.argv[3])
    key_file = sys.argv[4] if len(sys.argv) > 4 else None

    node = Node(ip, port, key_file)
    node.start_p2p()
    node.start_api(api_port)
