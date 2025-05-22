from database import mock_db
from models.message import Message
from services.notification_service import NotificationService  # new import

class MessageService:
    @staticmethod
    def send_message(sender_username, receiver_username, content):
        # Check if receiver exists
        receiver_found = any(user.username == receiver_username for user in mock_db.users)
        if not receiver_found:
            print("Receiver not found.")
            return
        message = Message(sender_username, receiver_username, content)
        mock_db.messages.append(message)
        print(f"Message sent to {receiver_username}.")

    @staticmethod
    def view_inbox(username):
        inbox = [msg for msg in mock_db.messages if msg.receiver_username == username]
        if not inbox:
            print("No messages.")
            return
        for idx, msg in enumerate(inbox, start=1):
            print(f"{idx}. {msg}\n")

    @staticmethod
    def send_message(sender_username, receiver_username, content):
        receiver_found = any(user.username == receiver_username for user in mock_db.users)
        if not receiver_found:
            print("Receiver not found.")
            return
        message = Message(sender_username, receiver_username, content)
        mock_db.messages.append(message)

        NotificationService.add_notification(receiver_username, f"New message from {sender_username}")
        print(f"Message sent to {receiver_username}.")
