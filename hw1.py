"""Salary analysis."""


def get_best_salaries(ignored_depts: tuple = None, **dept_employees) -> tuple:
    """Calculate employee salary statistics.

    Args:
        ignored_depts (Tuple): depts ignored when calculating statistics.
        dept_employees: the key is the name of the department, the value is a dictionary.

    Returns:
        Tuple: the first element is a tuple of 3 employees,
        and the second element is a float number.
    """
    employees = {}
    for dept, employees_salaries in dept_employees.items():
        if ignored_depts is None or dept not in ignored_depts:
            for key in employees_salaries.keys():
                employees_salaries[key] = round(employees_salaries[key], 2)
            employees.update(employees_salaries)
    best_salaried_employees = sorted(employees.items(), key=get_employee_salary, reverse=True)[:3]
    best_salaries_sum = sum(employee[1] for employee in best_salaried_employees)
    salaries_sum = sum(salary for salary in employees.values())

    percent = round((best_salaries_sum / salaries_sum) * 100, 2)

    return best_salaried_employees, percent


def get_employee_salary(employee: tuple):
    """Get employee salary.

    Args:
        employee (Tuple): employee with his salary.

    Returns:
        int: employee salary.
    """
    return employee[1]
