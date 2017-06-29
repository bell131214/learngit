from flask import Flask,render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello, World123456!!"
#
# @app.route('/abc')
# def index():
#     return 'Index Page'
#
# @app.route('/hello')
# def hello():
#     return 'Hello World'
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)



if __name__=='__main__':
    app.run(debug=True)