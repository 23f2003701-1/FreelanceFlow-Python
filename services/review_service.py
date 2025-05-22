from database import mock_db
from models.review import Review

class ReviewService:
    @staticmethod
    def leave_review(freelancer_username, client_username, rating, comment):
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return
        review = Review(freelancer_username, client_username, rating, comment)
        mock_db.reviews.append(review)
        print(f"Review added for {freelancer_username}.")

    @staticmethod
    def view_reviews(freelancer_username):
        reviews = [review for review in mock_db.reviews if review.freelancer_username == freelancer_username]
        if not reviews:
            print("No reviews yet.")
            return
        for idx, review in enumerate(reviews, start=1):
            print(f"{idx}. {review}\n")
