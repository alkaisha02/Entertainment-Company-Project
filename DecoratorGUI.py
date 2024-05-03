import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Supplier import Supplier
from Suppliers.Decorator import Decorator

class DecoratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Decorator Supplier Management System")
        self.master.geometry("800x650")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color

        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Decorator Supplier Management System", font=("Arial", 24), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for decorator supplier details
        self.setup_decorator_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_decorator_widgets(self):
        # Set up labels and entry fields for decorator supplier details
        decorator_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Decoration Theme:", "Decoration Style:"]
        self.decorator_entries = {}
        for label_text in decorator_labels:
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.decorator_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        decorator_button_texts = ["Add Decorator Supplier", "Display Decorators", "Delete Decorator", "Modify Decorator"]
        decorator_button_commands = [self.add_decorator, self.display_decorators, self.delete_decorator, self.modify_decorator]
        for i, text in enumerate(decorator_button_texts):
            button = tk.Button(self.master, text=text, command=decorator_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_decorator(self):
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        # Check if a decorator supplier with the same ID already exists
        try:
            existing_decorators = DataHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A decorator supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing decorators, so no need to check
        
        # Get other decorator supplier details from entry fields
        name = self.decorator_entries["Name:"].get()
        address = self.decorator_entries["Address:"].get()
        contact_details = self.decorator_entries["Contact Details:"].get()
        decoration_theme = self.decorator_entries["Decoration Theme:"].get()
        decoration_style = self.decorator_entries["Decoration Style:"].get()

        # Create a Decorator object
        decorator = Decorator(supplier_id, name, address, contact_details, decoration_theme, decoration_style)

        # Load existing decorator supplier data or create an empty list if not found
        try:
            existing_decorators = DataHandler.load_data("decorators_data.pkl")
        except FileNotFoundError:
            existing_decorators = []

        # Add the new decorator supplier to the existing list
        existing_decorators.append(decorator)

        # Save the updated decorator supplier data
        DataHandler.save_data(existing_decorators, "decorators_data.pkl")

        messagebox.showinfo("Success", "Decorator supplier added successfully.")

    def display_decorators(self):
        # Display functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = DataHandler.load_data("decorators_data.pkl")
            display_text = ""
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {decorator.supplier_id}\n"
                    display_text += f"Name: {decorator.name}\n"
                    display_text += f"Address: {decorator.address}\n"
                    display_text += f"Contact Details: {decorator.contact_details}\n"
                    display_text += f"Decoration Theme: {decorator.decoration_theme}\n"
                    display_text += f"Decoration Style: {decorator.decoration_style}\n"
                    break  # Exit loop once the decorator supplier is found
            else:
                messagebox.showinfo("Error", "Decorator supplier not found.")
                return
            messagebox.showinfo("Decorator Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Decorators", "No decorator suppliers found.")

    def delete_decorator(self):
        # Delete functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = DataHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    existing_decorators.remove(decorator)
                    DataHandler.save_data(existing_decorators, "decorators_data.pkl")
                    messagebox.showinfo("Success", "Decorator supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Decorator supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No decorator suppliers found.")

    def modify_decorator(self):
        # Modify functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = DataHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    # Update decorator supplier details
                    decorator.name = self.decorator_entries["Name:"].get()
                    decorator.address = self.decorator_entries["Address:"].get()
                    decorator.contact_details = self.decorator_entries["Contact Details:"].get()
                    decorator.decoration_theme = self.decorator_entries["Decoration Theme:"].get()
                    decorator.decoration_style = self.decorator_entries["Decoration Style:"].get()
                    DataHandler.save_data(existing_decorators, "decorators_data.pkl")
                    messagebox.showinfo("Success", "Decorator supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Decorator supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No decorator suppliers found.")

def main():
    root = tk.Tk()
    app = DecoratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
