from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trivia")
def trivia():
    return render_template("trivia.html")

@app.route("/memory")
def memory():
    return render_template("memory.html")

if __name__ == "__main__":
    app.run(debug=True)