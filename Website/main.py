from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/wikipedia')
def wikipedia():
    return render_template('wikipedia.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
