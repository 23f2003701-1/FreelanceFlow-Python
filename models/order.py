class Order:
    def __init__(self, gig, client_username):
        self.gig = gig
        self.client_username = client_username
        self.freelancer_username = gig.freelancer_username
        self.status = 'pending'  

    def __str__(self):
        return (f"Order for '{self.gig.title}' (${self.gig.price}) "
                f"by {self.client_username} -> {self.freelancer_username} | Status: {self.status}")
