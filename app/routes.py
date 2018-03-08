from flask import render_template

from app import app

@app.route('/index1')
def index1():
    user = {'username': 'Sara'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
        <h1>Hello, '''
    <body> + user['username'] + '''!</h1>
    </body>
</html>'''


@app.route('/index2')
def index2():

    user = {'username': 'Sara Trickett'}
    return render_template('index.html', title='Home', user=user)


from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)