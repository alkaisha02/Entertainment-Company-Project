import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Supplier import Supplier
from Suppliers.EntertainmentCompany import EntertainmentCompany

class EntertainmentCompanyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Entertainment Company Supplier Management System")
        self.master.geometry("800x700")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up welcome label
        welcome_label = tk.Label(self.master, text="Welcome to Entertainment Company Supplier Management System", font=("Arial", 18), fg="blue", bg="white")
        welcome_label.pack(pady=20)

        # Set up labels and entry fields for entertainment company supplier details
        self.setup_entertainment_company_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_entertainment_company_widgets(self):
        # Set up labels and entry fields for entertainment company supplier details
        entertainment_company_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Entertainment Type:", "Services Offered:"]
        self.entertainment_company_entries = {}
        for i, label_text in enumerate(entertainment_company_labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(pady=5, fill="x")
        
            label = tk.Label(frame, text=label_text, fg="blue", bg="white", font=("Arial", 16))  # Blue label color, font size 16
            label.pack(side="left", padx=(10, 5), pady=5)  # Align labels to the left
        
            entry = tk.Entry(frame, width=50)
            entry.pack(side="right", padx=(5, 10), pady=5, fill="x")  # Align entry fields to the right
            self.entertainment_company_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        entertainment_company_button_texts = ["Add Entertainment Company", "Display Entertainment Companies", "Delete Entertainment Company", "Modify Entertainment Company"]
        entertainment_company_button_commands = [self.add_entertainment_company, self.display_entertainment_companies, self.delete_entertainment_company, self.modify_entertainment_company]
        for i, text in enumerate(entertainment_company_button_texts):
            button = tk.Button(self.master, text=text, command=entertainment_company_button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_entertainment_company(self):
        supplier_id = self.entertainment_company_entries["Supplier ID:"].get()
        # Check if an entertainment company supplier with the same ID already exists
        try:
            existing_entertainment_companies = DataHandler.load_data("entertainment_companies_data.pkl")
            for company in existing_entertainment_companies:
                if company.supplier_id == supplier_id:
                    messagebox.showerror("Error", "An entertainment company supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing entertainment companies, so no need to check
        
        # Get other entertainment company supplier details from entry fields
        name = self.entertainment_company_entries["Name:"].get()
        address = self.entertainment_company_entries["Address:"].get()
        contact_details = self.entertainment_company_entries["Contact Details:"].get()
        entertainment_type = self.entertainment_company_entries["Entertainment Type:"].get()
        services_offered = self.entertainment_company_entries["Services Offered:"].get()

        # Create an EntertainmentCompany object
        entertainment_company = EntertainmentCompany(supplier_id, name, address, contact_details, entertainment_type, services_offered)

        # Load existing entertainment company supplier data or create an empty list if not found
        try:
            existing_entertainment_companies = DataHandler.load_data("entertainment_companies_data.pkl")
        except FileNotFoundError:
            existing_entertainment_companies = []

        # Add the new entertainment company supplier to the existing list
        existing_entertainment_companies.append(entertainment_company)

        # Save the updated entertainment company supplier data
        DataHandler.save_data(existing_entertainment_companies, "entertainment_companies_data.pkl")

        messagebox.showinfo("Success", "Entertainment company supplier added successfully.")

    def display_entertainment_companies(self):
        # Display functionality for entertainment company suppliers
        supplier_id = self.entertainment_company_entries["Supplier ID:"].get()
        try:
            existing_entertainment_companies = DataHandler.load_data("entertainment_companies_data.pkl")
            display_text = ""
            for company in existing_entertainment_companies:
                if company.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {company.supplier_id}\n"
                    display_text += f"Name: {company.name}\n"
                    display_text += f"Address: {company.address}\n"
                    display_text += f"Contact Details: {company.contact_details}\n"
                    display_text += f"Entertainment Type: {company.entertainment_type}\n"
                    display_text += f"Services Offered: {company.services_offered}\n"
                    break  # Exit loop once the entertainment company supplier is found
            else:
                messagebox.showinfo("Error", "Entertainment company supplier not found.")
                return
            messagebox.showinfo("Entertainment Company Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Entertainment Companies", "No entertainment company suppliers found.")

    def delete_entertainment_company(self):
        # Delete functionality for entertainment company suppliers
        supplier_id = self.entertainment_company_entries["Supplier ID:"].get()
        try:
            existing_entertainment_companies = DataHandler.load_data("entertainment_companies_data.pkl")
            for company in existing_entertainment_companies:
                if company.supplier_id == supplier_id:
                    existing_entertainment_companies.remove(company)
                    DataHandler.save_data(existing_entertainment_companies, "entertainment_companies_data.pkl")
                    messagebox.showinfo("Success", "Entertainment company supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Entertainment company supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No entertainment company suppliers found.")

    def modify_entertainment_company(self):
        # Modify functionality for entertainment company suppliers
        supplier_id = self.entertainment_company_entries["Supplier ID:"].get()
        try:
            existing_entertainment_companies = DataHandler.load_data("entertainment_companies_data.pkl")
            for company in existing_entertainment_companies:
                if company.supplier_id == supplier_id:
                    # Update entertainment company supplier details
                    company.name = self.entertainment_company_entries["Name:"].get()
                    company.address = self.entertainment_company_entries["Address:"].get()
                    company.contact_details = self.entertainment_company_entries["Contact Details:"].get()
                    company.entertainment_type = self.entertainment_company_entries["Entertainment Type:"].get()
                    company.services_offered = self.entertainment_company_entries["Services Offered:"].get()
                    DataHandler.save_data(existing_entertainment_companies, "entertainment_companies_data.pkl")
                    messagebox.showinfo("Success", "Entertainment company supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Entertainment company supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No entertainment company suppliers found.")

def main():
    root = tk.Tk()
    app = EntertainmentCompanyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
