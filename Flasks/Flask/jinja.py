from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<HTML><H1>hello Flask tushar</H1></HTML>"

@app.route("/index" ,methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('submit.html')

@app.route("/submit" , methods = ['GET','POST'])
def submit():
    if request.method == "POST":
        submit = request.form['name']
        return f'hello{submit}'
    return render_template['form.html']

#variable Rule
@app.route('/success/<int:score>')
def success(score):
    result = ""
    if score >= 35:
        result = "passed"
    else:
        result="failed"
    return render_template('result.html',results = result)


if __name__ == "__main__":
    app.run(debug=True)