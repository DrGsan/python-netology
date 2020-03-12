from application.db.people import get_employees
from application.salary import calculate_salary


def task():
    calculate_salary()
    get_employees()
    print('-'*50)
    print('Looks like everything is fine')
    print('It was test.py')
    print('-'*50)
    print('-'*50)
    return


if __name__ == '__main__':
    task()