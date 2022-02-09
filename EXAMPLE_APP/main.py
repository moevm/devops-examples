from flask import Flask, redirect, url_for, request, render_template, abort
from bussiness_logic import check_password

app = Flask(__name__)
  

# TODO Add more functions to bussiness_logic

# TODO add some extremly stupid and unneccessary dependencies for bussiness logic

# TODO Add some js and images to include in templates/index.html (and spam console errors). JS should perform delayed rendering of some new markup on a web page

@app.route('/')
def index():
    return render_template("index.html")


# TODO Add route for file upload


# TODO Add route for file download

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
  
@app.route('/login',methods = ['POST'])
def login():
    user = request.form['name']
    password = request.form['password']
    if check_password(user, password):
        return redirect(url_for('success',name = user))
    else:
        abort(401)
  
if __name__ == '__main__':
   app.run(debug = True)
