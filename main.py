from application.salary import calculate_salary
from application.db.people import get_employees
from application.dt.dt import today_date


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    today_date()
