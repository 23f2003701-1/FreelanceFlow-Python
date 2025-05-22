from database import mock_db
from models.notification import Notification

class NotificationService:
    @staticmethod
    def add_notification(username, content):
        notification = Notification(username, content)
        mock_db.notifications.append(notification)

    @staticmethod
    def view_notifications(username):
        user_notifications = [n for n in mock_db.notifications if n.username == username]
        if not user_notifications:
            print("No notifications.")
            return
        for idx, notification in enumerate(user_notifications, start=1):
            print(f"{idx}. {notification.content}")

    @staticmethod
    def clear_notifications(username):
        mock_db.notifications = [n for n in mock_db.notifications if n.username != username]
        print("Notifications cleared.")
