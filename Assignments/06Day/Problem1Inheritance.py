class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def show_details(self):
        print(f"\nCompany Name: {self.name}")
        print(f"Location: {self.location}")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation
    
    def show_details(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


class CompanyAcquisition(Company):
    def __init__(self, name, location, acquired_company_name):
        super().__init__(name, location)
        self.acquired_company_name = acquired_company_name
        self.existing_employees = []
        self.acquired_employees = []
    
    def add_existing_employee(self, employee):
        self.existing_employees.append(employee)
    
    def add_acquired_employee(self, employee):
        self.acquired_employees.append(employee)
    
    def show_details(self):
        super().show_details()
        print(f"Acquired Company: {self.acquired_company_name}")
        print(f"\nTotal Existing Employees: {len(self.existing_employees)}")
        print(f"Total Acquired Employees: {len(self.acquired_employees)}")
        print(f"Total Merged Employees: {len(self.existing_employees) + len(self.acquired_employees)}")
        
        if self.existing_employees:
            print("\n--- Existing Employees ---")
            for emp in self.existing_employees:
                emp.show_details()
        
        if self.acquired_employees:
            print("\n--- Acquired Employees ---")
            for emp in self.acquired_employees:
                emp.show_details()


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company
    
    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
    
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled
    
    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {', '.join(self.policies_handled)}")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages
    
    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration
    
    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")


class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, policies_handled):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled
    
    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {', '.join(self.policies_handled)}")
        print("Role: Manager with HR Responsibilities")


class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages, duration):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages
        self.duration = duration
    
    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Internship Duration: {self.duration} months")
        print("Role: Developer Intern")


def main():
    print("=" * 60)
    print("COMPANY ACQUISITION MANAGEMENT SYSTEM")
    print("=" * 60)
    
    company = CompanyAcquisition("TechCorp Solutions", "San Francisco, USA", "InnovateTech Labs")
    
    existing_emp1 = Manager("E001", "John Smith", "Senior Manager", "2020-01-15", "N/A", 15)
    existing_emp2 = Developer("E002", "Sarah Johnson", "Lead Developer", "2019-06-10", "N/A", ["Python", "Java", "JavaScript"])
    existing_emp3 = HR("E003", "Emily Davis", "HR Manager", "2018-03-20", "N/A", ["Recruitment", "Training", "Employee Relations"])
    
    company.add_existing_employee(existing_emp1)
    company.add_existing_employee(existing_emp2)
    company.add_existing_employee(existing_emp3)
    
    acquired_emp1 = Developer("A001", "Michael Brown", "Full Stack Developer", "2021-02-10", "InnovateTech Labs", ["Python", "React", "Node.js"])
    acquired_emp2 = Intern("A002", "Jessica Wilson", "Software Intern", "2025-06-01", "InnovateTech Labs", 6)
    acquired_emp3 = ManagerHR("A003", "David Lee", "Manager & HR Lead", "2019-08-15", "InnovateTech Labs", 10, ["Performance Review", "Compliance"])
    acquired_emp4 = DeveloperIntern("A004", "Amanda Chen", "Developer Intern", "2025-07-01", "InnovateTech Labs", ["Python", "C++"], 3)
    
    company.add_acquired_employee(acquired_emp1)
    company.add_acquired_employee(acquired_emp2)
    company.add_acquired_employee(acquired_emp3)
    company.add_acquired_employee(acquired_emp4)
    
    company.show_details()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATING POLYMORPHISM")
    print("=" * 60)
    
    employees_list = [existing_emp1, existing_emp2, existing_emp3, acquired_emp1, 
                      acquired_emp2, acquired_emp3, acquired_emp4]
    
    for emp in employees_list:
        emp.show_details()
        print("-" * 60)
    
    print("\n" + "=" * 60)
    print("INHERITANCE HIERARCHY DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. Single Inheritance:")
    print("   Company → CompanyAcquisition")
    
    print("\n2. Multi-level Inheritance:")
    print("   Employee → NewEmployee → Manager")
    print("   Employee → NewEmployee → HR")
    print("   Employee → NewEmployee → Developer")
    print("   Employee → NewEmployee → Intern")
    
    print("\n3. Multiple Inheritance:")
    print("   ManagerHR inherits from both Manager and HR")
    print("   DeveloperIntern inherits from both Developer and Intern")
    
    print("\n4. Hybrid Inheritance:")
    print("   Combination of multi-level and multiple inheritance")
    print("   Example: ManagerHR (Manager → NewEmployee → Employee) + HR")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
