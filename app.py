from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with the description of the problem and solution."""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)