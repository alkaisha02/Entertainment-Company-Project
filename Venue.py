class Venue:
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display_details(self):
        """
        Method to display the details of the venue.
        """
        print("Venue ID:", self.venue_id)
       
