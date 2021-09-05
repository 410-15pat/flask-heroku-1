from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(_name_)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/hello/<string:name>')
def Home(name):
	return render_template('home.html', name_html=name)

@app.route('/name')
def name():
    return "<font color=blue>สัณหพร รัตนพาหิระ</font> <br> <font color=red>เลขที่26 ม.4/10</font> "

if _name_ == "_main_":
    app.run(debug=False)
