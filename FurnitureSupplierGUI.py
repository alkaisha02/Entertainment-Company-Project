import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Supplier import Supplier
from Suppliers.FurnitureSupplier import FurnitureSupplier

class FurnitureSupplierGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Furniture Supplier Management System")
        self.master.geometry("800x600")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Furniture Supplier Management System", font=("Arial", 18), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for furniture supplier details
        self.setup_furniture_supplier_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_furniture_supplier_widgets(self):
        # Set up labels and entry fields for furniture supplier details
        furniture_supplier_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Furniture Type:", "Rental Options:"]
        self.furniture_supplier_entries = {}
        for i, label_text in enumerate(furniture_supplier_labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, font=("Arial", 14), fg="blue", bg="white")  # Blue label color, font size 14
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.furniture_supplier_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        furniture_supplier_button_texts = ["Add Furniture Supplier", "Display Furniture Suppliers", "Delete Furniture Supplier", "Modify Furniture Supplier"]
        furniture_supplier_button_commands = [self.add_furniture_supplier, self.display_furniture_suppliers, self.delete_furniture_supplier, self.modify_furniture_supplier]
        for i, text in enumerate(furniture_supplier_button_texts):
            button = tk.Button(self.master, text=text, command=furniture_supplier_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_furniture_supplier(self):
        supplier_id = self.furniture_supplier_entries["Supplier ID:"].get()
        # Check if a furniture supplier with the same ID already exists
        try:
            existing_furniture_suppliers = DataHandler.load_data("furniture_suppliers_data.pkl")
            for supplier in existing_furniture_suppliers:
                if supplier.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A furniture supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing furniture suppliers, so no need to check
        
        # Get other furniture supplier details from entry fields
        name = self.furniture_supplier_entries["Name:"].get()
        address = self.furniture_supplier_entries["Address:"].get()
        contact_details = self.furniture_supplier_entries["Contact Details:"].get()
        furniture_type = self.furniture_supplier_entries["Furniture Type:"].get()
        rental_options = self.furniture_supplier_entries["Rental Options:"].get()

        # Create a FurnitureSupplier object
        furniture_supplier = FurnitureSupplier(supplier_id, name, address, contact_details, furniture_type, rental_options)

        # Load existing furniture supplier data or create an empty list if not found
        try:
            existing_furniture_suppliers = DataHandler.load_data("furniture_suppliers_data.pkl")
        except FileNotFoundError:
            existing_furniture_suppliers = []

        # Add the new furniture supplier to the existing list
        existing_furniture_suppliers.append(furniture_supplier)

        # Save the updated furniture supplier data
        DataHandler.save_data(existing_furniture_suppliers, "furniture_suppliers_data.pkl")

        messagebox.showinfo("Success", "Furniture supplier added successfully.")

    def display_furniture_suppliers(self):
        # Display functionality for furniture suppliers
        supplier_id = self.furniture_supplier_entries["Supplier ID:"].get()
        try:
            existing_furniture_suppliers = DataHandler.load_data("furniture_suppliers_data.pkl")
            display_text = ""
            for supplier in existing_furniture_suppliers:
                if supplier.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {supplier.supplier_id}\n"
                    display_text += f"Name: {supplier.name}\n"
                    display_text += f"Address: {supplier.address}\n"
                    display_text += f"Contact Details: {supplier.contact_details}\n"
                    display_text += f"Furniture Type: {supplier.furniture_type}\n"
                    display_text += f"Rental Options: {supplier.rental_options}\n"
                    break  # Exit loop once the furniture supplier is found
            else:
                messagebox.showinfo("Error", "Furniture supplier not found.")
                return
            messagebox.showinfo("Furniture Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Furniture Suppliers", "No furniture suppliers found.")

    def delete_furniture_supplier(self):
        # Delete functionality for furniture suppliers
        supplier_id = self.furniture_supplier_entries["Supplier ID:"].get()
        try:
            existing_furniture_suppliers = DataHandler.load_data("furniture_suppliers_data.pkl")
            for supplier in existing_furniture_suppliers:
                if supplier.supplier_id == supplier_id:
                    existing_furniture_suppliers.remove(supplier)
                    DataHandler.save_data(existing_furniture_suppliers, "furniture_suppliers_data.pkl")
                    messagebox.showinfo("Success", "Furniture supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Furniture supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No furniture suppliers found.")

    def modify_furniture_supplier(self):
        # Modify functionality for furniture suppliers
        supplier_id = self.furniture_supplier_entries["Supplier ID:"].get()
        try:
            existing_furniture_suppliers = DataHandler.load_data("furniture_suppliers_data.pkl")
            for supplier in existing_furniture_suppliers:
                if supplier.supplier_id == supplier_id:
                    # Update furniture supplier details
                    supplier.name = self.furniture_supplier_entries["Name:"].get()
                    supplier.address = self.furniture_supplier_entries["Address:"].get()
                    supplier.contact_details = self.furniture_supplier_entries["Contact Details:"].get()
                    supplier.furniture_type = self.furniture_supplier_entries["Furniture Type:"].get()
                    supplier.rental_options = self.furniture_supplier_entries["Rental Options:"].get()
                    DataHandler.save_data(existing_furniture_suppliers, "furniture_suppliers_data.pkl")
                    messagebox.showinfo("Success", "Furniture supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Furniture supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No furniture suppliers found.")

def main():
    root = tk.Tk()
    app = FurnitureSupplierGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
