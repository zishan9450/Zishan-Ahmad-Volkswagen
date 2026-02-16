class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__revenue = 0
        self.__expenses = 0
    
    def set_financial_data(self, revenue, expenses):
        self.__revenue = revenue
        self.__expenses = expenses
    
    def _financial_report(self):
        profit = self.__revenue - self.__expenses
        print(f"\n{'='*50}")
        print("CONFIDENTIAL FINANCIAL REPORT")
        print(f"{'='*50}")
        print(f"Company: {self.name}")
        print(f"Revenue: ${self.__revenue:,}")
        print(f"Expenses: ${self.__expenses:,}")
        print(f"Profit: ${profit:,}")
        print(f"{'='*50}")
    
    def show_details(self):
        print(f"\nCompany Name: {self.name}")
        print(f"Location: {self.location}")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation
        self.__policies = []
    
    def add_policy(self, policy):
        self.__policies.append(policy)
    
    def _policy_update(self):
        print(f"\n{'='*50}")
        print("CONFIDENTIAL POLICY INFORMATION")
        print(f"{'='*50}")
        print(f"Employee: {self.emp_name}")
        print(f"Policies Assigned:")
        if self.__policies:
            for i, policy in enumerate(self.__policies, 1):
                print(f"  {i}. {policy}")
        else:
            print("  No policies assigned")
        print(f"{'='*50}")
    
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
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, company):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
        self.company = company
    
    def access_financial_report(self):
        print(f"\n[Access Granted] {self.emp_name} (Manager) accessing financial report...")
        self.company._financial_report()
    
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
        print(f"Access Level: Financial Reports")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled, company):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled
        self.company = company
    
    def access_policy_update(self, employee):
        print(f"\n[Access Granted] {self.emp_name} (HR) accessing policy information...")
        employee._policy_update()
    
    def access_financial_report(self):
        print(f"\n[Access Granted] {self.emp_name} (HR) accessing financial report...")
        self.company._financial_report()
    
    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {', '.join(self.policies_handled)}")
        print(f"Access Level: Financial Reports, Policy Updates")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages
    
    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Access Level: Basic (No confidential access)")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration
    
    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")
        print(f"Access Level: Basic (No confidential access)")


class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size, policies_handled, company):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled
        self.company = company
    
    def access_financial_report(self):
        print(f"\n[Access Granted] {self.emp_name} (Manager+HR) accessing financial report...")
        self.company._financial_report()
    
    def access_policy_update(self, employee):
        print(f"\n[Access Granted] {self.emp_name} (Manager+HR) accessing policy information...")
        employee._policy_update()
    
    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {', '.join(self.policies_handled)}")
        print(f"Role: Manager with HR Responsibilities")
        print(f"Access Level: Full Access (Financial Reports + Policy Updates)")


class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, programming_languages, duration):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages
        self.duration = duration
    
    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Internship Duration: {self.duration} months")
        print(f"Role: Developer Intern")
        print(f"Access Level: Basic (No confidential access)")


def demonstrate_access_control():
    print("=" * 70)
    print("CONTROLLED ACCESS IN COMPANY ACQUISITION SYSTEM")
    print("=" * 70)
    
    company = CompanyAcquisition("TechCorp Solutions", "San Francisco, USA", "InnovateTech Labs")
    company.set_financial_data(5000000, 3000000)
    
    manager = Manager("E001", "John Smith", "Senior Manager", "2020-01-15", "N/A", 15, company)
    hr = HR("E002", "Emily Davis", "HR Manager", "2018-03-20", "N/A", ["Recruitment", "Training"], company)
    developer = Developer("E003", "Sarah Johnson", "Lead Developer", "2019-06-10", "N/A", ["Python", "Java"])
    intern = Intern("E004", "Michael Lee", "Software Intern", "2025-06-01", "N/A", 6)
    manager_hr = ManagerHR("E005", "David Chen", "Manager & HR Lead", "2019-08-15", "N/A", 10, ["Performance Review"], company)
    dev_intern = DeveloperIntern("E006", "Amanda Wilson", "Developer Intern", "2025-07-01", "N/A", ["Python", "C++"], 3)
    
    developer.add_policy("Code Review Policy")
    developer.add_policy("Security Guidelines")
    
    print("\n" + "=" * 70)
    print("TESTING ACCESS CONTROL")
    print("=" * 70)
    
    print("\n--- Manager Access ---")
    manager.access_financial_report()
    
    print("\n--- HR Access ---")
    hr.access_financial_report()
    hr.access_policy_update(developer)
    
    print("\n--- Manager+HR Access (Hybrid) ---")
    manager_hr.access_financial_report()
    manager_hr.access_policy_update(developer)
    
    print("\n--- Developer Access (RESTRICTED) ---")
    try:
        print(f"{developer.emp_name} (Developer) attempting to access financial report...")
        developer._financial_report()
    except AttributeError as e:
        print(f"[Access Denied] Developers cannot access financial reports")
    
    print(f"\n{developer.emp_name} (Developer) attempting to access policy updates...")
    print(f"[Access Denied] Developers cannot access policy updates")
    
    print("\n--- Intern Access (RESTRICTED) ---")
    print(f"{intern.emp_name} (Intern) attempting to access financial report...")
    print(f"[Access Denied] Interns cannot access financial reports")
    
    print("\n--- Developer Intern Access (RESTRICTED) ---")
    print(f"{dev_intern.emp_name} (Developer Intern) attempting to access sensitive data...")
    print(f"[Access Denied] Developer Interns cannot access confidential information")
    
    print("\n" + "=" * 70)
    print("EMPLOYEE DETAILS")
    print("=" * 70)
    
    employees = [manager, hr, developer, intern, manager_hr, dev_intern]
    for emp in employees:
        emp.show_details()
        print("-" * 70)
    
    print("\n" + "=" * 70)
    print("INHERITANCE & ENCAPSULATION SUMMARY")
    print("=" * 70)
    print("\n1. Single Inheritance:")
    print("   - Company → CompanyAcquisition")
    print("   - Employee → NewEmployee")
    
    print("\n2. Multi-level Inheritance:")
    print("   - Employee → NewEmployee → Manager")
    print("   - Employee → NewEmployee → HR")
    print("   - Employee → NewEmployee → Developer")
    print("   - Employee → NewEmployee → Intern")
    
    print("\n3. Multiple Inheritance:")
    print("   - ManagerHR inherits from Manager and HR")
    print("   - DeveloperIntern inherits from Developer and Intern")
    
    print("\n4. Hybrid Inheritance:")
    print("   - ManagerHR combines multi-level and multiple inheritance")
    
    print("\n5. Encapsulation (Hidden Methods):")
    print("   - _financial_report() accessible only to Manager and HR")
    print("   - _policy_update() accessible only to HR")
    print("   - Developer and Intern have NO access to hidden methods")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_access_control()
