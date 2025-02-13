from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@main.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return "Access Denied", 403
    return render_template('admin.html')