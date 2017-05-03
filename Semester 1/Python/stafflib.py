"""
This will serve as the Python library to save the functions that I will use for HW #15
"""

dataStructure = {"first_name": None,
                 "last_name": None,
                 "age": None,
                 "since": None,
                 "role": None,
                 "days": None,
                 "salary": None}  # Data template

employee = []  # Initialize empty employee list


def register(first_name, last_name, age, since, role, days, salary):
    """
    Registers new employee by passing arguments as information
    :param first_name: String of first name
    :param last_name: String of last name
    :param age: Integer of age
    :param since: String of vinculated since
    :param role: String of role
    :param days: Integer of days worked
    :param salary: Integer of salary
    :return: None
    """
    temp = dataStructure.copy()  # Creates a copy of template

    temp["first_name"] = first_name
    temp["last_name"] = last_name
    temp["age"] = age
    temp["since"] = since
    temp["role"] = role
    temp["days"] = days
    temp["salary"] = salary

    employee.append(temp)


def show_emp():
    """
    Prints the employees list in the given format of the assignment
    :return: None
    """
    print("Showing register of employees:")
    for num, emp in enumerate(employee):
        if emp["days"] != 1:
            print("Staff #%r: %s %s age %r has been working "
                  "%r days since %s as a %s for USD%r,"
                  % (num+1, emp["first_name"], emp["last_name"],
                     emp["age"], emp["days"], emp["since"], emp["role"], emp["salary"]))
        else:
            print("Staff #%r: %s %s age %r has been working "
                  "%r day since %s as a %s for USD%r,"
                  % (num+1, emp["first_name"], emp["last_name"],
                     emp["age"], emp["days"], emp["since"], emp["role"], emp["salary"]))
    print("Task Completed.")


def days_inc():
    """
    Increments the key-value pair = days worked by one for each employee
    :return: None
    """
    for emp in employee:
        emp["days"] += 1


def delist(first_name, last_name):
    """
    Removes an employee from the list
    :param first_name: String of first name
    :param last_name: String of last name
    :return: None
    """
    for emp in employee:
        if emp["first_name"] == first_name:
            if emp["last_name"] == last_name:
                employee.remove(emp)
