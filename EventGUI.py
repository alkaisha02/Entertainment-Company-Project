import tkinter as tk
from tkinter import messagebox
from Controllers.Event import Event
from Util.DataHandler import DataHandler

class EventGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")
        self.master.geometry("800x750")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Event Management System", font=("Arial", 18), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for event details
        self.setup_event_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_event_widgets(self):
        # Set up labels and entry fields for event details
        event_labels = ["Event ID:", "Type:", "Theme:", "Date:", "Time:", "Duration:", "Venue:", "Client ID:", "Guest List:", "Suppliers:"]
        self.event_entries = {}
        for i, label_text in enumerate(event_labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.event_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        event_button_texts = ["Add Event", "Display Events", "Delete Event", "Modify Event"]
        event_button_commands = [self.add_event, self.display_events, self.delete_event, self.modify_event]
        for i, text in enumerate(event_button_texts):
            button = tk.Button(self.master, text=text, command=event_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_event(self):
        # Add functionality for events
        event_id = self.event_entries["Event ID:"].get()
        # Check if an event with the same ID already exists
        try:
            existing_events = DataHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                    messagebox.showerror("Error", "An event with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing events, so no need to check
        
        # Get other event details from entry fields
        event_details = {key: entry.get() for key, entry in self.event_entries.items()}

        # Create an Event object
        event = Event(**event_details)

        # Load existing event data or create an empty list if not found
        try:
            existing_events = DataHandler.load_data("events_data.pkl")
        except FileNotFoundError:
            existing_events = []

        # Add the new event to the existing list
        existing_events.append(event)

        # Save the updated event data
        DataHandler.save_data(existing_events, "events_data.pkl")

        messagebox.showinfo("Success", "Event added successfully.")

    def display_events(self):
        # Display functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = DataHandler.load_data("events_data.pkl")
            display_text = ""
            for event in existing_events:
                if event.event_id == event_id:
                    display_text += f"Event ID: {event.event_id}\n"
                    display_text += f"Type: {event.type}\n"
                    display_text += f"Theme: {event.theme}\n"
                    display_text += f"Date: {event.date}\n"
                    display_text += f"Time: {event.time}\n"
                    display_text += f"Duration: {event.duration}\n"
                    display_text += f"Venue: {event.venue}\n"
                    display_text += f"Client ID: {event.client_id}\n"
                    display_text += f"Guest List: {', '.join(event.guest_list)}\n"
                    display_text += f"Suppliers: {', '.join(event.suppliers)}\n"
                    break  # Exit loop once the event is found
            else:
                messagebox.showinfo("Error", "Event not found.")
                return
            messagebox.showinfo("Event Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Events", "No events found.")

    def delete_event(self):
        # Delete functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = DataHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                    existing_events.remove(event)
                    DataHandler.save_data(existing_events, "events_data.pkl")
                    messagebox.showinfo("Success", "Event deleted successfully.")
                    return
            messagebox.showinfo("Error", "Event not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No events found.")

    def modify_event(self):
        # Modify functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = DataHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                    # Update event details
                    event_details = {key: entry.get() for key, entry in self.event_entries.items()}
                    event.__dict__.update(event_details)
                    DataHandler.save_data(existing_events, "events_data.pkl")
                    messagebox.showinfo("Success", "Event details modified successfully.")
                    return
            messagebox.showinfo("Error", "Event not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No events found.")

def main():
    root = tk.Tk()
    app = EventGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
