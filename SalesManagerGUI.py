import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.SalesManager import SalesManager

class SalesManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Manager Management System")
        self.master.geometry("500x600")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up labels and entry fields for sales manager details
        self.setup_sales_manager_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_sales_manager_widgets(self):
        # Set up labels and entry fields for sales manager details
        sales_manager_labels = ["Name:", "Employee ID:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:", "Team Size:"]
        self.sales_manager_entries = {}
        for i, label_text in enumerate(sales_manager_labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(fill="x", padx=10, pady=5)
        
            label = tk.Label(frame, text=label_text, bg="white", font=("Arial", 12))
            label.pack(side="left", padx=5, pady=5)
        
            entry = tk.Entry(frame)
            entry.pack(side="right", padx=5, pady=5, fill="x", expand=True)
            self.sales_manager_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        sales_manager_button_texts = ["Add Sales Manager", "Display Sales Managers", "Delete Sales Manager", "Modify Sales Manager"]
        sales_manager_button_commands = [self.add_sales_manager, self.display_sales_managers, self.delete_sales_manager, self.modify_sales_manager]
        for i, text in enumerate(sales_manager_button_texts):
            button = tk.Button(self.master, text=text, command=sales_manager_button_commands[i], bg="blue", fg="white", width=30)
            button.pack(pady=5)

    def add_sales_manager(self):
        employee_id = self.sales_manager_entries["Employee ID:"].get()
        # Check if a sales manager with the same ID already exists
        try:
            existing_sales_managers = DataHandler.load_data("sales_managers_data.pkl")
            for manager in existing_sales_managers:
                if manager.employee_id == employee_id:
                    messagebox.showerror("Error", "A sales manager with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing sales managers, so no need to check
        
        # Get other sales manager details from entry fields
        name = self.sales_manager_entries["Name:"].get()
        department = self.sales_manager_entries["Department:"].get()
        job_title = self.sales_manager_entries["Job Title:"].get()
        basic_salary = float(self.sales_manager_entries["Basic Salary:"].get())
        age = int(self.sales_manager_entries["Age:"].get())
        dob = self.sales_manager_entries["Date of Birth:"].get()
        passport_details = self.sales_manager_entries["Passport Details:"].get()
        team_size = int(self.sales_manager_entries["Team Size:"].get())

        # Create a SalesManager object
        sales_manager = SalesManager(name, employee_id, department, job_title, basic_salary, age, dob, passport_details, team_size)

        # Load existing sales manager data or create an empty list if not found
        try:
            existing_sales_managers = DataHandler.load_data("sales_managers_data.pkl")
        except FileNotFoundError:
            existing_sales_managers = []

        # Add the new sales manager to the existing list
        existing_sales_managers.append(sales_manager)

        # Save the updated sales manager data
        DataHandler.save_data(existing_sales_managers, "sales_managers_data.pkl")

        messagebox.showinfo("Success", "Sales manager added successfully.")

    def display_sales_managers(self):
        # Display functionality for sales managers
        employee_id = self.sales_manager_entries["Employee ID:"].get()
        try:
            existing_sales_managers = DataHandler.load_data("sales_managers_data.pkl")
            display_text = ""
            for manager in existing_sales_managers:
                if manager.employee_id == employee_id:
                    display_text += f"Name: {manager.name}\n"
                    display_text += f"Employee ID: {manager.employee_id}\n"
                    display_text += f"Department: {manager.department}\n"
                    display_text += f"Job Title: {manager.job_title}\n"
                    display_text += f"Basic Salary: {manager.basic_salary}\n"
                    display_text += f"Age: {manager.age}\n"
                    display_text += f"Date of Birth: {manager.dob}\n"
                    display_text += f"Passport Details: {manager.passport_details}\n"
                    display_text += f"Team Size: {manager.team_size}\n"
                    break  # Exit loop once the sales manager is found
            else:
                messagebox.showinfo("Error", "Sales manager not found.")
                return
            messagebox.showinfo("Sales Manager Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Sales Managers", "No sales managers found.")

    def delete_sales_manager(self):
        # Delete functionality for sales managers
        employee_id = self.sales_manager_entries["Employee ID:"].get()
        try:
            existing_sales_managers = DataHandler.load_data("sales_managers_data.pkl")
            for manager in existing_sales_managers:
                if manager.employee_id == employee_id:
                    existing_sales_managers.remove(manager)
                    DataHandler.save_data(existing_sales_managers, "sales_managers_data.pkl")
                    messagebox.showinfo("Success", "Sales manager deleted successfully.")
                    return
            messagebox.showinfo("Error", "Sales manager not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No sales managers found.")

    def modify_sales_manager(self):
        # Modify functionality for sales managers
        employee_id = self.sales_manager_entries["Employee ID:"].get()
        try:
            existing_sales_managers = DataHandler.load_data("sales_managers_data.pkl")
            for manager in existing_sales_managers:
                if manager.employee_id == employee_id:
                    # Update sales manager details
                    manager.name = self.sales_manager_entries["Name:"].get()
                    manager.department = self.sales_manager_entries["Department:"].get()
                    manager.job_title = self.sales_manager_entries["Job Title:"].get()
                    manager.basic_salary = float(self.sales_manager_entries["Basic Salary:"].get())
                    manager.age = int(self.sales_manager_entries["Age:"].get())
                    manager.dob = self.sales_manager_entries["Date of Birth:"].get()
                    manager.passport_details = self.sales_manager_entries["Passport Details:"].get()
                    manager.team_size = int(self.sales_manager_entries["Team Size:"].get())
                    DataHandler.save_data(existing_sales_managers, "sales_managers_data.pkl")
                    messagebox.showinfo("Success", "Sales manager details modified successfully.")
                    return
            messagebox.showinfo("Error", "Sales manager not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No sales managers found.")

def main():
    root = tk.Tk()
    app = SalesManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
