from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:name>')
def home(name):
    return render_template(name)
    
# @app.route('/day')
# def day():
#     return render_template('/day.html')

# @app.route('/addfood')
# def add_food():
#     return render_template('/add_food.html')