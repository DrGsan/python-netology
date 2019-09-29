from application.salary import calculate_salary
from application.db.people import get_employees


def task():
    calculate_salary()
    get_employees()
    print('-'*50)
    print('Looks like everything is fine')
    print('It was main.py')
    print('-'*50)
    print('-'*50)
    return


if __name__ == '__main__':
    task()