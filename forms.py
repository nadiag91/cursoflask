from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms.validators import email_validator

from wtforms import validators
from wtforms.fields.simple import PasswordField



def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    username  = StringField ('username', 
    [   validators.Required(message='campo obligatorio'), 
        validators.Length(min=4, max=25, message='Ingrese un username valido') 
    ])
    email = EmailField ('correo electronico', 
    [   validators.Required(message='campo obligatorio'), 
        ])
    comment = TextField ('comentario')
    honeypot = HiddenField('', [lenght_honeypot])

class LoginForm(Form):
    username = StringField('Username', [validators.data_required(message = 'Username requerido'),
    validators.length(min=4, max=25)])
    password = PasswordField('Password', [validators
    .data_required(message= 'Password obligatorio')])

#comment
class CreateForm(Form):
    username = TextField ('Username',
                [
                    validators.data_required(message = 'campo obligatorio')
                ])
    email = EmailField ('Email',
            [
                validators.data_required(message = 'campo obligatorio'),
                ])
    password = PasswordField ('Contraseña',
                [validators.data_required(message= 'Contraseña requerida')])