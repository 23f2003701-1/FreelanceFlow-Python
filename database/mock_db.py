from database import mock_db
from models.user import User
from models.gig import Gig
from models.order import Order
from models.message import Message
from models.notification import Notification

users = []
gigs = []  
orders = []
messages = []
reviews = []
notifications = []

def add_sample_users():
    mock_db.users.append(User("john_doe", "password123", "client"))
    mock_db.users.append(User("jane_smith", "password123", "client"))
    mock_db.users.append(User("alice_williams", "password123", "freelancer"))
    mock_db.users.append(User("bob_jones", "password123", "freelancer"))

# Add sample gigs (freelancers' services)
def add_sample_gigs():
    mock_db.gigs.append(Gig("Web Development", "Build a custom website", 500, "alice_williams"))
    mock_db.gigs.append(Gig("Graphic Design", "Create custom logos", 300, "bob_jones"))
    mock_db.gigs.append(Gig("SEO Optimization", "Improve website rankings", 250, "alice_williams"))

# Add sample orders (clients ordering gigs)
def add_sample_orders():
    mock_db.orders.append(Order(mock_db.gigs[0], "john_doe"))
    mock_db.orders.append(Order(mock_db.gigs[1], "jane_smith"))
    mock_db.orders.append(Order(mock_db.gigs[2], "john_doe"))

# Add sample messages (between users)
def add_sample_messages():
    mock_db.messages.append(Message("john_doe", "alice_williams", "I’m interested in your web development service"))
    mock_db.messages.append(Message("jane_smith", "bob_jones", "Could you create a new logo for my brand?"))
    mock_db.messages.append(Message("alice_williams", "john_doe", "Your website project is underway!"))

# Add sample notifications (for user events)
def add_sample_notifications():
    mock_db.notifications.append(Notification("john_doe", "New message from alice_williams"))
    mock_db.notifications.append(Notification("jane_smith", "New order placed for your gig: Graphic Design"))
    mock_db.notifications.append(Notification("bob_jones", "New order placed for your gig: SEO Optimization"))

# Populate the mock database with sample data
def populate_sample_data():
    add_sample_users()
    add_sample_gigs()
    add_sample_orders()
    add_sample_messages()
    add_sample_notifications()

    print("Sample data added successfully!")
