from flask import abort, render_template
from flask_login import current_user, login_required
from ..models import Department, Employee, Role

from . import home
from .. import db

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

# Department View

# prevent non-admins from accessing the page
@home.route('/departments', methods=['GET', 'POST'])
def list_departments():
    """
    List all departments
    """

    departments = Department.query.all()

    return render_template('home/departments/departments.html',
                           departments=departments, title="Departments")

@home.route('/departments/view/<int:id>', methods=['GET', 'POST'])
def list_department_employees(id):
    """
    Display department's employees
    """
    employees = Employee.query.filter_by(department_id=id).all()
    department = Department.query.get_or_404(id)
    print employees
    return render_template('home/departments/department.html', employees=employees, department=department, itle="Department Employees")

# Employee Views

@home.route('/employees')
def list_employees():
    """
    List all employees
    """
    employees = Employee.query.all()
    print employees
    return render_template('home/employees/employees.html',
                           employees=employees, title='Employees')
