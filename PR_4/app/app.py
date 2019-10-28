#!myenv/bin/python
from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField
from wtforms.validators import InputRequired, DataRequired, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfkGL8UAAAAANKTCJY57zTjQYSmwF69rWbzaxLk'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfkGL8UAAAAADEjOKSQrGr2mqaqfEI73Y838zTg'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}
app.config['TESTING'] = True


class LoginForm(FlaskForm):
	username = StringField('Ведіть імя: ', validators = [InputRequired('Імя користувача є обовязкове!'), Length(min = 5, max= 10, message = 'Must be from 5 to 10 symb.')])
	password = PasswordField('Введіть пароль: ', validators = [InputRequired('Пароль є необхідний!'), AnyOf(values = ['password','secret'])])
	email = StringField('Email: ', validators = [DataRequired(), Length(min=6, max=35)] )
	recaptcha = RecaptchaField()



@app.route('/form', methods=['GET', 'POST'])
def form():
	form = LoginForm()
	if form.validate_on_submit():
		return '<h1> Імя користувача - {}. Пароль - {}. Email - {}'.format(form.username.data, form.password.data, form.email.data)
	return render_template('form.html', form = form)

if __name__ == '__main__':
	app.run(port=5000, debug=True)
