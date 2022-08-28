class Message():

    def __init__(self, sender_connector, msg_type, data):
        self.sender_connector = sender_connector
        self.msg_type = msg_type
        self.data = data
