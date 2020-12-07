from flask import Flask, redirect, render_template, request, url_for
import random
from tempfile import mkdtemp
from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.jinja_env.cache = {}

app.run(host="0.0.0.0", port=8080, threaded=True)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/coin", methods=["GET", "POST"])
def coin():
    if request.method == "POST":
        heads = request.form.get("formHeads")
        tails = request.form.get("formTails")
        rand = random.randint(0, 1)
        if rand == 0:
            result = "Heads"
            outcome = heads
        else:
            result = "Tails"
            outcome = tails
        return render_template("results.html", result=result, outcome=outcome,  type="coin")
    else:
        return render_template("coin.html")

@app.route("/dice", methods=["GET", "POST"])
def dice():
    if request.method == "POST":
        outcome1 = request.form.get("outcome1")
        outcome2 = request.form.get("outcome2")
        outcome3 = request.form.get("outcome3")
        outcome4 = request.form.get("outcome4")
        outcome5 = request.form.get("outcome5")
        outcome6 = request.form.get("outcome6")
        rand = random.randint(1, 6)
        if rand == 1:
            result = "outcome1"
            outcome = outcome1
        elif rand == 2:
            result = "outcome2"
            outcome = outcome2
        elif rand == 3:
            result = "outcome3"
            outcome = outcome3
        elif rand == 4:
            result = "outcome4"
            outcome = outcome4
        elif rand == 5:
            result = "outcome5"
            outcome = outcome5
        elif rand == 6:
            result = "outcome6"
            outcome = outcome6
        return render_template("results.html", result=result, outcome=outcome, type="dice")
    else:
        return render_template("dice.html")

@app.route("/ball", methods=["GET", "POST"])
def ball():
    if request.method == "POST":
        outcomes = ["It is certain", " It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", " Outlook not so good.", "Very doubtful."]
        rand = random.randint(0, 19)
        result = "8ball"
        outcome = outcomes[rand]
        return render_template("results.html", result=result, outcome=outcome, type="ball")
    else:
        return render_template("ball.html")

@app.route("/custom", methods=["GET", "POST"])
def custom():
    if request.method == "POST":
        no_of_choices = int(request.form.get("choices"))
        choices = range(no_of_choices)
        return render_template("customed.html", choices=choices)
    else:
        return render_template("custom.html")

@app.route("/customed", methods=["GET", "POST"])
def customed():
    if request.method == "POST":
        count = 0
        while request.form.get("choice" + str(count + 1)) != None:
            count += 1
        rand = random.randint(1, count)
        outcome = request.form.get("choice" + str(rand))
        return render_template("results.html", outcome=outcome, result="questions", type="custom")
    else:
        return render_template("custom.html")

if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)