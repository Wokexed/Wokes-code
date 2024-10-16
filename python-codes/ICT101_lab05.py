class Employees:
    def __init__(self, name, employee_id, age):
        self.name = name
        self.employee_id = employee_id
        self.age = age
    
    def hire(self):
        print(f"{self.name} has been hired.")
    
    def resign(self):
        print(f"{self.name} has resigned.")

class Fulltime(Employees):
    def __init__(self, name, employee_id, age, monthly_salary, business_title):
        super().__init__(name, employee_id, age)
        self.monthly_salary = monthly_salary
        self.business_title = business_title

    def calculate_bonus(self):
        bonus = float(self.monthly_salary * 2.5)
        print(f"{self.name} has been paid a bonus of ${bonus}.")

    def request_overtime(self):
        print("This is a placeholder")
    def promote(self):
        print(f"{self.name} has been promoted to {self.business_title}.")

class Parttime(Employees):
    def __init__(self, name, employee_id, age, hourly_pay, hours_per_week):
        super().__init__(name, employee_id, age)
        self.hourly_pay = hourly_pay
        self.hours_per_week = hours_per_week

    def calculate_pay(self):
        pay = self.hourly_pay  * self.hours_per_week
        print(f"{self.name} is paid a weekly pay of ${pay}")



fulltime_employee = Fulltime("John Doe", "FT123", 30, 5000, "Senior management")
fulltime_employee.hire()
fulltime_employee.calculate_bonus()
fulltime_employee.promote()
fulltime_employee.resign()

parttime_employee = Parttime("Jane Smith", "PT123", 25, 20, 20)
parttime_employee.hire()
parttime_employee.calculate_pay()