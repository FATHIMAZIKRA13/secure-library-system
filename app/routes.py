from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, Book, Loan
from app.forms import RegistrationForm, LoginForm, BookForm
from datetime import datetime
import os
from werkzeug.utils import secure_filename

# PDF Upload Folder
UPLOAD_FOLDER = 'static/pdfs'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/dashboard')
@login_required
def dashboard():
    books = Book.query.all()
    my_loans = Loan.query.filter_by(user_id=current_user.id, return_date=None).all()
    return render_template('dashboard.html', books=books, my_loans=my_loans)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role='member')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if current_user.role != 'admin':
        flash('Only admins can add books!', 'danger')
        return redirect(url_for('dashboard'))
    
    form = BookForm()
    if form.validate_on_submit():
        pdf_filename = None
        if form.pdf.data:
            pdf = form.pdf.data
            pdf_filename = secure_filename(pdf.filename)
            pdf.save(os.path.join(UPLOAD_FOLDER, pdf_filename))

        book = Book(
            title=form.title.data,
            author=form.author.data,
            isbn=form.isbn.data,
            quantity=form.quantity.data,
            available=form.quantity.data,
            pdf_filename=pdf_filename
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_book.html', form=form)