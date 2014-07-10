from bottle import route, run, template, get, post, request

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


# FILTERS
@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()

# @route('/static/<path:path>')
# def callback(path):
#     return static_file(path, ...)


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
	if(username == "abcd" and password == "abcd"):
		return True
	else:
		return False

# route static files
from bottle import static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/Users/tokhi/Documents/python/web')

# Error pages
from bottle import error
@error(404)
def error404(error):
    return 'Nothing here, sorry'


# changing the default encoding
from bottle import response
@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15'
    return u'This will be sent with ISO-8859-15 encoding.'

@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9.'



run(host='localhost', port=8080, debug=True)