from flask import Flask, render_template

app = Flask(__name__)

# Дані для меню
menu_items = [
    {"name": "Маргарита", "ingredients": "Томатний соус, сир моцарела, базилік", "price": "150 UAH"},
    {"name": "Пепероні", "ingredients": "Томатний соус, сир моцарела, пепероні", "price": "180 UAH"},
    {"name": "Чотири сири", "ingredients": "Томатний соус, моцарела, горгонзола, пармезан, дор блю", "price": "200 UAH"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True)