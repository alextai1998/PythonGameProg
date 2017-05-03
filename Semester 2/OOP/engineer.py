# Python OOP


class Employee:

    # class variables:
    numOfEmp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numOfEmp += 1

    def fullname(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    num_of_developer = 0
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
        Developer.num_of_developer += 1


class Manager(Employee):
    num_of_manager = 0

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        Manager.num_of_manager += 1

    def add_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())


class Engineer(Employee):
    num_of_engineer = 0

    def __init__(self, first, last, pay, department):
        super().__init__(first, last, pay)
        self.department = department
        Engineer.num_of_engineer += 1


dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'Java')
print(isinstance(dev1, Developer))


eng_1 = Engineer('Alex', 'Tai', 70000, 'Department 1')
print(eng_1.fullname())
print(eng_1.department)
print(Engineer.num_of_engineer)
