from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    mobile_number = StringField('Mobile Number', validators=[DataRequired()])
    email_id = StringField('Email ID', validators=[DataRequired(), Email()])
    profile_picture = FileField('Profile Picture', validators=[Optional()])
    medical_records = TextAreaField('Medical Records', validators=[Optional()])
    symptoms = TextAreaField('Symptoms', validators=[Optional()])
    submit = SubmitField('Save')