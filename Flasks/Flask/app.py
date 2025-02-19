from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to flask course hii i am here hello pin is here"

if __name__ == "__main__":
    app.run(debug=True)