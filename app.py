from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Модель для пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)


# Главная страница
@app.route('/')
def home():
    return render_template('index.html')


# Регистрация
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Проверка уникальности пользователя
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User with this email already exists.', 'danger')
            return redirect(url_for('register'))

        # Добавление пользователя в базу данных
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')


# Инициализация базы данных
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)