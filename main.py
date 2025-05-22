from services.user_service import UserService
from services.gig_service import GigService
from services.order_service import OrderService
from services.message_service import MessageService
from services.review_service import ReviewService
from services.notification_service import NotificationService
from database import mock_db

mock_db.populate_sample_data()  

current_user = None  

def main_menu():
    global current_user
    while True:
        print("\n=== FreelanceFlow ===")
        if not current_user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (client/freelancer): ")
                UserService.register(username, password, role)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = UserService.login(username, password)
                if user:
                    current_user = user

            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            print(f"\nLogged in as: {current_user.username} ({current_user.role})")
            if current_user.role == 'freelancer':
                print("1. Create Gig")
                print("2. View My Gigs")
                print("3. View Orders Received")
                print("4. Send Message")
                print("5. View Inbox")
                print("6. View My Reviews")
                print("7. View Notifications")
                print("8. Clear Notifications")
                print("9. Logout")
            else:  # client
                print("1. View All Gigs")
                print("2. Place Order for Gig")
                print("3. View My Orders")
                print("4. Send Message")
                print("5. View Inbox")
                print("6. Leave Review")
                print("7. View Notifications")
                print("8. Clear Notifications")
                print("9. Logout")

            choice = input("Enter choice: ")

            if current_user.role == 'freelancer':
                if choice == '1':
                    title = input("Enter gig title: ")
                    description = input("Enter gig description: ")
                    price = float(input("Enter gig price: "))
                    GigService.create_gig(title, description, price, current_user.username)

                elif choice == '2':
                    GigService.list_all_gigs()

                elif choice == '3':
                    OrderService.view_freelancer_orders(current_user.username)

                elif choice == '4':
                    receiver = input("Enter receiver username: ")
                    content = input("Enter message: ")
                    MessageService.send_message(current_user.username, receiver, content)

                elif choice == '5':
                    MessageService.view_inbox(current_user.username)

                elif choice == '6':
                    ReviewService.view_reviews(current_user.username)

                elif choice == '7':
                    NotificationService.view_notifications(current_user.username)

                elif choice == '8':
                    NotificationService.clear_notifications(current_user.username)

                elif choice == '9':
                    current_user = None
                    print("Logged out successfully.")

                else:
                    print("Invalid choice.")
            else:
                if choice == '1':
                    GigService.list_all_gigs()

                elif choice == '2':
                    GigService.list_all_gigs()
                    gig_choice = int(input("Enter gig number to order: "))
                    OrderService.place_order(gig_choice, current_user.username)

                elif choice == '3':
                    OrderService.view_client_orders(current_user.username)

                elif choice == '4':
                    receiver = input("Enter receiver username: ")
                    content = input("Enter message: ")
                    MessageService.send_message(current_user.username, receiver, content)

                elif choice == '5':
                    MessageService.view_inbox(current_user.username)

                elif choice == '6':
                    freelancer_username = input("Enter freelancer username to review: ")
                    rating = int(input("Enter rating (1-5): "))
                    comment = input("Enter comment: ")
                    ReviewService.leave_review(freelancer_username, current_user.username, rating, comment)

                elif choice == '7':
                    NotificationService.view_notifications(current_user.username)

                elif choice == '8':
                    NotificationService.clear_notifications(current_user.username)

                elif choice == '9':
                    current_user = None
                    print("Logged out successfully.")

                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
