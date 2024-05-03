import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Guest import Guest

class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guest Management System")
        self.master.geometry("800x500")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Guest Management System", font=("Arial", 24), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for guest details
        self.setup_guest_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_guest_widgets(self):
        labels = ["Guest ID:", "Name:", "Address:", "Contact Details:"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.entries[label_text] = entry

    def setup_buttons(self):
        button_texts = ["Add Guest", "Display Guests", "Delete Guest", "Modify Guest"]
        button_commands = [self.add_guest, self.display_guests, self.delete_guest, self.modify_guest]
        for i, text in enumerate(button_texts):
            button = tk.Button(self.master, text=text, command=button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_guest(self):
        guest_id = self.entries["Guest ID:"].get()
        # Check if a guest with the same ID already exists
        try:
            existing_guests = DataHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    messagebox.showerror("Error", "A guest with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing guests, so no need to check
        
        # Get other guest details from entry fields
        name = self.entries["Name:"].get()
        address = self.entries["Address:"].get()
        contact_details = self.entries["Contact Details:"].get()

        # Create a Guest object
        guest = Guest(guest_id, name, address, contact_details)

        # Load existing guest data or create an empty list if not found
        try:
            existing_guests = DataHandler.load_data("guests_data.pkl")
        except FileNotFoundError:
            existing_guests = []

        # Add the new guest to the existing list
        existing_guests.append(guest)

        # Save the updated guest data
        DataHandler.save_data(existing_guests, "guests_data.pkl")

        messagebox.showinfo("Success", "Guest added successfully.")

    def display_guests(self):
        guest_id = self.entries["Guest ID:"].get()
        try:
            existing_guests = DataHandler.load_data("guests_data.pkl")
            display_text = ""
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    display_text += f"Guest ID: {guest.guest_id}\n"
                    display_text += f"Name: {guest.name}\n"
                    display_text += f"Address: {guest.address}\n"
                    display_text += f"Contact Details: {guest.contact_details}\n"
                    break  # Exit loop once the guest is found
            else:
                messagebox.showinfo("Error", "Guest not found.")
                return
            messagebox.showinfo("Guest Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Guests", "No guests found.")

    def delete_guest(self):
        guest_id = self.entries["Guest ID:"].get()
        try:
            existing_guests = DataHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    existing_guests.remove(guest)
                    DataHandler.save_data(existing_guests, "guests_data.pkl")
                    messagebox.showinfo("Success", "Guest deleted successfully.")
                    return
            messagebox.showinfo("Error", "Guest not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No guests found.")

    def modify_guest(self):
        guest_id = self.entries["Guest ID:"].get()
        try:
            existing_guests = DataHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    # Update guest details
                    guest.name = self.entries["Name:"].get()
                    guest.address = self.entries["Address:"].get()
                    guest.contact_details = self.entries["Contact Details:"].get()
                    DataHandler.save_data(existing_guests, "guests_data.pkl")
                    messagebox.showinfo("Success", "Guest details modified successfully.")
                    return
            messagebox.showinfo("Error", "Guest not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No guests found.")

def main():
    root = tk.Tk()
    app = GuestGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
