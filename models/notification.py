class Notification:
    def __init__(self, username, content):
        self.username = username
        self.content = content

    def __str__(self):
        return f"Notification for {self.username}: {self.content}"
