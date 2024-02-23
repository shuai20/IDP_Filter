from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
from IDPFilter_Flashtext import IDPFilter
#from IDPFilter_Flashtext_initial import IDPFilter
import os
from hashlib import pbkdf2_hmac

idp_filter = IDPFilter()

def hash_password(password):
    salt = os.urandom(16)  # generate16salt
    pwdhash = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + pwdhash

def verify_password(stored_password, provided_password):
    salt = stored_password[:16]  # get salt
    stored_pwdhash = stored_password[16:]
    pwdhash = pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == stored_pwdhash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'some_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
#    sensitive_words = db.Column(db.String, nullable=True)
#    non_sensitive_words = db.Column(db.String, nullable=True)
    name_filter = db.Column(db.Boolean, default=False)
    number_filter = db.Column(db.Boolean, default=False)
    link_filter = db.Column(db.Boolean, default=False)
    country_filter = db.Column(db.Boolean, default=False)
    disease_filter = db.Column(db.Boolean, default=False)
    streets_filter = db.Column(db.Boolean, default=False)
    self_regarding_blacklist = db.Column(db.String, nullable=True)  # SRB
    self_regarding_whitelist = db.Column(db.String, nullable=True)  # SRW
    others_regarding_blacklist = db.Column(db.String, nullable=True)  # ORB

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hash_password(password)
        #new password hash
        #password_hash = hashlib.sha256(password.encode()).hexdigest()

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose another one.')
        else:
            new_user = User(username=username, password=password_hash)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #password_hash = hashlib.sha256(password.encode()).hexdigest()

        user = User.query.filter_by(username=username).first()

        #user = User.query.filter_by(username=username, password=password_hash).first()
        if user and verify_password(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.')
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password.')

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        user.self_regarding_blacklist = request.form['self_regarding_blacklist']
        user.self_regarding_whitelist = request.form['self_regarding_whitelist']
        user.others_regarding_blacklist = request.form['others_regarding_blacklist']
        db.session.commit()
        flash('Words updated successfully.')
        user.name_filter = 'name_filter' in request.form
        print(user.name_filter)
        user.number_filter = 'number_filter' in request.form
        user.link_filter = 'link_filter' in request.form
        user.country_filter = 'country_filter' in request.form
        user.disease_filter = 'disease_filter' in request.form
        user.streets_filter = 'streets_filter' in request.form




        db.session.commit()
        flash('Settings updated successfully.')

    return render_template('Newdashboard.html', user=user)

@app.route('/filter_text', methods=['GET', 'POST'])
def filter_text():
    if 'user_id' not in session:
        flash('Please log in to access this page.')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    filtered_text = None

    if request.method == 'POST':
        input_text = request.form.get('text')
        # Pass the user's SRB, SRW, and ORB to the filter function
        #user_srb = user.self_regarding_blacklist or ''
        user_srw = user.self_regarding_whitelist or ''
        user_orb = user.others_regarding_blacklist or ''
        global_srb = ','.join([u.self_regarding_blacklist for u in User.query.all() if u.self_regarding_blacklist])
 #       sensitive_words = [word.strip() for word in user.sensitive_words.split(',')]
 #       non_sensitive_words = [word.strip() for word in user.non_sensitive_words.split(',')]

        selected_categories = request.form.getlist('categories') if request.form.getlist('categories') else None



        print("Selected Categories:", selected_categories)
        filtered_text, filtered_count = idp_filter.filter_text(input_text, user_orb, user_srw, global_srb,
                                                               selected_categories)
        #filtered_text, filtered_count = idp_filter.filter_text(input_text, sensitive_words, non_sensitive_words, selected_categories, global_srb, user_orw)

    return render_template('Newdashboard.html', user=user, filtered_text=filtered_text, filtered_count=filtered_count)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.')
    return redirect(url_for('index'))





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
