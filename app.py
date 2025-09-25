from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/english')
def english():
    return render_template('english.html')

@app.route('/tamil')
def tamil():
    return render_template('tamil.html')

@app.route('/sinhala')
def sinhala():
    return render_template('sinhala.html')

@app.route('/korean')
def korean():
    return render_template('korean.html')

if __name__ == '__main__':
    app.run(debug=True)
