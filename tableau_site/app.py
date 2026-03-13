from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboards")
def dashboards():
    return render_template("dashboards.html")

@app.route("/worksheets")
def worksheets():
    return render_template("worksheets.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

if __name__ == "__main__":
    app.run(debug=True)