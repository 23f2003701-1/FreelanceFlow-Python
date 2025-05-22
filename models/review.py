class Review:
    def __init__(self, freelancer_username, client_username, rating, comment):
        self.freelancer_username = freelancer_username
        self.client_username = client_username
        self.rating = rating  # rating out of 5
        self.comment = comment

    def __str__(self):
        return (f"Rating: {self.rating}/5 by {self.client_username}\n"
                f"Comment: {self.comment}")
