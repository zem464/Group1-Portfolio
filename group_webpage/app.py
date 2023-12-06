from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/work', methods=['GET', 'POST'])
def work():
    return render_template('work.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
