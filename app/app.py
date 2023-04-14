from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import re
from flashtext import KeywordProcessor
import spacy
from IDP_filter import filter_text_with_regex, filter_text_with_flashtext, filter_text_with_nlp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'some_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    sensitive_words = db.Column(db.String, nullable=True)
    non_sensitive_words = db.Column(db.String, nullable=True)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

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
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        user = User.query.filter_by(username=username, password=password_hash).first()
        if user:
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
        sensitive_words = ' '.join(request.form['sensitive_words'].split())
        non_sensitive_words = ' '.join(request.form['non_sensitive_words'].split())

        # sensitive_words = request.form['sensitive_words']
        # non_sensitive_words = request.form['non_sensitive_words']
        user.sensitive_words = sensitive_words
        user.non_sensitive_words = non_sensitive_words
        db.session.commit()
        flash('Words updated successfully.')

    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.')
    return redirect(url_for('index'))

nlp = spacy.load("en_core_web_sm")

# 创建一个敏感词数据库（这里只是一个示例，你可以根据需要添加更多词汇）
sensitive_word_db = ["China", "India", "United States"]

# 预先编译正则表达式
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# 添加一个新的路由处理过滤文本
@app.route('/filter_text', methods=['POST'])
def filter_text():
    if 'user_id' not in session:
        flash('Please log in to access the text filtering feature.')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    input_text = request.form['input_text']

    # 获取用户自定义敏感词
    user_sensitive_words = user.sensitive_words.split()

    # 合并用户自定义敏感词和敏感词数据库
    all_sensitive_words = user_sensitive_words + sensitive_word_db

    filtered_text_regex = filter_text_with_regex(input_text, all_sensitive_words)
    filtered_text_flashtext = filter_text_with_flashtext(input_text, all_sensitive_words)
    filtered_text_nlp = filter_text_with_nlp(input_text, all_sensitive_words)

    return render_template('dashboard.html', user=user, input_text=input_text,
                           filtered_text_regex=filtered_text_regex,
                           filtered_text_flashtext=filtered_text_flashtext,
                           filtered_text_nlp=filtered_text_nlp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
