from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField 


class QuestionForm(FlaskForm):
	subject = StringField('제목', validators=[DataRequired('제목을 입력해주세요')])
	content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

class AnswerForm(FlaskForm):
	content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

class UserCreateForm(FlaskForm):
	username = StringField('아이디', validators=[DataRequired(), Length(min=3, max=20)])
	password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
	password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
	email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
	username = StringField('아이디', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField('비밀번호', validators=[DataRequired()])

class CommentForm(FlaskForm):
	content = TextAreaField('내용', validators=[DataRequired()])
