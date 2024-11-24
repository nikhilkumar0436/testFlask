import random
from flask import *
from flask_migrate import Migrate
from flask_sqlalchemy import *

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# @app.route('/admin')
def admin():
    return 'test'


app.add_url_rule('/admin', 'admin1', admin)


@app.route('/test/<name>')
def test(name):
    return render_template('base.html', name=name)


@app.route('/tes/<name>')
def tes(name):
    k = {'a': 1, 'b': 2}
    k[name] = 5
    return render_template('base1.html', name=k)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passw = request.args.get('pass')
    if uname == 'nikhil' and passw == 'hi':
        return 'welcome %s' % uname
    else:
        return 'invalid'


@app.route('/login', methods=['POST'])
def loginp():
    uname = request.form['uname']
    passw = request.form['pass']
    if uname == 'nikhil' and passw == 'hi':
        return 'welcome %s' % uname


@app.route('/user/<name>/<int:test>')
def user(name, test):
    if name == 'admin':
        print(test)
        return redirect(url_for('admin'))
    else:
        return 'hi'


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name, age):

        self.id = random.random()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add',methods=['POST'])
def add_data():
    fname = request.form['first_name']
    lname = request.form['last_name']
    age = request.form['age']
    record = Profile(fname, lname, age)
    db.session.add(record)

    return 'submitted successfully'


@app.route('/view',methods=['GET'])
def view_data():

    profiles=db.session.execute(db.select(Profile)).scalars()
    # print(profiles)
    for pro in profiles:
        print(pro.first_name)

    return render_template('view_profile.html',profile=profiles)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
