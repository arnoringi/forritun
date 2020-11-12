# Weekly salaries

class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        Employee.__init__(self, name)
        self.wage = wage
    
    def weekly_pay(self, hours):
        HOURS = 40
        OVERTIME = 1.5

        if hours > HOURS:
            pay = (self.wage * HOURS) + (self.wage * OVERTIME * (hours - HOURS))
        else:
            pay = self.wage * hours
        return pay

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name)
        self.salary = salary

    def weekly_pay(self, hours):
        WEEKS = 52
        pay = self.salary / WEEKS
        return pay

class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        SalariedEmployee.__init__(self, name, salary)
        self.bonus = bonus

    def weekly_pay(self, hours):
        return SalariedEmployee.weekly_pay(self, hours) + self.bonus



# def print_salaries(staff):
#     for employee in staff:
#         name = employee.get_name()
#         hours = int(input("Hours worked by " + name + ": "))
#         pay = employee.weekly_pay(hours)
#         print("{}: {:.2f}".format(name, pay))

# # The main program starts here
# staff = []
# staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
# staff.append(SalariedEmployee("Sally Lin", 52000.0)) # 52000 is the annual salary
# staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
# print_salaries(staff)