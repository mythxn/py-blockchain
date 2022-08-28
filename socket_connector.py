class SocketConnector:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __eq__(self, other):
        return self.ip == other.ip and self.port == other.port
