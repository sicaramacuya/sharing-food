from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """A homepage with the description of the problem and solution."""
    return render_template('home.html')

@app.route('/donate')
def donate_page():
    """A page where the user can donate food."""
    return render_template('donate.html')
    
if __name__ == '__main__':
    app.run(debug=True)