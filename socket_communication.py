from p2pnetwork.node import Node

from peer_discovery_handler import PeerDiscoveryHandler


class SocketCommunication(Node):

    def __init__(self, ip, port):
        super().__init__(ip, port, None)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)

    def start_socket(self):
        self.start()
        self.peer_discovery_handler.start()

    def inbound_node_connected(self, connected_node):
        print('inbound_node_connected')
        self.send_to_node(connected_node, f'Hello from {self.port}')

    def outbound_node_connected(self, connected_node):
        print('outbound_node_connected')
        self.send_to_node(connected_node, f'Hello from {self.port}')

    def node_message(self, connected_node, message):
        print(message)