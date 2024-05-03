import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Supplier import Supplier
from Suppliers.Caterer import Caterer

class CatererGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Caterer Supplier Management System")
        self.master.geometry("800x650")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color

        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Caterer Supplier Management System", font=("Arial", 24), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for caterer supplier details
        self.setup_caterer_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_caterer_widgets(self):
    # Set up labels and entry fields for caterer supplier details
        caterer_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Menu:", "Minimum Guests:", "Maximum Guests:"]
        self.caterer_entries = {}
        for label_text in caterer_labels:
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.caterer_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        caterer_button_texts = ["Add Caterer Supplier", "Display Caterers", "Delete Caterer", "Modify Caterer"]
        caterer_button_commands = [self.add_caterer, self.display_caterers, self.delete_caterer, self.modify_caterer]
        for i, text in enumerate(caterer_button_texts):
            button = tk.Button(self.master, text=text, command=caterer_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_caterer(self):
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        # Check if a caterer supplier with the same ID already exists
        try:
            existing_caterers = DataHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A caterer supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing caterers, so no need to check
        
        # Get other caterer supplier details from entry fields
        name = self.caterer_entries["Name:"].get()
        address = self.caterer_entries["Address:"].get()
        contact_details = self.caterer_entries["Contact Details:"].get()
        menu = self.caterer_entries["Menu:"].get()
        min_guests = self.caterer_entries["Minimum Guests:"].get()
        max_guests = self.caterer_entries["Maximum Guests:"].get()

        # Create a Caterer object
        caterer = Caterer(supplier_id, name, address, contact_details, menu, min_guests, max_guests)

        # Load existing caterer supplier data or create an empty list if not found
        try:
            existing_caterers = DataHandler.load_data("caterers_data.pkl")
        except FileNotFoundError:
            existing_caterers = []

        # Add the new caterer supplier to the existing list
        existing_caterers.append(caterer)

        # Save the updated caterer supplier data
        DataHandler.save_data(existing_caterers, "caterers_data.pkl")

        messagebox.showinfo("Success", "Caterer supplier added successfully.")

    def display_caterers(self):
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = DataHandler.load_data("caterers_data.pkl")
            display_text = ""
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {caterer.supplier_id}\n"
                    display_text += f"Name: {caterer.name}\n"
                    display_text += f"Address: {caterer.address}\n"
                    display_text += f"Contact Details: {caterer.contact_details}\n"
                    display_text += f"Menu: {caterer.menu}\n"
                    display_text += f"Minimum Guests: {caterer.min_guests}\n"
                    display_text += f"Maximum Guests: {caterer.max_guests}\n"
                    break  # Exit loop once the caterer supplier is found
            else:
                messagebox.showinfo("Error", "Caterer supplier not found.")
                return
            messagebox.showinfo("Caterer Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Caterers", "No caterer suppliers found.")

    def delete_caterer(self):
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = DataHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    existing_caterers.remove(caterer)
                    DataHandler.save_data(existing_caterers, "caterers_data.pkl")
                    messagebox.showinfo("Success", "Caterer supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Caterer supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No caterer suppliers found.")

    def modify_caterer(self):
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = DataHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    caterer.name = self.caterer_entries["Name:"].get()
                    caterer.address = self.caterer_entries["Address:"].get()
                    caterer.contact_details = self.caterer_entries["Contact Details:"].get()
                    caterer.menu = self.caterer_entries["Menu:"].get()
                    caterer.min_guests = self.caterer_entries["Minimum Guests:"].get()
                    caterer.max_guests = self.caterer_entries["Maximum Guests:"].get()
                    DataHandler.save_data(existing_caterers, "caterers_data.pkl")
                    messagebox.showinfo("Success", "Caterer supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Caterer supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No caterer suppliers found.")

def main():
    root = tk.Tk()
    app = CatererGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
