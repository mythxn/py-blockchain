import threading
import time

from chain_utils import ChainUtils
from message import Message


class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socket_communication = node

    def start(self):
        threading.Thread(target=self.status).start()
        threading.Thread(target=self.discovery).start()

    def status(self):
        while True:
            print('Current Connections:')
            for peer in self.socket_communication.peers:
                print(peer.ip, peer.port)
            time.sleep(5)

    def discovery(self):
        while True:
            self.socket_communication.broadcast(self.handshake_message())
            time.sleep(10)

    def handshake(self, connected_node):
        self.socket_communication.send(connected_node, self.handshake_message())

    def handshake_message(self):
        own_connector = self.socket_communication.socket_connector
        own_peers = self.socket_communication.peers
        data = own_peers
        message_type = 'discovery'
        message = Message(own_connector, message_type, data)
        return ChainUtils.encode(message)

    def handle_message(self, message):
        peers_socket_connector = message.sender_connector
        peers_peer_list = message.data

        new_peer = all(peer != peers_socket_connector for peer in self.socket_communication.peers)
        if new_peer:
            self.socket_communication.peers.append(peers_socket_connector)

        for peersPeer in peers_peer_list:
            peer_known = any(peer == peersPeer for peer in self.socket_communication.peers)
            if not peer_known and peersPeer != self.socket_communication.socket_connector:
                self.socket_communication.connect_with_node(peersPeer.ip, peersPeer.port)
