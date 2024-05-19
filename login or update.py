from flask import render_template, flash, redirect, url_for, request
from forms import RegistrationForm, PatientForm
from models import User, Patient
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('patient'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('patient'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('patient'))
    return render_template('login.html', title='Login', form=form)

@app.route('/patient', methods=['GET', 'POST'])
@login_required
def patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(name=form.name.data, address=form.address.data, mobile_number=form.mobile_number.data, email_id=form.email_id.data, user_id=current_user.id)
        if form.profile_picture.data:
            patient.profile_picture = form.profile_picture.data
        if form.medical_records.data:
            patient.medical_records = form.medical_records.data
        if form.symptoms.data:
            patient.symptoms = form.symptoms.data
        db.session.add(patient)
        db.session.commit()
        flash('Your patient profile has been updated!')
        return redirect(url_for('patient'))
    patients = Patient.query.filter_by(user_id=current_user.id).all()
    return render_template('patient.html', title='Patient Profile', form=form, patients=patients)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))