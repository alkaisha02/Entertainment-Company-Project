import tkinter as tk
from tkinter import messagebox
from Util.DataHandler import DataHandler
from Entities.Employee import Employee

class EmployeeGUI:      
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")
        self.master.geometry("800x700")  # Set window dimensions
        self.master.configure(bg="white")  # Set background color
        
        # Set up labels and entry fields for employee details
        self.setup_employee_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_employee_widgets(self):
        labels = ["Employee ID:", "Name:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:"]
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
        button_texts = ["Add Employee", "Display Employees", "Delete Employee", "Modify Employee", "Search Employee"]
        button_commands = [self.add_employee, self.display_employees, self.delete_employee, self.modify_employee, self.search_employee]
        for i, text in enumerate(button_texts):
            button = tk.Button(self.master, text=text, command=button_commands[i], bg="blue", fg="white", width=30)  # Blue button with white text
            button.pack(pady=5)  # Add padding

    def add_employee(self):
        employee_id = self.entries["Employee ID:"].get()
        # Check if an employee with the same ID already exists
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
            for employee in existing_employees:
                if employee.employee_id == employee_id:
                    messagebox.showerror("Error", "An employee with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing employees, so no need to check
        
        # Get other employee details from entry fields
        name = self.entries["Name:"].get()
        department = self.entries["Department:"].get()
        job_title = self.entries["Job Title:"].get()
        basic_salary = float(self.entries["Basic Salary:"].get())
        age = int(self.entries["Age:"].get())
        dob = self.entries["Date of Birth:"].get()
        passport_details = self.entries["Passport Details:"].get()

        # Create an Employee object
        employee = Employee(name, employee_id, department, job_title, basic_salary, age, dob, passport_details)

        # Load existing employee data or create an empty list if not found
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
        except FileNotFoundError:
            existing_employees = []

        # Add the new employee to the existing list
        existing_employees.append(employee)

        # Save the updated employee data
        DataHandler.save_data(existing_employees, "employees_data.pkl")

        messagebox.showinfo("Success", "Employee added successfully.")

    def display_employees(self):
        employee_id = self.entries["Employee ID:"].get()
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
            display_text = ""
            for employee in existing_employees:
                if employee.employee_id == employee_id:
                    display_text += f"Employee ID: {employee.employee_id}\n"
                    display_text += f"Name: {employee.name}\n"
                    display_text += f"Department: {employee.department}\n"
                    display_text += f"Job Title: {employee.job_title}\n"
                    display_text += f"Basic Salary: {employee.basic_salary}\n"
                    display_text += f"Age: {employee.age}\n"
                    display_text += f"Date of Birth: {employee.dob}\n"
                    display_text += f"Passport Details: {employee.passport_details}\n"
                    break  # Exit loop once the employee is found
            else:
                messagebox.showinfo("Error", "Employee not found.")
                return
            messagebox.showinfo("Employee Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Employees", "No employees found.")

    def delete_employee(self):
        employee_id = self.entries["Employee ID:"].get()
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
            for employee in existing_employees:
                if employee.employee_id == employee_id:
                    existing_employees.remove(employee)
                    DataHandler.save_data(existing_employees, "employees_data.pkl")
                    messagebox.showinfo("Success", "Employee deleted successfully.")
                    return
            messagebox.showinfo("Error", "Employee not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No employees found.")

    def modify_employee(self):
        employee_id = self.entries["Employee ID:"].get()
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
            for employee in existing_employees:
                if employee.employee_id == employee_id:
                    # Update employee details
                    employee.name = self.entries["Name:"].get()
                    employee.department = self.entries["Department:"].get()
                    employee.job_title = self.entries["Job Title:"].get()
                    employee.basic_salary = float(self.entries["Basic Salary:"].get())
                    employee.age = int(self.entries["Age:"].get())
                    employee.dob = self.entries["Date of Birth:"].get()
                    employee.passport_details = self.entries["Passport Details:"].get()

                    DataHandler.save_data(existing_employees, "employees_data.pkl")
                    messagebox.showinfo("Success", "Employee details modified successfully.")
                    return
            messagebox.showinfo("Error", "Employee not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No employees found.")
    
    def search_employee(self):
        employee_id = self.entries["Employee ID:"].get()
        try:
            existing_employees = DataHandler.load_data("employees_data.pkl")
            for employee in existing_employees:
                if employee.employee_id == employee_id:
                    # Display employee details in the entry fields
                    self.entries["Name:"].delete(0, tk.END)
                    self.entries["Name:"].insert(0, employee.name)
                    self.entries["Department:"].delete(0, tk.END)
                    self.entries["Department:"].insert(0, employee.department)
                    self.entries["Job Title:"].delete(0, tk.END)
                    self.entries["Job Title:"].insert(0, employee.job_title)
                    self.entries["Basic Salary:"].delete(0, tk.END)
                    self.entries["Basic Salary:"].insert(0, employee.basic_salary)
                    self.entries["Age:"].delete(0, tk.END)
                    self.entries["Age:"].insert(0, employee.age)
                    self.entries["Date of Birth:"].delete(0, tk.END)
                    self.entries["Date of Birth:"].insert(0, employee.dob)
                    self.entries["Passport Details:"].delete(0, tk.END)
                    self.entries["Passport Details:"].insert(0, employee.passport_details)
                    return
            messagebox.showinfo("Error", "Employee not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No employees found.")

def main():
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
