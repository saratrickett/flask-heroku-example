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
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sara Trickett'}
    return render_template('index.html', title='Home', user=user)
