from p2pnetwork.node import Node

from peer_discovery_handler import PeerDiscoveryHandler
from socket_connector import SocketConnector


class SocketCommunication(Node):

    def __init__(self, ip, port):
        super().__init__(ip, port, None)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.socket_connector = SocketConnector(ip, port)

    def connect_to_first_node(self):
        if self.socket_connector.port != 10001:
            self.connect_to_node(SocketConnector('localhost', 10001))

    def start_socket(self):
        self.start()
        self.peer_discovery_handler.start()

    def inbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def outbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def node_message(self, connected_node, message):
        print(message)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)
