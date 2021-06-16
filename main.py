from flask import Flask
from flask import render_template
from flask import request
from flask_wtf.csrf import CsrfProtect
from werkzeug import datastructures
import forms

from flask_wtf import CSRFProtect

from models import db
from models import User

from config import DevelopmentConfig

from flask import flash

app =Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()

@app.route('/', methods = ['GET', 'POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
        
    title = 'Curso Flask'
    return render_template('index.html', title=title, form = comment_form)

@app.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = forms.CreateForm (request.form)
    if request.method == 'POST' and create_form.validate():

        user =User (create_form.username.data,
                    create_form.email.data,
                    create_form.password.data)

        db.session.add(user)
        db.session.commit()

    return render_template('create.html', form = create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=8000)
