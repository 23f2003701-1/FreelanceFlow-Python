class Gig:
    def __init__(self, title, description, price, freelancer_username):
        self.title = title
        self.description = description
        self.price = price
        self.freelancer_username = freelancer_username

    def __str__(self):
        return f"{self.title} - ${self.price} by {self.freelancer_username}\n{self.description}"