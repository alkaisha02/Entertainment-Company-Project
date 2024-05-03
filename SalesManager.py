from Entities.Employee import Employee

class SalesManager(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details, team_size):
        """
        Constructor method to initialize attributes of the SalesManager class.
        
        Parameters:
            name (str): The name of the sales manager.
            employee_id (str): Unique identifier for the sales manager.
            department (str): The department in which the sales manager works.
            job_title (str): The job title or role of the sales manager.
            basic_salary (float): The basic salary of the sales manager.
            age (int): The age of the sales manager.
            dob (str): The date of birth of the sales manager.
            passport_details (str): Information about the passport of the sales manager.
            team_size (int): The size of the sales team managed by the sales manager.
        """
        super().__init__(name, employee_id, department, job_title, basic_salary, age, dob, passport_details)
        self.team_size = team_size
        
    def display_details(self):
        """
        Method to display the details of the sales manager, including inherited details from the Employee class.
        """
        super().display_details()
        print("Team Size:", self.team_size)
class SalesManager:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details, team_size):
       
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details
        self.team_size = team_size
  