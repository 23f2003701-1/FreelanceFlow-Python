class Message:
    def __init__(self, sender_username, receiver_username, content):
        self.sender_username = sender_username
        self.receiver_username = receiver_username
        self.content = content

    def __str__(self):
        return f"From: {self.sender_username} | To: {self.receiver_username}\nMessage: {self.content}"
