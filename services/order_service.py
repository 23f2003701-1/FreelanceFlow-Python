from database import mock_db
from models.order import Order
from services.notification_service import NotificationService  # new import

class OrderService:
    @staticmethod
    def place_order(gig_index, client_username):
        if gig_index < 1 or gig_index > len(mock_db.gigs):
            print("Invalid gig selected.")
            return
        gig = mock_db.gigs[gig_index - 1]
        order = Order(gig, client_username)
        mock_db.orders.append(order)
        print(f"Order placed successfully for gig '{gig.title}'.")

    @staticmethod
    def view_client_orders(client_username):
        orders = [order for order in mock_db.orders if order.client_username == client_username]
        if not orders:
            print("You have no orders yet.")
            return
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. {order}")

    @staticmethod
    def view_freelancer_orders(freelancer_username):
        orders = [order for order in mock_db.orders if order.freelancer_username == freelancer_username]
        if not orders:
            print("No orders received yet.")
            return
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. {order}")

    @staticmethod
    def place_order(gig_choice, client_username):
        if not mock_db.gigs:
            print("No gigs available to order.")
            return

        if gig_choice < 1 or gig_choice > len(mock_db.gigs):
            print("Invalid gig choice.")
            return

        gig = mock_db.gigs[gig_choice - 1]
        order = Order(gig, client_username)
        mock_db.orders.append(order)

        NotificationService.add_notification(gig.freelancer_username, f"New order placed for your gig: {gig.title}")
        print(f"Order placed for gig: {gig.title}")
