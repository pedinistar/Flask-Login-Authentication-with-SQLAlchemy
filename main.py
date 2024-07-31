from flask import Flask, render_template, redirect, url_for, flash, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask_login import LoginManager, UserMixin,login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
db_url = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


Base = declarative_base()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

login_manager = LoginManager()
login_manager.login_view = 'login'


class User(Base, UserMixin):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  email = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)

  def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


Base.metadata.create_all(engine)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


@app.route('/')
def index():
  return render_template('index.html', current_user=current_user)


@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(
      password=password, method='pbkdf2:sha256')
    user = User(username, email, hashed_password)
    session.add(user)
    session.commit()
    flash('Registration successful! Please login.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    user = session.query(User).filter(User.email==email).first()
    if user and check_password_hash(user.password, password=password):
      login_user(user=user)
      return redirect(url_for('home'))
    else:
      flash('Login failed. Check your email and/or password', 'danger')
  return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
  return f'Hello, {current_user.username}! Welcome to your dashboard.'

if __name__ == '__main__':
  app.run(debug=True)
