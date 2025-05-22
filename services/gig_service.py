from database import mock_db
from models.gig import Gig

class GigService:
    @staticmethod
    def create_gig(title, description, price, freelancer_username):
        gig = Gig(title, description, price, freelancer_username)
        mock_db.gigs.append(gig)
        print(f"Gig '{title}' created successfully!")

    @staticmethod
    def list_all_gigs():
        if not mock_db.gigs:
            print("No gigs available yet.")
            return
        for idx, gig in enumerate(mock_db.gigs, start=1):
            print(f"{idx}. {gig}\n")
