from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.models.user import User, db
# from src import db
from flask_login import login_user
from email_validator import validate_email, EmailNotValidError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validasi Email
        try:
            validate_email(email)
        except EmailNotValidError as e:
            flash(f"Invalid email: {str(e)}", 'error')
            return redirect(url_for('auth.register'))

        # Cek apakah username atau email sudah terdaftar
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('Email or username already registered', 'error')
            return redirect(url_for('auth.register'))

        # Buat user baru
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please check your email for verification.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
