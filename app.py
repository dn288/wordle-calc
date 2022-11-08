import os, re
from flask import Flask, redirect, render_template, request, flash


# create and configure app
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="afvabrtkdfporgjae12541")
    

# simple wordle score calculator
@app.route("/", methods=["GET", "POST"])
def wordle_calc():
    if request.method == "POST":
        game = request.form.get("game")
        stats = request.form.get("stats")
        if not game:
            flash("ERROR - Please select game!", category="err")
            return render_template("wordle_calc.html")
        if not stats:
            flash("ERROR - Please choose enter stats!", category="err")
            return render_template("wordle_calc.html")

        try:
            z = extract(stats)
            s = fscore(score(z))
            total_played = z[0][1]  
            labels = [row[0] for row in z[2:]]
            values = [row[1]*100/z[0][1] for row in z[2:]]
            
            flash("SUCCESS!")
            return render_template("results.html", game=game, labels=labels, values=values, s=s, total_played=total_played)
        except:
            flash("ERROR - Stats format not valid! Please check instructions.", category="err")
            return render_template("wordle_calc.html")
    else:
        return render_template("wordle_calc.html")

@app.route("/formula")
def formula():
    return render_template("formula.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/links")
def links():
    return render_template("links.html")


def fscore(x):
    """format score to 3 decimals"""
    return "%.3f" % x


def extract(x):
    """extract data from info pasted"""
    y = re.search(r"^([A-Z]+\s\s?([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s([0-9][0-9]?[0-9]?)\s%?\s?[a-zA-Z]+\s\%?\s?([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s[a-zA-Z]+\s([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s[a-zA-Z]+\s[A-Z]+\s[A-Z]+\s\s?1\s([0-9][0-9]?)\s2\s([0-9][0-9]?[0-9]?)\s3\s([0-9][0-9]?[0-9]?)\s4\s([0-9][0-9]?[0-9]?)\s5\s([0-9][0-9]?[0-9]?)\s6\s([0-9][0-9]?[0-9]?))", x)
    if y:
        totl = int(y.group(2))
        ones = int(y.group(6))
        twos = int(y.group(7))
        threes = int(y.group(8))
        fours = int(y.group(9))
        fives = int(y.group(10))
        sixes =  int(y.group(11))
        total_solved = ones + twos + threes + fours + fives + sixes

        z = [
                ("total", totl),
                ("total_solved", total_solved),
                ("1/6", ones),
                ("2/6", twos),
                ("3/6", threes),
                ("4/6", fours),
                ("5/6", fives),
                ("6/6", sixes),
                ("X/6", totl - total_solved),
            ]
        return z
    else:
        raise exception


def score(z):
    a = z[2][1]*1 + z[3][1]*2 + z[4][1]*3 + z[5][1]*4 + z[6][1]*5 + z[7][1]*6
    b = z[0][1] - z[8][1]
    c = z[1][1] / z[0][1]
    d = (a/b)/c
    return d


if __name__=="__main__":
    app.debug = True
    app.run()
