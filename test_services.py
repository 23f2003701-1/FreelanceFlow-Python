from unittest import TestCase
from services.user_service import UserService
from services.gig_service import GigService
from services.order_service import OrderService
from services.message_service import MessageService
from services.review_service import ReviewService
from services.notification_service import NotificationService
from database import mock_db
from models.gig import Gig
from models.message import Message

class TestUserService(TestCase):
    def setUp(self):
        mock_db.users.clear()

    def test_register_valid(self):
        UserService.register("testuser", "123", "client")
        self.assertEqual(len(mock_db.users), 1)

    def test_register_invalid_role(self):
        UserService.register("baduser", "123", "teacher")
        self.assertEqual(len(mock_db.users), 0)

    def test_login_success(self):
        UserService.register("loginuser", "pass", "freelancer")
        user = UserService.login("loginuser", "pass")
        self.assertIsNotNone(user)

class TestGigService(TestCase):
    def setUp(self):
        mock_db.gigs.clear()

    def test_create_gig(self):
        GigService.create_gig("Test Gig", "Some desc", 100, "freelancer1")
        self.assertEqual(len(mock_db.gigs), 1)

class TestOrderService(TestCase):
    def setUp(self):
        mock_db.gigs.clear()
        mock_db.orders.clear()
        gig = Gig("Web Dev", "desc", 200, "freelancer1")
        mock_db.gigs.append(gig)

    def test_place_order_valid(self):
        OrderService.place_order(1, "client1")
        self.assertEqual(len(mock_db.orders), 1)

class TestMessageService(TestCase):
    def setUp(self):
        mock_db.users.clear()
        mock_db.messages.clear()
        from models.user import User
        mock_db.users.append(User("sender", "123", "client"))
        mock_db.users.append(User("receiver", "123", "freelancer"))

    def test_send_message_valid(self):
        MessageService.send_message("sender", "receiver", "Hello")
        self.assertEqual(len(mock_db.messages), 1)

class TestNotificationService(TestCase):
    def setUp(self):
        mock_db.notifications.clear()

    def test_add_notification(self):
        NotificationService.add_notification("user1", "Msg arrived")
        self.assertEqual(len(mock_db.notifications), 1)

if __name__ == '__main__':
    import unittest
    unittest.main()
