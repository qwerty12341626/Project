from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")


@app.route('/methodology')
def methodology():
    return render_template("methodology.html")


@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)