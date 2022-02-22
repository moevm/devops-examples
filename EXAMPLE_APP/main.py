import os

from flask import Flask, abort, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

from bussiness_logic import allowed_file, check_password, create_folder, get_files_in_folder

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for filename in request.files:
            file = request.files[filename]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return {'files': get_files_in_folder(app.config['UPLOAD_FOLDER'])}
    return render_template("upload.html", files=get_files_in_folder(app.config['UPLOAD_FOLDER']))


@app.route('/download/<name>', methods=['GET'])
def download(name):
    print(name, get_files_in_folder(app.config['UPLOAD_FOLDER']))
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)


@app.route('/files', methods=['GET'])
def files():
    return render_template('files.html', files=get_files_in_folder(app.config['UPLOAD_FOLDER']))


@app.route('/to_files')
def to_files():
    return redirect(url_for('files'))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

# for ERR_TOO_MANY_REDIRECTS
@app.route('/increment/<int:a>')
def increment_int(a):
    return redirect(url_for('increment_int', a=a+1))

@app.route('/check_even/<int:a>')
def check_even(a):
    if a % 2 == 0: return redirect(url_for('even', a=a))
    else: return redirect(url_for('odd', a=a))

@app.route('/even/<int:a>')
def even(a):
    return redirect(url_for('check_even', a=a//2))

@app.route('/odd/<int:a>')
def odd(a):
    return "{} is odd".format(a)

@app.route('/login',methods = ['POST'])
def login():
    user = request.form['name']
    password = request.form['password']
    if check_password(user, password):
        return redirect(url_for('success',name = user))
    else:
        abort(401)
  
if __name__ == '__main__':
    create_folder(app.config['UPLOAD_FOLDER'])
    app.run(debug = True)
