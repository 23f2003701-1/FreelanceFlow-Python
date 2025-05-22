from database import mock_db
from models.user import User

class UserService:
    @staticmethod
    def register(username, password, role):
        if role not in ["client", "freelancer"]:
            print("Role must be either 'client' or 'freelancer'.")
            return
        if any(user.username == username for user in mock_db.users):
            print("Username already taken!")
            return
        new_user = User(username, password, role)
        mock_db.users.append(new_user)
        print(f"User '{username}' registered successfully as a {role}.")
        return new_user

    @staticmethod
    def login(username, password):
        for user in mock_db.users:
            if user.username == username and user.password == password:
                print(f"Welcome back, {user.username}!")
                return user
        print("Invalid username or password.")
        return None
