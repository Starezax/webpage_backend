from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# Main pages
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


# Wiki  subsections

@app.route('/wiki_ww1')
def wiki_ww1():
    return render_template('wiki_ww1.html')

@app.route('/wiki_ww2')
def wiki_ww2():
    return render_template('wiki_ww2.html')

@app.route('/wiki_ussr')
def wiki_ussr():
    return render_template('wiki_ussr.html')

@app.route('/wiki_1991')
def wiki_1991():
    return render_template('wiki_1991.html')

@app.route('/wiki_2014')
def wiki_2014():
    return render_template('wiki_2014.html')

@app.route('/wiki_2022')
def wiki_2022():
    return render_template('wiki_2022.html')


if __name__ == '__main__':
    app.run(debug=True)
