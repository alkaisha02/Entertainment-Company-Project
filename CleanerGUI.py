import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Supplier import Supplier
from Suppliers.Cleaner import Cleaner

class CleanerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cleaner Supplier Management System")
        self.master.geometry("800x650")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color

        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Cleaner Supplier Management System", font=("Arial", 24), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for cleaner supplier details
        self.setup_cleaner_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_cleaner_widgets(self):
        # Set up labels and entry fields for cleaner supplier details
        cleaner_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Cleaning Services:"]
        self.cleaner_entries = {}
        for label_text in cleaner_labels:
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.cleaner_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        cleaner_button_texts = ["Add Cleaner Supplier", "Display Cleaners", "Delete Cleaner", "Modify Cleaner"]
        cleaner_button_commands = [self.add_cleaner, self.display_cleaners, self.delete_cleaner, self.modify_cleaner]
        for i, text in enumerate(cleaner_button_texts):
            button = tk.Button(self.master, text=text, command=cleaner_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_cleaner(self):
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        name = self.cleaner_entries["Name:"].get()
        address = self.cleaner_entries["Address:"].get()
        contact_details = self.cleaner_entries["Contact Details:"].get()
        cleaning_services = self.cleaner_entries["Cleaning Services:"].get()
        
        if not supplier_id.strip() or not name.strip() or not address.strip() or not contact_details.strip() or not cleaning_services.strip():
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            existing_cleaners = DataHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A cleaner supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing cleaners, so no need to check
        
        cleaner = Cleaner(supplier_id, name, address, contact_details, cleaning_services)
        existing_cleaners.append(cleaner)
        DataHandler.save_data(existing_cleaners, "cleaners_data.pkl")
        messagebox.showinfo("Success", "Cleaner supplier added successfully.")

    def display_cleaners(self):
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = DataHandler.load_data("cleaners_data.pkl")
            display_text = ""
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {cleaner.supplier_id}\n"
                    display_text += f"Name: {cleaner.name}\n"
                    display_text += f"Address: {cleaner.address}\n"
                    display_text += f"Contact Details: {cleaner.contact_details}\n"
                    display_text += f"Cleaning Services: {cleaner.cleaning_services}\n"
                    break  # Exit loop once the cleaner supplier is found
            else:
                messagebox.showinfo("Error", "Cleaner supplier not found.")
                return
            messagebox.showinfo("Cleaner Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Cleaners", "No cleaner suppliers found.")

    def delete_cleaner(self):
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = DataHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    existing_cleaners.remove(cleaner)
                    DataHandler.save_data(existing_cleaners, "cleaners_data.pkl")
                    messagebox.showinfo("Success", "Cleaner supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Cleaner supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No cleaner suppliers found.")

    def modify_cleaner(self):
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = DataHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    cleaner.name = self.cleaner_entries["Name:"].get()
                    cleaner.address = self.cleaner_entries["Address:"].get()
                    cleaner.contact_details = self.cleaner_entries["Contact Details:"].get()
                    cleaner.cleaning_services = self.cleaner_entries["Cleaning Services:"].get()
                    DataHandler.save_data(existing_cleaners, "cleaners_data.pkl")
                    messagebox.showinfo("Success", "Cleaner supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Cleaner supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No cleaner suppliers found.")

def main():
    root = tk.Tk()
    app = CleanerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
