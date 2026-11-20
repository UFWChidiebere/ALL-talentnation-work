class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"Employee's details are: {self.name} with ID:{self.employee_id} work in {self.department} department and has a take home salary of {self.salary}")

    def increase_salary(self, new_salary):
        if new_salary < 0:
            print("Input a valid amount.")
            return
        # self.salary = new_salary
        self.salary += new_salary
        # return self.salary

    def change_department(self, new_department):
        self.department = new_department
        return f"Transferred to a new department: {self.department}"

    def annual_salary(self):
        self.salary * 12
        return f"Employee's annual salary is ${self.salary}"

employee1 = Employee("Wisdom", "W980876", "Cybersecurity", 250000)
employee2 = Employee("Chika", "C980876", "Tech", 450000)
employee3 = Employee("Nifemi", "N9808756", "IT", 250000)
employee4 = Employee("Ghost", "G980876RT", "Dark_Web", 100000)
employee5 = Employee("Unknown", "W980876thdbb", "Back_up", 4000000)

employees = [ employee1, employee2, employee3, employee4, employee5]
for employee in employees:
    employee.display_info()

employee3.increase_salary(500000)
print(employee3.display_info())