import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Employee import Employee
from Entities.Salesperson import Salesperson

class SalespersonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Salesperson Management System")
        self.master.geometry("500x600")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up labels and entry fields for salesperson details
        self.setup_salesperson_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_salesperson_widgets(self):
        # Set up labels and entry fields for salesperson details
        salesperson_labels = ["Name:", "Employee ID:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:", "Sales Targets:"]
        self.salesperson_entries = {}
        for i, label_text in enumerate(salesperson_labels):
            frame = tk.Frame(self.master, bg="white")
            frame.pack(fill="x", padx=10, pady=5)
        
            label = tk.Label(frame, text=label_text, bg="white", font=("Arial", 12))
            label.pack(side="left", padx=5, pady=5)
        
            entry = tk.Entry(frame)
            entry.pack(side="right", padx=5, pady=5, fill="x", expand=True)
            self.salesperson_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        salesperson_button_texts = ["Add Salesperson", "Display Salespersons", "Delete Salesperson", "Modify Salesperson"]
        salesperson_button_commands = [self.add_salesperson, self.display_salespersons, self.delete_salesperson, self.modify_salesperson]
        for i, text in enumerate(salesperson_button_texts):
            button = tk.Button(self.master, text=text, command=salesperson_button_commands[i], bg="blue", fg="white", width=30)
            button.pack(pady=5)

    def add_salesperson(self):
        employee_id = self.salesperson_entries["Employee ID:"].get()
        # Check if a salesperson with the same ID already exists
        try:
            existing_salespersons = DataHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    messagebox.showerror("Error", "A salesperson with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing salespersons, so no need to check
        
        # Get other salesperson details from entry fields
        name = self.salesperson_entries["Name:"].get()
        department = self.salesperson_entries["Department:"].get()
        job_title = self.salesperson_entries["Job Title:"].get()
        basic_salary = float(self.salesperson_entries["Basic Salary:"].get())
        age = int(self.salesperson_entries["Age:"].get())
        dob = self.salesperson_entries["Date of Birth:"].get()
        passport_details = self.salesperson_entries["Passport Details:"].get()
        sales_targets = float(self.salesperson_entries["Sales Targets:"].get())

        # Create a Salesperson object
        salesperson = Salesperson(name, employee_id, department, job_title, basic_salary, age, dob, passport_details, sales_targets)

        # Load existing salesperson data or create an empty list if not found
        try:
            existing_salespersons = DataHandler.load_data("salespersons_data.pkl")
        except FileNotFoundError:
            existing_salespersons = []

        # Add the new salesperson to the existing list
        existing_salespersons.append(salesperson)

        # Save the updated salesperson data
        DataHandler.save_data(existing_salespersons, "salespersons_data.pkl")

        messagebox.showinfo("Success", "Salesperson added successfully.")

    def display_salespersons(self):
        # Display functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = DataHandler.load_data("salespersons_data.pkl")
            display_text = ""
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    display_text += f"Name: {salesperson.name}\n"
                    display_text += f"Employee ID: {salesperson.employee_id}\n"
                    display_text += f"Department: {salesperson.department}\n"
                    display_text += f"Job Title: {salesperson.job_title}\n"
                    display_text += f"Basic Salary: {salesperson.basic_salary}\n"
                    display_text += f"Age: {salesperson.age}\n"
                    display_text += f"Date of Birth: {salesperson.dob}\n"
                    display_text += f"Passport Details: {salesperson.passport_details}\n"
                    display_text += f"Sales Targets: {salesperson.sales_targets}\n"
                    break  # Exit loop once the salesperson is found
            else:
                messagebox.showinfo("Error", "Salesperson not found.")
                return
            messagebox.showinfo("Salesperson Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Salespersons", "No salespersons found.")

    def delete_salesperson(self):
        # Delete functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = DataHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    existing_salespersons.remove(salesperson)
                    DataHandler.save_data(existing_salespersons, "salespersons_data.pkl")
                    messagebox.showinfo("Success", "Salesperson deleted successfully.")
                    return
            messagebox.showinfo("Error", "Salesperson not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No salespersons found.")

    def modify_salesperson(self):
        # Modify functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = DataHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    # Update salesperson details
                    salesperson.name = self.salesperson_entries["Name:"].get()
                    salesperson.department = self.salesperson_entries["Department:"].get()
                    salesperson.job_title = self.salesperson_entries["Job Title:"].get()
                    salesperson.basic_salary = float(self.salesperson_entries["Basic Salary:"].get())
                    salesperson.age = int(self.salesperson_entries["Age:"].get())
                    salesperson.dob = self.salesperson_entries["Date of Birth:"].get()
                    salesperson.passport_details = self.salesperson_entries["Passport Details:"].get()
                    salesperson.sales_targets = float(self.salesperson_entries["Sales Targets:"].get())
                    DataHandler.save_data(existing_salespersons, "salespersons_data.pkl")
                    messagebox.showinfo("Success", "Salesperson details modified successfully.")
                    return
            messagebox.showinfo("Error", "Salesperson not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No salespersons found.")

def main():
    root = tk.Tk()
    app = SalespersonGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
