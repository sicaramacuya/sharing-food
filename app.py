from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """A homepage with the description of the problem and solution."""
    return render_template('home.html')

@app.route('/donate')
def donate_page():
    """A page where the donor can donate food."""
    return render_template('donate.html')

@app.route('/volunteer')
def volunteer_page():
    """A page where the volunteer can see the differents donations he/she can transport."""
    return render_template('volunteer.html')

@app.route('/profile')
def profile_page():
    """A page where the user can see their stats."""
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)