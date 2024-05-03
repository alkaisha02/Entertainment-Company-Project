class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue, client_id, guest_list, suppliers):
       
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers = suppliers

    def display_details(self):
        """
        Method to display the details of the event.
        """
        print("Event ID:", self.event_id)
        print("Type:", self.type)
        print("Theme:", self.theme)
        print("Date:", self.date)
        print("Time:", self.time)
        print("Duration:", self.duration)
        print("Venue:", self.venue)
        print("Client ID:", self.client_id)
        print("Guest List:", self.guest_list)
        print("Suppliers:", self.suppliers)
