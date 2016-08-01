from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from webapp.models import db, Post, Tag, Comment, User, tags, Recipie
from flask_wtf.file import FileField, FileAllowed, FileRequired

class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])

class LoginForm(Form):

    username= StringField('Username', [DataRequired(), Length(max=255)])
    password= PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember Me')
    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our the exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True

class RegisterForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    recaptcha= RecaptchaField()

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        if not check_validate:
            return False
        user = User.query.filter_by(username=self.username.data).first()

        if user:
            self.username.errors.append(
            "User with that name already exists"
            )
            return False
        return True

class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Content', [DataRequired()])

class RecipieForm(Form):
    title = StringField('Title',validators=[DataRequired(), Length(max=255)])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
